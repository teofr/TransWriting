from googletrans import Translator
import json
from pprint import pprint
import networkx as nx

def rewrite(lista):
    t = Translator()
    actual = 'en'
    prox = 'es'
    while True:
        trad = t.translate(lista[-1], src = actual, dest = prox).text
        if trad in lista:
            break
        lista.append(trad)
        temp = actual
        actual = prox
        prox = temp
    res = ""
    for t in lista:
        res += " -> {}".format(t)
    print (res)
    return lista

#inicial = str(input())

#print (rewrite([inicial]))

with open('words_dictionary.json') as data_file:
    data = json.load(data_file)

for k in data.keys():
    rewrite([k])
    #data[k] = t.translate(k, src='en', dest='es').text
    #print ("{} -> {}".format(k, data[k]))
