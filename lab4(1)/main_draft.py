import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_adjlist('t.txt')

pos = {str(i): (i, 3) for i in range(4)}
pos.update({str(i): (i-4, 2) for i in range(4, 8)})
pos.update({str(i): (i-8, 1) for i in range(8, 12)})
pos['6'] = (3, 2)
pos['7'] = (4, 2)
pos['3'] = (5, 3)
pos['11'] = (5, 1)

nx.draw(g, pos=pos, with_labels=True, font_color='white', node_color='black')
plt.savefig('main.png', format="png")
plt.show()

tr = nx.Graph()
cnt = 0

for i in nx.connected_components(g):
    print(i)
    cnt += 1
    print(f'For connected component №{cnt}:')
    g1 = nx.subgraph(g, list(i))
    print('Nodes:', end=' ')
    print(*(nods := list(g1.nodes())))
    print('Edges:', end=' ')
    print(*(edgs := list(g1.edges())))
    print('Degrees of nods:', end=' ')
    deg = []
    for j in g1:
        print(f'\'{j}\' -- {g1.degree(j)} ', end='  ')
    ex = nx.eccentricity(g1)
    print()
    print('Eccentricity of nodes:', end=' ')
    cnt1 = 0
    for j in list(ex):
        print(f'\'{j}\' -- {list(ex.values())[cnt1]}', end='  ')
        cnt1 += 1
    print()
    d = nx.diameter(g1)
    r = nx.radius(g1)
    if len(nods) > 1:
        print(f'Diameter -- {d}')
        print(f'Radius -- {r}')
    else:
        print("This component doesn't have a diameter and a radius.")

    if len(nods) > 1:
        lst = []
        lst1 = []
        for v, w in nx.bfs_edges(g1, list(ex)[list(ex.values()).index(d)]):
            lst.append((v, w))

        lst = lst[::g1.degree(list(ex)[list(ex.values()).index(d)])]
        for v, w in lst:
            if v not in lst1:
                lst1.append(v)
            if w not in lst1:
                lst1.append(w)

        edgs_c = []
        for e in edgs:
            p = tuple(reversed(e))
            if e in lst or p in lst:
                edgs_c.append('red')
            else:
                edgs_c.append('black')
        nods_c = []
        for n in nods:
            if n in lst1:
                nods_c.append('red')
            else:
                nods_c.append('black')
        nx.draw(g1, pos=pos, with_labels=True, font_color='white', edge_color=edgs_c, node_color=nods_c)
        plt.savefig(f'{cnt}cc.png', format="png")
        plt.show()

        tr.add_edges_from(nx.dfs_edges(g1))
    print()

nx.draw(tr, pos=pos, with_labels=True, font_color='white', node_color='black')
plt.savefig('tree.png', format="png")
plt.show()
