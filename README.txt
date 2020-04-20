--------------------------------------- README ----------------------------------------

---------------------------------------Allgemein---------------------------------------

Diese Anwendung wurde entwickelt um vorausschauend Logistik speziell für die 
Pumpenproduktion vereinfachend zu planen. Sie ist in der Lage Daten aus jeder Pumpe, 
die in Form einer csv-Datei in den Ordner „Datafolder“ gespeichert wird, herauszuholen 
und planend, diese in einen Produktionszyklus zu integrieren, um so den 
Materialverbrauch der zu produzierenden Pumpe/(n) zu simulieren.

---------------------------------------Funktionen--------------------------------------

1. Mainlayout & Pumpen einfügen

Die obere blaue Menü-Leiste dient der Bedienung weiterer Funktionen die später
beschrieben sind.
Das Feld Sollzahl ist für die gewünscht Eingabe der Produktionszahl der gewünschten
Pumpe. Das Feld Pumpensuche ist für die Vereinfachung der Suche nach einer bestimmten
Pumpe. Gibt man dort die Pumpennummer ein, wird sich die Liste der Pumpen 
aktualisieren, und die gewünschte Pumpe anzeigen.
Die Liste unter dem Logo enthält alle verfügbaren csv-Dateien, die im "Datafolder"
gespeichert sind. Möchte man eine weitere Pumpe zu dieser "Datenbank" hinzufügen, 
sollte man aus dem SAP, die fehlende Pumpe als ".csv"-Datei speichern und diese in den 
Ordner "Datafolder" einfügen (einfach Programm-Ordner öffnen und "Datafolder" suchen).

2. Pumpen auswählen

Möchte man eine Pumpe auswählen, klickt man einfach auf die gewünschte Pumpe und 
gibt die gewünschte Sollzahl ein. WICHTIG: Die Pumpen sollten so ausgewählt werden, 
wie auch ihre Reihenfolge, um die spätere Simulation des Materialverbrauchs zu 
ermöglichen. 
Man kann maximal bis zu 10 Pumpen auswählen.

3. Simulation

Ist man nun mit der Auswahl der Pumpen fertig, klickt man auf "Simulieren" oben auf der 
Menüleiste. Nun öffnet sich ein neues Fenster. Dieses enthält eine weitere Menüleiste 
und eine Liste. Hier beschrieben sind die gewählten Pumpen mit ihrer Produktionszahl, 
Name und Produktionszeit. Wählt man eine Pumpe aus und drückt auf öffnen, 
so öffnet sich die die "Excel" der jeweiligen Pumpe. Ebenfalls zu finden sind 
Felder die mit Takt und Regelkreiszeit beschrieben sind, diese sind zum Einstellen 
der genannten Parameter da, möchte man diese einstellen, so gibt man das gewünschte 
Parameter ein und drückt auf "OK". Dabei zu Beachten ist, dass die Zeit in Sekunden 
verlangt werden.
Sind die Parameter eingestellt, kann man verschiedene Graphen("Simulationen") abspielen. 
Einmal den Materialverbrauch pro Pumpe(Material/Pumpe), die Gesamtanzahl an benötigten 
Materialien für diesen Produktionsvorgang und den Materialverbrauch pro 
Regelkreis(Material/RK). Die Simulation der Regelkreise erfolgt nach Reihenfolge 
der Auswahl der Pumpen, weshalb es wichtig ist, die Reihenfolge der Produktion 
bei der Auswahl zu beachten.

4. Funktion "Clear Temp"

Alle Daten die aus den ".csv" Dateien gesammelt werden, werden in "Temporary-files" 
gespeichert.
Das heißt, nach jeder Suche, sind die Daten gespeichert und wieder verwendbar. 
Es sind aber auch, nur bis zu 10 Pumpen maximal möglich zu speichern und ebenfalls 
kann es passieren, dass man einen Fehler bei der Auswahl macht. 
In diesem Fall kann man die Funktion im Hauptmenü "Clear Temp" verwenden. 
Dann werden alle gespeicherten Daten gelöscht. Falls man einen Fehler bei der Auswahl 
macht, sollte man deshalb die Auswahl von vorne, ab der 1. Pumpe beginnen.

----------------------------------------Scriptsprache----------------------------------

Die verwendete Scriptsprache war Python(3.7).

-----------------------------------------Ersteller-------------------------------------

Ersteller dieses Programms ist Isaac L.L. Yuki - Student der Elektrotechnik bei 
Pierburg Pump Technology. Bei Erklärungsnot im Falle einer Umschreibung des Programms, 
falls die Scripts in Python benötigt werden oder sonstiges bitte isaacyuki@hotmail.com 
kontaktieren oder auch per interne Email.






