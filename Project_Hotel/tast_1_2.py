list1 = [10,21,45,66,78]
list2 = [10,22,46,66,78,90]

differences = set(list1).symmetric_difference(set(list2))  
sym_differences = list(differences)

sym_differences.sort()

print(sym_differences)

# unterschied der beiden listen festgestellt
# durch set.symetric_difference(s)
# mit set() die listen in mengen umgewandelt
# mit list() symetrische differenz in eine liste umgewandelt
# liste zum schluss mit sort() sortiert 

values = set(list1).intersection(set(list2))
common_values = list(values)

common_values.sort()
print(common_values) 

# gemeinsamkeiten der beiden listen festgestellt
# durch set.intersection
# mit set wieder die listen in mengen umgewandelt

