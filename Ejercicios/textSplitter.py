import csv

def splitAndCount(string, idx=0):
    characters = ["\n", " ", ""]
    data = []
    i = 1
    if idx<2:
        string = string.split(characters[idx])
        string = list(filter(lambda n: n!="", string))
        string = list(filter(lambda n: n!=" ", string))

    print(string)
    data.extend([len(string)])
    if idx>0:
        data.extend([len(set(string))])
    idx += 1
    if idx<3:
        string =  characters[idx].join(string)
        data.extend(splitAndCount(string, idx))
    return data

    
    splitStr = string.split

f = open("//home//juancho//Documents//Personalizadas//DataScience//Ejercicios//ciencia_de_datos_wikipedia.txt", "r")

texto = f.read()

textData = splitAndCount(texto)

print("Parrafos: ", textData[0])
print("Palabras totales: ", textData[1])
print("Palabras diferentes: ", textData[2])
print("Caracteres totales: ", textData[3])
print("Caracteres diferentes: ", textData[4])