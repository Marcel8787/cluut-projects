# (Aufgabe 0)

# Was ist ein Apache HTTP Server?
# Welches Format haben Apache Access Logs?
# Welche Informationen sind in einer Access Log Zeile enthalten?

# Beim Apache-Webserver handelt es sich um eine plattformübergreifende Software, die sowohl auf Unix/Linux wie auch auf Windows Servern ausgeführt werden kann. 
# Seine Aufgabe ist es, eine Verbindung zwischen einem physischen Server mit den gespeicherten Webseiten und den Browsern der Internetuser herzustellen

# Apache verwendet standardmäßig das Common Log Format (CLF), aber Sie können Ihre eigene Formatzeichenfolge angeben, 
# um die in jedem Protokoll enthaltenen Felder zu ändern. Sie können auch die Direktive CustomLog verwenden, um den Speicherort der Protokolldatei zu ändern.

# Die Apache-Zugriffsprotokolle sind Textdateien, die Informationen über alle vom Apache-Server verarbeiteten Anfragen enthalten. Sie können erwarten, 
# dass Sie Informationen wie den Zeitpunkt der Anfrage, die angeforderte Ressource, den Antwortcode, die Zeit, die zum Antworten benötigt wurde, und die zum Anfordern der Daten verwendete IP-Adresse finden

# (Aufgabe 1)

# Lade die zip-Datei herunter und speichere alle enthaltenen Files in einem Cloud9 Folder für dieses Projekt.
# Öffne die Datei apache_logs in einem Python Skript namens log_analysis.py und lese alle Zeilen in eine Liste ein.
# Schau dir die erste Zeile der Datei an und schreibe in einem Kommentar auf, welche Informationen wir in jeder Log Zeile haben.

with open("apache_logs", "r") as file:
    logs = file.readlines()
    # print(logs[0])
    

# (Aufgabe 2)

# Speichere die erste Zeile des Log Files in eine separate Variable first_line.
# Splitte die Zeile in ihre Einzelteile mit dem split()-Befehl.
# Extrahiere nun den HTTP Status Code.
# Welcher Status Code wurde für diese Anfrage an den HTTP Server zurückgegeben?
# Was bedeutet der HTTP Status Code?

first_line = logs[0].split()
code = first_line[8]
print(code)


# (Aufgabe 3)

# Analysiere nun alle Log Zeilen und speichere alle HTTP Status Codes in einer Liste mit dem Namen status_codes.
# Zähle, wie oft der Status Code 200 vorkommt und speichere den Wert in status_200.
# Zähle, wie oft der Status Code 404 vorkommt und speichere den Wert in status_404.
# Importiere nun die Klasse Counter aus dem Modul collections.
# https://docs.python.org/3/library/collections.html#collections.Counter
# Benutze die Counter Klasse, um für jeden Status Code in status_codes die Anzahl an Vorkommen zu bestimmen.
# Welche sind die 3 häufigsten HTTP Status Codes?
from collections import Counter

status_codes = [line.split()[8] for line in logs]
# print(status_codes)

status_200 = status_codes.count("200")
print(status_200)

status_404 = status_codes.count("404")
print(status_404)

counter = Counter(status_codes)
print(counter)

print(counter.most_common(3))

# (Aufgabe 4)

# Um deine Webapplikation für Benutzer zu verbessern, musst du herausfinden, welche Anfragen nicht funktioniert haben.
# Filtere deshalb die Log Zeilen nach dem Status Code 404 und speichere alle Zeilen, die diesen Status Code beibehalten, in der Liste lines_with_404.
# Benutze für das filtern die filter()-Funktion und lambda.
# Speichere in einer neuen Liste namens resource_list die angefragten URL Paths (resource requested).
# Benutze hier wieder die split()-Methode.
# Tip: https://www.sumologic.com/blog/apache-access-log/
# Wieviele verschiedene Fehlerquellen hast du gefunden?
# Welche sind die 3 häufigsten Fehlerquellen bei den Anfragen auf unseren Apache Server?
# Tip: https://docs.python.org/3/library/collections.html#collections.Counter

lines_with_404 = list(filter(lambda x: x.split()[8] == "404", logs))
resource_list = [line.split()[6]for line in lines_with_404]
print(len(set(resource_list)))
print(Counter(resource_list).most_common(3))






# (Aufgabe Bonus)

# Ziel der Aufgabe ist es einen Log Report zu erstellen, der zwei Abbildungen beinhaltet.
# Installiere hierfür das Python Modul fpdf mit pip: https://pypi.org/project/fpdf/
# Das Skript log_pdf.py aus dem LMS beinhaltet eine Klasse PDF, mit der du deinen Log Report erstellen kannst.
# Importiere die Klasse PDF aus dem Modul log_pdf in dein Skript.
# Erstelle ein Histogram mit seaborn für deine Liste status_codes und speichere den Plot in der Datei status_codes.png.
# Erstelle ein Histogram mit seaborn für deine Liste resource_list und speichere den Plot in der Datei resource_list.png.
# Erstelle eine Liste plots, die zwei Strings enthält: status_codes.png, resource_list.png
# Erstelle eine Instanz der Klasse PDF mit dem Namen log_report.
# Erstelle nun eine for-Schleife über die Elemente plot in deiner Liste plots und rufe in der for-Schleife den folgenden Befehl auf:
#      log_report.print_page(plot)
# Um den PDF Report nun zu erstellen, füge die folgende Zeile in deinen Code: 
#      log_report.output("LogReport.pdf", "F") 
# Schaue dir den PDF Report an. Was könnte noch verbessert werden?

from log_pdf import PDF
import seaborn as sns

sns.set_theme()
sns.set_context("paper", rc ={"font.size": 5, "axes.titlesize": 10})
status = sns.histplot(status_codes)
status.set_title("Das sind die Status Codes")
status.set_xlabel("HTTP Status")
status.set_ylabel("Anzahl")
status.get_figure().savefig("status_codes.png", bbox_inches ="tight")
status.figure.clf()


status_resource = sns.histplot(y = resource_list)
status_resource.set_title("Das sind die angefragten resourcen des HTTP Server")
status_resource.set_xlabel("Anzahl")
status_resource.set_ylabel("Resource Namen")

status_resource.get_figure().set_figwidth(8)
status_resource.get_figure().set_figheight(11)
status_resource.get_figure().savefig("resource_list.png", bbox_inches ="tight")
status_resource.figure.clf()

plots = ["status_codes.png", "resource_list.png"]
log_report = PDF()

for plot in plots:
    log_report.print_page(plot)
    
log_report.output("LogReport.pdf", "F")











