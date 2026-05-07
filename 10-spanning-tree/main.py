# TODO 0 pipem nainstalovat
# https://github.com/JakubSido/adthelpers

# pip install git+https://github.com/JakubSido/adthelpers
# nebo stáhnout zip a instalovat jako pip install <cesta_k_rozbalenému_zipu>


import json
from queue import PriorityQueue

import adthelpers


class Graph:
    def __init__(self) -> None:
        self.edges: dict[int, list[tuple[float, int]]] = {}

    def add_edge(self, src: int, dst: int, weight: float = 0) -> None:
        # TODO 1 napište kód přidání hrany do datové struktury grafu
        if src not in self.edges:
            self.edges[src] = []
        if dst not in self.edges:
            self.edges[dst] = []
        self.edges[src].append((weight,dst))
        self.edges[dst].append((weight,src))


def load_graph(filename: str) -> Graph:
    graph = Graph()

    # TODO 2 vytvořte graf podle dat ze souboru
    with open(filename,"r") as file:
        data = json.load(file)
    for link in data["links"]:
        graph.add_edge(link["source"],link["target"],link["weight"])
    return graph


def spanning_tree(graph: Graph) -> None:
    closed: set[int] = set()
    sp_tree: list[tuple[int, int]] = []
    queue: PriorityQueue = PriorityQueue()

    painter = adthelpers.painter.Painter(
        graph,
        visible=queue,
        closed=closed,
        color_edges=sp_tree,
    )
    painter.draw_graph()

    # TODO 3 Implementujte Prim-Jarníkův algoritmus pro nalezení minimální kostry
    #weight source target
    queue.put((-1,(-1,0)))
    while not queue.empty():
        weight,(src, target)=queue.get()
        #najdu všechny sousedy src
        #přidam je do fronty
        current = target
        if current in closed:
            continue
        closed.add(current)
        sp_tree.append((src,target))
        for neighbor in graph.edges[current]:
           weight = neighbor[0]
           dest = neighbor[1]
           queue.put((weight,(current,dest)))
           painter.draw_graph()
    painter.draw_graph()

def main() -> None:
    graph = load_graph("10-spanning-tree/data/graph_grid_s3_3.json")


    painter = adthelpers.painter.Painter(
        graph,
        # colors=("red", "blue", "yellow", "grey") # pokud by byl problém s barvami je možné změnit
    )
    painter.draw_graph()

    # debug to see progress...
    spanning_tree(graph)

    # don't close before user acknowledges diagrams
    input("Press enter to exit program...")


if __name__ == "__main__":
    main()
