import json

print('Willkommen bei der Deutschen Bahn ! Sie haben folgende Tickets zur Auswahl:')

with open("tickets.json", "r") as file:
    ticket_dict = json.load(file)
for line_num, ticket in enumerate(ticket_dict["tickets"]):
    print(line_num, (ticket["name"]))
    
infos = int(input('Bitte wählen Sie eine Nummer für eine entsprechende Fahrkarte:'))

if infos < 0 or infos >= len(ticket_dict["tickets"]):
    print('Die Auswahl ist leider Ungültig !')
    exit()


user_ticket = ticket_dict["tickets"][infos]["name"]
user_price = ticket_dict["tickets"][infos]["price"]
user_cash = ticket_dict["accepted_cash"]


print(f'Sie haben die {user_ticket} gewählt. Der Preis beträgt {user_price} €')
print('Der Automat aktezpiert folgende Münzen und Geldscheine')
for entry in ticket_dict["accepted_cash"]:
    print(entry, "Euro")
print()
money = 0

while money < user_price :
    print('Bitte werfen Sie eine Münze oder einen Geldschein ein, es fehlen noch', user_price - money, '€')
    x = int(input())
      
      
   
    if x in user_cash:
      print('Danke für', x, '€')
      money += x
      
    else:
      print('Leider aktzeptieren wir diese Münze/diesen Geldschein nicht.Bitte werden sie etwas anderes ein')
      
   
print()

print('Danke für ihren Einkauf und noch eine angenehme Fahrt ! ihr Restgeld beträgt', money - user_price, '€')





    
    
    