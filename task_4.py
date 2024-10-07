import networkx as nx
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value, color="skyblue"):
        self.left_child = None
        self.right_child = None
        self.value = value
        self.color = color  # Additional argument to store the color of the node

def build_graph(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.value, pos=(x, y), layer=layer, color=node.color)
        if node.left_child is not None:
            graph.add_edge(node.value, node.left_child.value)
            left_shift = 1 / layer
            build_graph(graph, node.left_child, pos, x-left_shift, y-1, layer+1)
        if node.right_child is not None:
            graph.add_edge(node.value, node.right_child.value)
            right_shift = 1 / layer
            build_graph(graph, node.right_child, pos, x+right_shift, y-1, layer+1)
    return graph

def visualize_tree(tree_root):
    graph = nx.DiGraph()
    pos = {}
    tree = build_graph(graph, tree_root, pos)

    node_colors = [node[1]['color'] for node in tree.nodes(data=True)]

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=nx.get_node_attributes(tree, 'pos'), with_labels=True, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

# Creating the tree structure
root = TreeNode(0)
root.left_child = TreeNode(1, "red")
root.right_child = TreeNode(2, "green")
root.left_child.left_child = TreeNode(3, "blue")
root.left_child.right_child = TreeNode(4, "yellow")
root.right_child.left_child = TreeNode(5, "purple")
root.right_child.right_child = TreeNode(6, "orange")

# Displaying the tree structure
visualize_tree(root)