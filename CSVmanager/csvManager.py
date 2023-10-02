import csv
from datetime import datetime

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
    
    def writeCSV(patternName, patternColor):
        with open(csv_datei, mode='a', newline='') as datawriter:
            writer=csv.writer(datawriter)

            timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data=(timestamp_str, patternName, patternColor)
            writer.writerow(data)
    