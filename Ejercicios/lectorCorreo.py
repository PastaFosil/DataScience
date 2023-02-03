import csv

f = open("//home//juancho//Documents//Personalizadas//DataScience//correos.txt", "r")

correos = f.read()
dominios = []
vocales = "aeiou"

newDoc = [["Usuario","No. de vocales"]]
for i in correos.split("\n"):
    
    if i != "":
        aux = i.split("@")
        newDoc.append(aux)
        
        aux = aux[1].split(".")
        if aux[0] not in dominios:
            dominios.append(aux[0])
        
        count = 0
        for i in vocales:
            count += newDoc[-1][0].count(i)
        newDoc[-1][1] = count

print(dominios)
print(newDoc)

with open("correosVocales.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(newDoc)

