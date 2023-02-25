# (Aufgabe 1)

# automatische Vervollständigung von Texteingabefeldern, Rangfolge der Suchrelevanz, Apps für unterstützendes Schreiben, Wortspiele und mehr.
# https://api.datamuse.com/ ist die Base URL.
# /words (Dieser Endpunkt gibt eine Liste von Wörtern (und Mehrwortausdrücken) aus einem bestimmten Vokabular zurück)
# /sug (Diese Ressource ist als Backend für „Autocomplete“-Widgets auf Websites und Apps nützlich, wenn das Vokabular möglicher Suchbegriffe sehr groß ist.
# Es bietet Wortvorschläge für eine teilweise eingegebene Abfrage unter Verwendung einer Kombination der in der Ressource „/words“ oben beschriebenen Operationen.

# (Aufgabe 2)

# Finde nun die top 5 Wörter, die eine ähnliche Bedeutung haben wie "on top of".
# Printe eine Liste mit synonymen Wörtern und Scores.
import requests
url = f"https://api.datamuse.com/words?ml=on+top+of&max=5"
r = requests.get(url)
resu = r.json()
words = [(res["word"],res["score"]) for res in resu]

print(words)

   

# (Aufgabe 3)

# Erstelle eine Funktion synonym_words, die die Parameter word und num_results entgegennimmt.
# Die Funktion benutzt die Datamuse API, um synonyme Wörter zu word zu sammeln.
# Die Funktion gibt eine Liste der Länge num_results zurück, die Tupel mit dem Format (synonymes Wort, Score) enthält.
# Teste die Funktion erneut mit dem Wort "on top of" und vergleiche das Ergebnis mit Aufgabe 2.
    
def synonym_words(word,num_results):

    url = f"https://api.datamuse.com/words?ml={word}&max={num_results}" 
    r = requests.get(url)
    resu = r.json()
    words = [(res["word"],res["score"]) for res in resu]

    return(words)

print(synonym_words("on top of", 5))

# (Aufgabe 4)

# Erstelle eine Funktion rhyme_words, die die Parameter word und num_results entgegennimmt.
# Die Funktion benutzt die Datamuse API, um reimbare Wörter zu word zu sammeln.
# Die Funktion gibt eine Liste der Länge num_results zurück, die Tupel mit dem Format (reimbares Wort, Score) enthält.
# Teste die Funktion mit dem Wort "grape". Was sind die Top 5 Wörter, die sich auf "grape" reimen?

def rhyme_words(word,num_results):
    
    url = f"https://api.datamuse.com/words?rel_rhy=grape&max=" + str(num_results)
    r = requests.get(url)
    resu = r.json()
    words = [(res["word"],res["score"]) for res in resu]
    
    return(words)
    
print(rhyme_words("grape", 5))



# (Aufgabe 5)

# Antonyme sind in der Sprachwissenschaft mit gegensätzlicher Bedeutung, z.b. früh --> spät.
# Erstelle eine Funktion antonym_words, die die Parameter word und num_results entgegennimmt.
# Die Funktion benutzt die Datamuse API, um Antonyme zu word zu sammeln.
# Die Funktion gibt eine Liste der Länge num_results zurück, die nur die Antonyme enthält.
# Teste die Funktion mit dem Wort "bright"

def antonym_words(word,num_results):
    url = f"https://api.datamuse.com/words?rel_ant=bright&max=" + str(num_results)
    r = requests.get(url)
    resu = r.json()
    words = [(res["word"]) for res in resu]
    
    return(words)
    
print(antonym_words("bright", 4))
    
# (Aufgabe 6)

# Erstelle ein neues Modul (also eine neue Datei) mit dem Namen word_module.py.
# Kopiere alle bisher erstellten Funktionen (synonyme_words, rhyme_words und antonym_words) in diese Datei.
# Erstelle in diesem Modul einen if __name__ == "__main__" block und teste deine Funktionen similar_words, rhyme_words und antonym_words in word_module.py.
# Schaue dir hierfür zunächst die offizielle Python Dokumentation an: https://docs.python.org/3/library/__main__.html
# Zusätzliche Hilfestellung findest du in diesem Beispiel: https://www.learnpython.dev/02-introduction-to-python/190-apis/final-exercise/
# Importiere mit der import Funktion dann alle Funktionen aus dem word_module Modul in dein ursprüngliches Pythonskript (z.B. data_muse.py) 
# und teste auch hier nochmal die Funktionen similar_words, rhyme_words und antonym_words (aber dieses mal eben jene aus dem Modul word_module.py).

# Wird der Code aus dem if __name__ == "__main__" Block in data_muse.py auch ausgeführt?
# Wofür kannst du den if __name__ == "__main__" Block benutzen?

from word_module import *

print(synonym_words("on top of", 5))
print(rhyme_words("grape", 5))
print(antonym_words("bright", 4))


