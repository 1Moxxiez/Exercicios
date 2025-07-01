''''''

def achata(l1):
    
    return [item for sublista in l1  for item in sublista ]

print(achata([[1, 2], [3, 4]]))
