import csv
import time

def read_csv_file(file_path):
    start_time = time.time()
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    end_time = time.time()
    return data, end_time - start_time

def write_csv_file(file_path, data):
    start_time = time.time()
    with open(file_path, 'w', newline='') as csvfile:  # Apriamo il file in modalità di scrittura ('w')
        writer = csv.writer(csvfile)
        writer.writerows(data)
    end_time = time.time()
    return end_time - start_time

def main():
    file_path = '/home/ludovica/hadoop-3.3.6/tweets/file.csv'

    # Leggi il file CSV
    data, csv_read_time = read_csv_file(file_path)

    start_time = time.time()
    print("Risultati della query:")
    for row in data:
        print(row)
    query_execution_time = time.time() - start_time

    # Modifica una riga esistente nel file CSV
    row_index_to_modify = 2  # Indice della riga da modificare
    if row_index_to_modify < len(data):
        data[row_index_to_modify] = ['Modificato 1', 'Modificato 2', 'Modificato 3', 'Modificato 4', 'Modificato 5', 'Modificato 6', 'Modificato 7', 'Modificato 8']

    # Scrivi i dati modificati nel file CSV
    update_time = write_csv_file(file_path, data)

    # Stampa i tempi di esecuzione
    print("Tempo di lettura del file CSV:", csv_read_time, "secondi")
    print("Tempo di esecuzione della query:", query_execution_time, "secondi")
    print("Tempo di modifica della riga nel file CSV:", update_time, "secondi")

if __name__ == "__main__":
    main()

