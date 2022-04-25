import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode = "r") as csv_file:
        reader = csv.DictReader(csv_file) #funkce vytvari slovniky, z kazdeho radku vyrobi slovnik, klicem je nazev sloupce  ahodnotou polozka v danem sloupci a radku
        for row in reader:
            print(row)
# ted jsme vytvorili nekolik slovniku a ted je spojime do jednoto slovniku velkeho
    with open(file_path, mode = "r") as csv_file:
        reader = csv.DictReader(csv_file)
        big_dictionary = {}
        for row in reader:
            for key, value in row.items():
                if key not in big_dictionary.keys():
                    big_dictionary[key] = [int(value)] #musime to dat do slovniku, protoze pak chceme appendovat
                else:
                    big_dictionary[key].append(int(value))
        return big_dictionary
        #ziskali jsme jeden slovnik, kde klice jsou nazvy sloupcu a hodnoty seznam cisel






def main():
    print(read_data("numbers.csv"))


if __name__ == '__main__':
    main()
