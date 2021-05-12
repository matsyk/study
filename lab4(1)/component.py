import networkx as nx


class ConnectedComponent:
    def __init__(self, gr, i, cnt):
        self._cnt = cnt
        self._i = i
        self._g1 = nx.subgraph(gr, list(i))
        self.lst = []
        self.lst1 = []
        self.edgs_c = []
        self.nods_c = []
        self._diam_nod = list(self.eccentircity)[list(self.eccentircity.values()).index(self.diameter)]

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
        for v, w in nx.bfs_edges(self._g1, self._diam_nod):
            self.lst.append((v, w))
        self.lst = self.lst[::self._g1.degree(self._diam_nod)]
        for v, w in self.lst:
            if v not in self.lst1:
                self.lst1.append(v)
            if w not in self.lst1:
                self.lst1.append(w)
