import json
import time

def read_json_file(file_path):
    start_time = time.time()
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    end_time = time.time()
    return data, end_time - start_time

def write_json_file(file_path, data):
    start_time = time.time()
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    end_time = time.time()
    return end_time - start_time

def main():
    file_path = '/home/ludovica/hadoop-3.3.6/tweets/file.json'

    # Leggi il file JSON
    data, json_read_time = read_json_file(file_path)

    start_time = time.time()
    print("Risultati della query:")
    for row in data:
        print(row)
    query_execution_time = time.time() - start_time

    # Modifica i dati
    row_index_to_modify = 2  # Indice della riga da modificare
    if row_index_to_modify < len(data):
        data[row_index_to_modify] = {
            "col1": "Modificato 1",
            "col2": "Modificato 2",
            "col3": "Modificato 3",
            "col4": "Modificato 4",
            "col5": "Modificato 5",
            "col6": "Modificato 6",
            "col7": "Modificato 7",
            "col8": "Modificato 8"
        }

    # Scrivi i dati modificati nel file JSON
    update_time = write_json_file(file_path, data)

    # Stampa i tempi di esecuzione
    print("Tempo di lettura del file JSON:", json_read_time, "secondi")
    print("Tempo di esecuzione della query:", query_execution_time, "secondi")
    print("Tempo di modifica dei dati nel file JSON:", update_time, "secondi")

if __name__ == "__main__":
    main()

