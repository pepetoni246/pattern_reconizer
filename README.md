# Dokumentation

## Einleitung und Ziele
Die Software dient dazu in Echtzeit Muster in einem Lifestream zu erkennen. Dazu sollen verschiedene Formen und die dazugehörige Farbe erkannt und in eine csv Datei abgelegt werden. Die Mustererkennung soll im Lifestream zu sehen sein. 
- Formen: Quadrat, Rechteck, Dreieck, Kreis
- Farben: Rot, Grün, Blau, Gelb, Violett
- Input: Kamera z.B Webcam des Laptops
- Output: csv.Datei mit Zeit, Form, Farbe
## Lösungen und Strategie
Die Software wird aus verschiedenen Funktionen zusammengesetzt. So bleibt sie Modular und kann nach Wunsch erweitert werden.

## Software-Architektur

```mermaid
flowchart LR
    A("`Camera`") --> |read data| B("`patter recognizer
    (tool from Klims)`") --> F("`show layered image`") --> C("`csv writer`") --> |write data| D("`csv file: PatternData.csv`")
    E("`JPEG 
    test image`")
    E --> |read data| B
```
## Komponentendiagramm

```mermaid
flowchart TD
    subgraph Presentation_Layer
    A("Image")
    end

    subgraph Buisness_Layer
    B("image processor")
    C("csv Manager")
    end

    subgraph Persistence_Layer

    D("csv data")
    end
    A -->Buisness_Layer
    A <.-B
    B -->C
    C -->Persistence_Layer
```
## Funktionen und Klassen
### CSVmanager
#### Init
Erstellt eine CSV Datei "patternData.csv" mit den Spalten timestamp, Pattern name, color. 
#### writeCSV
Die Funktion writeCSV öffnet die zuvor erstellte csv Datei und schreibt die Daten des self.image.processor in diese Datei. Dazu schreibt er zuerst den timestamp dann den patternName und anschliessend die patternColor, jeweils mit Komma separiert, rein.
### CameraReader
#### Init
Stellt die Verbidnung zu der Webcam des Laptops her. Falls die Kamera nicht geöffnet werden konnte, wird eine Entsprechende Fehlermeldung angezeigt.
#### getImage
Die Kamera ausgelesen und in einem seperaten Fenster geöffnet. Die Mustererkennung wird auf dem laufenden Kamerafeed angezeigt.

### Image Processor (Klassen von Klims)
- Pattern
- Detector(ABC)
- ImageProcessor
- ColorDetector(Detector)
- PatternDetector(Detector)

Diese Klassen haben wir auf Grund fehlender Bildverarbeitungskenntnissen von Klims erhalten.

## get it started











