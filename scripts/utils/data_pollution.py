import random
import pandas as pd
import numpy as np
import re
import os
from datetime import datetime

from scripts.utils.constants import RANDOM_SEED
from scripts.utils.data_sampling import generate_random_indices

def generate_random_name():
    first_names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Charles", "Thomas", "Julia", "Sophia", "Anne", "Louise", "Kristine", "Taylor"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Swift", "Hudson", "Alwin", "Haley", "Antonoff", "Carpenter"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def expand_abbreviation(street):
    street = street.replace("St", "Street")
    street = street.replace("Ave", "Avenue")
    street = street.replace("Blvd", "Boulevard")
    street = street.replace("Ln", "Lane")
    street = street.replace("Rd", "Road")
    street = street.replace("Dr", "Drive")
    street = street.replace("Pl", "Place")
    street = street.replace("Ct", "Court")
    return street

european_cities = ["Paris", "London", "Rome", "Berlin", "Madrid", "Amsterdam", "Vienna", "Barcelona", "Prague", "Budapest", "Bruxelles", "Lisbon", "Stockholm"]

def abbreviate_state(state):
    state_abbreviations = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY"
    }

    for full_name, abbreviation in state_abbreviations.items():
        state = state.replace(full_name, abbreviation)

    return state

# "different kinds" of missing values
missing_values_replacement_options = [np.nan, "", "-"]

def inject_missing_values(df, percentage):
    # total number of values
    total_elements = df.size

    # number of elements to replace
    num_to_replace = int(percentage * total_elements)

    # generate random positions in the dataframe
    indices = [(row, col) for row in range(df.shape[0]) for col in range(df.shape[1])]
    selected_indices = np.random.choice(len(indices), num_to_replace, replace=False)

    # replacing the real values with the missing values
    for idx in selected_indices:
        row, col = indices[idx]
        df.iat[row, col] = np.random.choice(missing_values_replacement_options)

def inject_non_exact_duplicates(df, percentage, help_dir):

    # number of rows to duplicate
    num_rows_to_duplicate = int(percentage * len(df))

    # randomly chooses the rows to duplicate
    rows_to_duplicate = df.sample(n=num_rows_to_duplicate, random_state=RANDOM_SEED)

    # list to save modified rows
    modified_rows = []

    # list to save the indices of the original and new rows
    duplicate_info = []

    # functions that modifies a row
    def modify_row(row_to_modify, original_row_index):

        # 50% chance
        if np.random.rand() < 0.5:
            # filters columns that have no missing values
            non_missing_columns = [col for col in row_to_modify.index if row_to_modify[col] not in missing_values_replacement_options]
            if non_missing_columns:
                col_to_modify = np.random.choice(non_missing_columns)
                # adds an extra missing value
                row_to_modify[col_to_modify] = np.random.choice(missing_values_replacement_options)

        # 50% chance
        else:
            # removes all non-number characters
            price_str = re.sub(r'\D', '', str(row_to_modify['price']))
            # modifies the price
            row_to_modify['price'] = (int(price_str) if price_str != "" else 0) + np.random.randint(5000, 50001)

        # Add the original index and new row to the duplicate info list
        duplicate_info.append((original_row_index, len(df) + len(modified_rows)))

        return row_to_modify

    # applies the modification to every duplicate row
    for original_index, row in rows_to_duplicate.iterrows():
        modified_rows.append(modify_row(row.copy(), original_index))

    # builds a new dataframe with the duplicated and modified rows
    duplicates_df = pd.DataFrame(modified_rows)

    # concatenates the starting dataframe with the duplicates
    new_df = pd.concat([df, duplicates_df], ignore_index=True)

    # Convert the duplicate info to a DataFrame
    duplicate_info_df = pd.DataFrame(duplicate_info, columns=['original_index', 'new_index'])

    # Save the duplicate information to a CSV file
    duplicate_info_path = os.path.join(help_dir, 'duplicate_rows_df_dirty_' + str(int(percentage * 100)) + '.csv')
    duplicate_info_df.to_csv(duplicate_info_path, index=False)

    return new_df

def make_dirty(df, percentage, help_dir):

    print("Injecting DQ issues with a pollution percentage of " + str(percentage * 100) + "%...")

    # change types
    df = df.astype('object')

    # replaces some ids with the agent names
    for idx in generate_random_indices(df, percentage):
        df.at[idx, 'brokered_by'] = generate_random_name()

    # replaces some status values with the initial letter
    for idx in generate_random_indices(df, percentage):
        original_status = df.at[idx, 'status']
        df.at[idx, 'status'] = original_status[0] if original_status else ""

    # replaces some numeric prices with strings with the dollar sign
    for idx in generate_random_indices(df, percentage):
        original_price = df.at[idx, 'price']
        df.at[idx, 'price'] = f"${original_price}"

    # replaces some numbers with 9999, which is way too high and unrealistic
    for idx in generate_random_indices(df, percentage):
        df.at[idx, 'bed'] = 9999

    # replaces some numbers with 0, which could be wrong depending on context
    for idx in generate_random_indices(df, percentage):
        df.at[idx, 'bath'] = 0

    # replaces some numbers with values that are out of the correct domain values
    for idx in generate_random_indices(df, percentage):
        df.at[idx, 'acre_lot'] = round(random.uniform(-2.00, -0.01), 2)

    # replaces some street abbreviations with the long version (e.g. blvd -> boulevard)
    for idx in generate_random_indices(df, percentage):
        original_street = df.at[idx, 'street']
        df.at[idx, 'street'] = expand_abbreviation(original_street)

    # replaces some american cities with random european ones
    for idx in generate_random_indices(df, percentage):
        df.at[idx, 'city'] = random.choice(european_cities)

    # replaces some state names with their official abbreviation
    for idx in generate_random_indices(df, percentage):
        original_state = df.at[idx, 'state']
        df.at[idx, 'state'] = abbreviate_state(original_state)

    # leaves only the first 2 digits of the zip code
    for idx in generate_random_indices(df, percentage):
        string_zip = str(df.at[idx, 'zip_code'])
        df.at[idx, 'zip_code'] = int(string_zip[:2])

    # changes the unit of measurement (from square feet to square miles)
    for idx in generate_random_indices(df, percentage):
        original_house_size = df.at[idx, 'house_size']
        modified_house_size = original_house_size / 27878400
        df.at[idx, 'house_size'] = modified_house_size

    # changes the date format
    for idx in generate_random_indices(df, percentage):
        original_date_str = df.at[idx, 'prev_sold_date']
        if original_date_str:
            # Convert the original date string to a datetime object
            original_date = datetime.strptime(original_date_str, '%Y-%m-%d')
            # Format the date as mm/dd/yy
            modified_date_str = original_date.strftime('%m/%d/%y')
            # Update the value in the DataFrame
            df.at[idx, 'prev_sold_date'] = modified_date_str

    print("Injecting missing values...")

    # injects missing values
    inject_missing_values(df, percentage)

    print("Injecting non exact duplicates...")

    # injects non-exact duplicates
    new_df = inject_non_exact_duplicates(df, percentage, help_dir)

    print("Done!")

    return new_df

def shuffle_dataset(df, percentage, help_dir):
    # adds a column that represent the original order
    df['original_index'] = df.index

    # shuffles the rows
    df_shuffled = df.sample(frac=1, random_state=RANDOM_SEED).reset_index(drop=True)

    # saves the original order
    original_order = df_shuffled[['original_index']]
    original_order_path = os.path.join(help_dir, 'original_order_df_dirty_' + str(int(percentage * 100)) + '.csv')
    original_order.to_csv(original_order_path, index=False)

    # removes the extra column
    df_shuffled = df_shuffled.drop(columns=['original_index'])

    return df_shuffled


def make_data_standardization_dirty(df, percentage):
    """
    Introduce modifiche sporche ai dati con una percentuale specificata.

    :param df: Il DataFrame da sporcare
    :param percentage: Percentuale di valori da modificare
    :return: Il DataFrame modificato
    """

    print("Injecting data standardization issues with a pollution percentage of " + str(percentage * 100) + "%...")

    df['price'] = df['price'].astype('object')
    df['bed'] = df['bed'].astype('object')
    df['bath'] = df['bath'].astype('object')
    df['house_size'] = df['house_size'].astype('object')

    # replaces some numeric prices with strings with the dollar sign
    for idx in generate_random_indices(df, percentage):
        original_price = df.at[idx, 'price']
        df.at[idx, 'price'] = f"${original_price}"

    # replaces some status values with the initial letter
    for idx in generate_random_indices(df, percentage):
        original_status = df.at[idx, 'status']
        df.at[idx, 'status'] = original_status[0] if original_status else ""

    replace_values(df, 'bed', percentage)
    replace_values(df, 'bath', percentage)

    # replaces some street abbreviations with the long version (e.g. blvd -> boulevard)
    for idx in generate_random_indices(df, percentage):
        original_street = df.at[idx, 'street']
        df.at[idx, 'street'] = expand_abbreviation(original_street)

    # replaces some state names with their official abbreviation
    for idx in generate_random_indices(df, percentage):
        original_state = df.at[idx, 'state']
        df.at[idx, 'state'] = abbreviate_state(original_state)

    # changes the unit of measurement (from square feet to square miles)
    for idx in generate_random_indices(df, percentage):
        original_house_size = df.at[idx, 'house_size']
        modified_house_size = original_house_size / 27878400
        df.at[idx, 'house_size'] = modified_house_size

    # changes the date format
    for idx in generate_random_indices(df, percentage):
        original_date_str = df.at[idx, 'prev_sold_date']
        if original_date_str:
            # Convert the original date string to a datetime object
            original_date = datetime.strptime(original_date_str, '%Y-%m-%d')
            # Format the date as mm/dd/yy
            modified_date_str = original_date.strftime('%m/%d/%y')
            # Update the value in the DataFrame
            df.at[idx, 'prev_sold_date'] = modified_date_str

    print("Done!")
    return df


def replace_values(df, column, percentage):
    print(
        f"Injecting alternated replacements in column '{column}' with a pollution percentage of {percentage * 100}%...")

    for idx in generate_random_indices(df, percentage):
        original_value = df.at[idx, column]

        if original_value == 1:
            df.at[idx, column] = "one"

        elif original_value == 2:
            df.at[idx, column] = "two"

        elif original_value == 3:
            df.at[idx, column] = "three"

        elif original_value == 4:
            df.at[idx, column] = "four"

        elif original_value == 5:
            df.at[idx, column] = "five"

        elif original_value == 6:
            df.at[idx, column] = "six"


def inject_duplicates(df, percentage):
    """
    Introduce duplicati e triplicati nel dataframe, aggiungendo una colonna `duplicate` per tracciare gli indici delle righe duplicate.

    :param df: Il DataFrame originale.
    :param percentage: Percentuale di righe da duplicare o triplicare.
    :return: Il DataFrame con i duplicati e triplicati aggiunti e la colonna `duplicate`.
    """

    print(f"Injecting duplicates with a percentage of {percentage * 100}%...")

    # Aggiungi la colonna 'duplicate' inizializzandola con -1
    df['duplicate'] = -1  # -1 significa che non ha duplicati

    # Numero totale di righe da duplicare
    num_rows_to_duplicate = int(percentage * len(df))

    # Calcola quante righe duplicare una sola volta e quante triplicare
    num_single_duplicates = int(num_rows_to_duplicate * 0.6)
    num_triple_duplicates = int(num_rows_to_duplicate * 0.2)

    # Seleziona casualmente le righe da duplicare e triplicare
    single_duplicate_rows = df.sample(n=num_single_duplicates, random_state=RANDOM_SEED).copy()
    remaining_rows = df.drop(single_duplicate_rows.index)
    triple_duplicate_rows = remaining_rows.sample(n=num_triple_duplicates, random_state=RANDOM_SEED + 1).copy()

    # Aggiungi le righe duplicate una sola volta
    for idx in single_duplicate_rows.index:
        # Copia la riga
        duplicate_row = df.loc[idx].copy()

        # Trova il nuovo indice per il duplicato
        new_idx = len(df)

        # Aggiorna la colonna 'duplicate' per l'originale e il duplicato
        df.at[idx, 'duplicate'] = new_idx
        duplicate_row['duplicate'] = idx

        # Aggiungi il duplicato al DataFrame
        df = pd.concat([df, duplicate_row.to_frame().T], ignore_index=True)

    # Aggiungi le righe triplicate
    for idx in triple_duplicate_rows.index:
        # Copia la riga due volte
        duplicate_row1 = df.loc[idx].copy()
        duplicate_row2 = df.loc[idx].copy()

        # Trova i nuovi indici per i duplicati
        new_idx1 = len(df)
        new_idx2 = new_idx1 + 1

        # Aggiorna la colonna 'duplicate' per l'originale e i duplicati
        df.at[idx, 'duplicate'] = f"{new_idx1},{new_idx2}"
        duplicate_row1['duplicate'] = f"{idx},{new_idx2}"
        duplicate_row2['duplicate'] = f"{idx},{new_idx1}"

        # Aggiungi i duplicati al DataFrame
        df = pd.concat([df, duplicate_row1.to_frame().T, duplicate_row2.to_frame().T], ignore_index=True)

    print(f"Added {num_rows_to_duplicate} duplicates (including single and triple duplicates).")
    return df