import csv
import io


def format_dataset_for_tablellama(dataset: str) -> str:
    # Usa un oggetto StringIO per trattare il dataset come file CSV
    f = io.StringIO(dataset)
    reader = csv.reader(f)

    # Separatori letterali
    tab = "[TAB]"
    sep = "[SEP]"

    # Leggere tutte le righe dal CSV
    rows = list(reader)

    # La prima riga è l'header, sostituisco le virgole con i pipe
    header = " | ".join(rows[0])

    # Le righe successive sono i dati, sostituendo le virgole con i pipe
    data_rows = [" | ".join(row) for row in rows[1:]]

    # Costruisco la stringa formattata
    formatted_rows = [header] + data_rows

    # Unisco le righe con [SEP] e aggiungo [TAB] all'inizio
    result = tab + " " + f" {sep} ".join(formatted_rows)

    return result