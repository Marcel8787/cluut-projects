# (Aufgabe 4)

import pandas as pd

file_products = pd.read_csv("products.csv", sep = ";")
data = ["Name", "Prod_id", "Category", "PRICE"]
file_products = file_products[[*data]]
products = list(file_products.to_records(index = False))


file_employees = pd.read_csv("employees.csv", sep = ";")
order = ["Name", "Age", "Pers_id", "JOB_ID"]
file_employees = file_employees[[*order]]
employees = list(file_employees.to_records(index = False))



# (Aufgabe 5)


# Erstelle einen Supermarkt my_supermarket mit den Werten "Supermarkt Deluxe", "Marienplatz 1", "München".


# Nimm deine employees und products und erstelle aus jedem Tupel ein Objekt.
# Für Elemente der employees Liste erstellst du Employee-Objekte und speicherst diese dann gesammelt in deinem Supermarkt.
# Für Elemente der products Liste erstellst du Products-Objekte und speichers diese dann gesammelt in deinem Supermarkt.


# Dein Supermarkt soll am Schluss alle Attribute gesetzt haben - keine leeren Listen mehr!



from supermarket import Supermarket, Employee, Product

my_supermarket = Supermarket( "Supermarkt Deluxe", "Marienplatz 1", "München")
my_supermarket.employees = [Employee(*elem) for elem in employees]
my_supermarket.products = [Product(*elem) for elem in products]


# (Aufgabe 6)

# Verschaffe dir einen Überblick über deinen Supermarkt und beantworte die folgenden Fragen.
# P.S.: Wir lieben aussagekräftige Antwortsätze - f-String!! ;)
# Überlege dir für welche der Anfragen es ggf. Sinn macht in Zukunft eine neue Methode in einer der Klassen zu implementieren.


# Wie viele Mitarbeiter hast du aktuell?
# Was ist das teuerste Produkt in deinem Supermarkt?
# Wie viel kostet ein Produkt im Durchschnitt in deinem Supermarkt?
# Wie viele Produkte hast du für jede Kategorie?
# Wie heißt der älteste Mitarbeiter?


print(f"der Supermarkt hat aktuell {len(my_supermarket.employees)} Mitarbeiter ")

# Preis an Stelle 3
# Name in Tupel steht an Stelle 0
# Preis mit Name verglichen 

max_product = max(products,key=lambda x:x[3])[0]
print(f"das teuerste Produt in meinem Supermarkt ist {max_product} ")

mean_prod = (sum(map(lambda x: x[3], products)) / len(products))
print(f"ein Produkt kostet im Durschnitt {mean_prod:.2f} € ")

from collections import Counter

number = Counter(product.category for product in my_supermarket.products)
print(f"in meinem Supermarkt sind meine Produkte so verteilt : {number} ")

name = max(employees,key=lambda x:x[1])[0]
print(f"der älteste Mitarbeiter heißt {name}")







 