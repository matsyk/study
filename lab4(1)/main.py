from nodesition import pos
from component import ConnectedComponent
import networkx as nx
import matplotlib.pyplot as plt


class MainGraph:
    def __init__(self, adjlist):
        self.g = nx.read_adjlist(adjlist)
        self._l = nx.Graph()

    def first_image(self):
        nx.draw_shell(self.g, with_labels=True, font_color='white', node_color='black')
        plt.savefig('main_shell.png', format='png')
        plt.show()

    def image(self, save_path, position=pos, node_c='black', edge_c='black'):
        nx.draw(self.g, pos=position, with_labels=True, font_color='white', node_color=node_c, edge_color=edge_c)
        plt.savefig(save_path, format="png")
        plt.show()

    def cc(self):
        cnt = 0
        _edgs_c = []
        _nods_c = []
        lst = []
        lst1 = []

        for i in nx.connected_components(self.g):
            cnt += 1
            comp_c = ConnectedComponent(self.g, i, cnt)
            comp_c.info()
            if comp_c.trivial:
                comp_c.draw_diameter()
                lst += comp_c.lst
                lst1 += comp_c.lst1
                _edgs_c += comp_c.edgs_c
                _nods_c += comp_c.nods_c
        for e in self.g.edges:
            p = tuple(reversed(e))
            if e in lst or p in lst:
                _edgs_c.append('red')
            else:
                _edgs_c.append('black')
        for n in self.g.nodes:
            if n in lst1:
                _nods_c.append('red')
            else:
                _nods_c.append('black')
        self.image('diameter.png', node_c=_nods_c, edge_c=_edgs_c)

    def tree(self):
        for i in nx.connected_components(self.g):
            g1 = nx.subgraph(self.g, list(i))
            self._l.add_edges_from(nx.dfs_edges(g1))
        _tree_c = []
        for e in self.g.edges:
            p = tuple(reversed(e))
            if e in self._l.edges or p in self._l.edges:
                _tree_c.append('red')
            else:
                _tree_c.append('black')
        self.image('with_tree.png', edge_c=_tree_c)


main = MainGraph('t.txt')
main.first_image()
main.image('main.png')
main.cc()
main.tree()
