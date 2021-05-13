from nodesition import pos
import networkx as nx
import matplotlib.pyplot as plt


class MainGraph:
    def __init__(self, adjlist):
        self.g = nx.read_adjlist(adjlist)
        self._l = nx.Graph()
        self.lst = []
        self.lst1 = []

    def first_image(self):
        nx.draw_shell(self.g, with_labels=True, font_color='black', node_color='white', edgecolors='black')
        plt.savefig('main_shell.png', format='png')
        plt.show()

    def image(self, save_path, position=pos, node_c='white', edge_c='black'):
        nx.draw(self.g, pos=position, width=2,  with_labels=True, font_color='black', node_color=node_c, edge_color=edge_c, edgecolors='black')
        plt.savefig(save_path, format="png")
        plt.show()

    def cc(self):
        cnt = 0
        for i in nx.connected_components(self.g):
            cnt += 1
            comp_c = ConnectedComponent(i, cnt, 't.txt')
            comp_c.info()
            print(self.lst)
            if comp_c.trivial:
                comp_c.draw_diameter()
                self.lst += comp_c.lst
                self.lst1 += comp_c.lst1
                print(self.lst)
        _edgs_c = ['red' if e in self.lst or tuple(reversed(e)) in self.lst else 'black' for e in self.g.edges]
        _nods_c = ['red' if n in self.lst1 else 'white' for n in self.g.nodes]
        self.image('diameter.png', node_c=_nods_c, edge_c=_edgs_c)

    def tree(self):
        for i in nx.connected_components(self.g):
            g1 = nx.subgraph(self.g, list(i))
            self._l.add_edges_from(nx.dfs_edges(g1))
        _tree_c = ['red' if e in self._l.edges or tuple(reversed(e)) in self._l.edges else 'black' for e in self.g.edges]
        self.image('with_tree.png', edge_c=_tree_c)


class ConnectedComponent(MainGraph):
    def __init__(self, i, cnt, adjlist):
        super().__init__(adjlist)
        self._cnt = cnt
        self._i = i
        self._g1 = nx.subgraph(self.g, list(i))
        self.lst = []
        self.lst1 = []

    @property
    def diam_nod(self):
        return list(self.eccentircity)[list(self.eccentircity.values()).index(self.diameter)]

    @property
    def nods(self):
        return list(nx.nodes(self._g1))

    @property
    def edgs(self):
        return list(nx.edges(self._g1))

    @property
    def eccentircity(self):
        return nx.eccentricity(self._g1)

    @property
    def diameter(self):
        return nx.diameter(self._g1)

    @property
    def radius(self):
        return nx.radius(self._g1)

    @property
    def trivial(self):
        return len(self.nods) > 1

    def degree(self, el):
        return self._g1.degree(el)

    def info(self):
        print(f'For connected component №{self._cnt}:')
        print('Nodes:', len(self.nods))
        print('Edges:', len(self.edgs))
        print('Degrees: ', end=' ')
        for j in self._g1:
            print(f'\'{j}\' -- {self.degree(j)} ', end='  ')
        print()
        print('Eccentricity of nodes:', end=' ')
        cnt1 = 0
        for j in list(self.eccentircity):
            print(f'\'{j}\' -- {list(self.eccentircity.values())[cnt1]}', end='  ')
            cnt1 += 1
        print()
        if self.trivial:
            print('Diameter:', self.diameter, sep=' ')
            print('Radius:', self.radius, sep=' ')
        else:
            print("This component doesn't have a diameter and a radius.")
        print('\n\n')

    def draw_diameter(self):
        for v, w in nx.bfs_edges(self._g1, self.diam_nod):
            self.lst.append((v, w))
        self.lst = self.lst[::self._g1.degree(self.diam_nod)]

        for v, w in self.lst:
            if v not in self.lst1:
                self.lst1.append(v)
            if w not in self.lst1:
                self.lst1.append(w)


main = MainGraph('t.txt')
main.first_image()
main.image('main.png')
main.cc()
main.tree()
