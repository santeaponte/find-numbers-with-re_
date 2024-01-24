
fname = input('Enter the file name: ')
try:
    fh = open(fname, 'r')
except:
    print('file cannot be opened: ', fname)
    quit()
    
lista1 = list()
sumador = 0
for i in fh:
    i = i.strip()
    i = i.split()
    for a in i:
      lista1.append(a)

suma = 0
lista2 = list()
for num in lista1:
  try:
    prom = float(num)
    lista2.append(prom)
    #print(lista2)
    suma += prom
  except:
    continue
print(len(lista2))
print(suma)



''' 
try:
    prom = float(token)
    #print(prom)
    sumador += prom
except:
    continue
            
'''