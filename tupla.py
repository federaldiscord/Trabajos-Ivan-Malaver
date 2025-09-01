tupla = (7,4,2,9,14,200)
tupla2 = "Juan", "Camilo", "Ana", "Laura", "Pedro", "Sofia", "Luis"
tupla3 = tuple([1,2,3,4,5])
print(tupla3)
print(tupla2)
print(tupla2[0])
print(tupla[4])
nuevalista = tuple(tupla)
print(nuevalista)

nTupla = tupla.__add__((10,20,30,40,50))

print(nTupla)
nnTupla = sorted(nTupla)
print(nnTupla)
print(tupla2[-2])


temp_list = list(tupla2)
temp_list[1] = "Carlos"
nnnTupla = tuple(temp_list)
print(nnnTupla)