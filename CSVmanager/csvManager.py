import csv

# path and name
csv_datei='CSVmanager\patternData.csv'
# initial data
initData = ["timestamp" , "Pattern name", "Color"]

class CSVmanager:
    def __init__(self):
        print("CSVmanager initialisiert")

        with open(csv_datei, mode='w', newline='') as file:
            schreiber=csv.writer(file)
            # write init data in file
            schreiber.writerow(initData)
    
    def writeCSV(data):
        with open(csv_datei, mode='a', newline='') as datawriter:
            writer=csv.writer(datawriter)
            writer.writerow(data)