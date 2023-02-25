marios = {
    "name" : "marios",
    "age" : 1999, 
    "payment_options" : ["card", "cash", "online"],  
    "available_rooms" : [800, 801, 802, 805, 900, 1000, 1001], 
    "price_per_night" : 50,
    "employees" : ["carlo", "maria", "marta", "luis", "fernando"], 
    
}  

hilten = {
    "name" : "hilten",
    "age" : 1992,
    "payment_options" : ["card", "online"],
    "available_rooms" : [100, 800, 801, 805, 1000, 1001],
    "price_per_night" : 70,
    "employees" : ["artur", "maria", "oliver", "xenia"]
    
 }
 
 # 2 Hotels als dictionarys erstellt
 
nights = 5 
cost_marios = nights * marios["price_per_night"]
cost_hilten = nights * hilten["price_per_night"]

print(cost_marios,cost_hilten) 

# die Kosten für 5 Übernachtungen einzel berechnet

all_hotels = cost_marios, cost_hilten 

smallest_price = min(all_hotels)
print(smallest_price)

# ausgerechnet welches Hotel günstiger ist

difference = cost_hilten - cost_marios 
print(difference)

# Preisunterschied ausgerechnet

print(f'Fünf Übernachtungen kosten {cost_marios} € im Hotel Marios und {cost_hilten}€ im Hotel Hilten. Der Preisunterschied sind {difference} € ')

room_numbers = set(marios["available_rooms"]).intersection(set(hilten["available_rooms"]))
list_numbers = list(room_numbers)

# überprüfen, welche Zimmernummern in beiden Hotels verfügbar sind


print(f'Guten Tag, könnten Sie mir bitte eines der folgenden Zimmer reservieren: {list_numbers} ? Danke')

payment_marios = len(marios["payment_options"])   
payment_hilten = len(hilten["payment_options"]) 

# Anzahl an Zahlungsmöglichkeiten ausgegeben

print(f'Im Hotel Marios gibt es {payment_marios} und im Hotel Hilten {payment_hilten} Zahlungsmöglihckeiten')

list_1 = (marios["payment_options"])
list_2 = (hilten["payment_options"])

differences = set(list_1).symmetric_difference(set(list_2)) 
sym_differences = list(differences) 

print(f'Die Hotels unterscheiden sich in den folgenden Zahlungsmöglichkeiten: {sym_differences} ')  

# Unterschiede an Zahlungsmöglichkeiten zwischen den Hotels
# welche Zahlungsmöglichkeiten nicht 
 
list1 = marios["employees"]
list2 = hilten["employees"]


if "fernando" in list1:
     print(f'fernando arbeitet im hotel marios und dort werde ich übernachten')
     
# mit einer if Schleife überprüft in welchem Hotel fernando arbeitet 
     



















  
 
 