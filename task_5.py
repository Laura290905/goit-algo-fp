import networkx as nx
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value, color="skyblue"):
        self.left_child = None
        self.right_child = None
        self.value = value
        self.color = color  # Attribute to store the color of the node

def build_graph(graph, node, pos, x=0, y=0, depth=1):
    if node is not None:
        graph.add_node(node.value, pos=(x, y), depth=depth, color=node.color)
        if node.left_child is not None:
            graph.add_edge(node.value, node.left_child.value)
            left_shift = 1 / depth
            build_graph(graph, node.left_child, pos, x-left_shift, y-1, depth+1)
        if node.right_child is not None:
            graph.add_edge(node.value, node.right_child.value)
            right_shift = 1 / depth
            build_graph(graph, node.right_child, pos, x+right_shift, y-1, depth+1)
    return graph

def display_tree(tree_root):
    graph = nx.DiGraph()
    pos = {}
    tree = build_graph(graph, tree_root, pos)

    node_colors = [node[1]['color'] for node in tree.nodes(data=True)]

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=nx.get_node_attributes(tree, 'pos'), with_labels=True, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def in_order_color(node, colors, counter):
    if node:
        in_order_color(node.left_child, colors, counter)
        node.color = colors[counter[0] % len(colors)]
        counter[0] += 1
        in_order_color(node.right_child, colors, counter)
