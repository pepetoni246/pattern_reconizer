# Dokumentation

## Software Architecture

```mermaid
flowchart LR
    A("`Camera`") --> |read data| B("`patter recognizer
    (tool from Klims)`") --> C("`csv writer`") --> |write data| D("`csv file
    (database)`")
    E("`JPEG 
    test image`")
    E --> |read data| B
```
## Layered Pattern

```mermaid
flowchart TB
    subgraph Presentation Layer
    A("Image")
    end
    subgraph Buisness Layer
    B("image processor")
    C("csv Manager")
    end
    subgraph Persistence Layer
    D("csv data")
    end
    A -->B
    B -->C
    C -->D
```
## Klassen
### CSVmanager
#### Init
Erstellt eine CSV Datei "patternData.csv" mit den Spalten timestamp, Pattern name, color. 
#### writeCSV
Die Funktion writeCSV öffnet die zuvor erstellte csv Datei und schreibt die Daten des self.image.processor in diese Datei. Dazu schreibt er zuerst den timestamp dann den patternName und anschliessend die patternColor, jeweils mit Komma separiert, rein.











