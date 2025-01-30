import csv
import io

def format_dataset_for_tablellama(dataset: str) -> str:
    # Usa un oggetto StringIO per trattare il dataset come file CSV
    f = io.StringIO(dataset)

    # Usa csv.Sniffer per rilevare automaticamente il delimitatore
    sample = f.read(1024)  # Legge un campione per l'analisi
    f.seek(0)  # Torna all'inizio del file dopo aver letto il campione
    dialect = csv.Sniffer().sniff(sample, delimiters=",;")  # Rileva "," o ";"

    reader = csv.reader(f, delimiter=dialect.delimiter)

    # Separatori letterali
    tab = "[TAB]"
    sep = "[SEP]"

    # Leggere tutte le righe dal CSV
    rows = list(reader)

    if not rows:
        raise ValueError("Dataset must not be empty.")

    # La prima riga è l'header, sostituisco il delimitatore con il pipe
    header = " | ".join(rows[0])

    # Le righe successive sono i dati, sostituendo il delimitatore con il pipe
    data_rows = [" | ".join(row) for row in rows[1:]]

    # Costruisco la stringa formattata
    formatted_rows = [header] + data_rows

    # Unisco le righe con [SEP] e aggiungo [TAB] all'inizio
    result = tab + " " + f" {sep} ".join(formatted_rows)

    return result