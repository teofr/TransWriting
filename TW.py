from googletrans import Translator
import json
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

def rewrite(lista, G, idiomas=['en', 'es']):
    idx = 0
    t = Translator()

    while True:
        next_idx = (idx + 1) % len(idiomas)

        actual = idiomas[idx]
        prox = idiomas[next_idx]
        trad = t.translate(lista[-1], src = actual, dest = prox).text.lower()
        if trad in lista:
            G.add_edge(lista[-1], trad)
            break
        G.add_edge(lista[-1], trad)
        lista.append(trad)
        idx = next_idx

    res = ""
    for t in lista:
        res += " -> {}".format(t)
    #print (res)
    return G


def drawConnected(G, save=False, file="temp.png"):
    largest_cc = nx.DiGraph()
    value = (0, 0)
    for candidate in nx.weakly_connected_component_subgraphs(G, copy=True):
        temp = 1
        for node in candidate.nodes():
            if candidate.in_degree(node) > 0 :
                temp = temp*candidate.in_degree(node)
        if (temp, len(candidate)) > value:
            value = (temp, len(candidate))
            largest_cc = candidate

    plt.clf()
    fig = plt.figure(figsize=(15,15))
    nx.draw_kamada_kawai(largest_cc, with_labels=True, node_size=0, edge_color='#efefef')
    if save:
        fig.savefig(file)
    else:
        fig.show()
    plt.close(fig)

H = nx.DiGraph()

with open('words_dictionary.json') as data_file:
    data = json.load(data_file)

cnt = 0
for k in data.keys():
    print ("cnt: {}             ".format(cnt), end='\r')
    cnt +=1
    H = rewrite([k], H, ['en', 'es'])
    drawConnected(H, save=True)
