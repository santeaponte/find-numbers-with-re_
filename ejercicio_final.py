import re as re

fname = input('Enter the file name: ')
try:
    fh = open(fname, 'r')
except:
    print('file cannot be opened: ', fname)
    quit()

lista1 = list()
for letras in fh:
    nums = re.findall(r'[0-9]+', letras)
    for num in nums:
        lista1.append(num)
        
suma = 0
conv = 0
for i in lista1:
    try:
        conv = float(i)
    except:
        continue
    suma += conv
print(int(suma))
        
