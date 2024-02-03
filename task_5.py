import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import rgb2hex

class ColoredNode:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())
        self.left = None
        self.right = None

def add_tree_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_tree_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_tree_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def depth_first_traversal(node, colors, depth=0):
    if node is not None:
        colors[node.id] = rgb2hex(cm.viridis(depth / 10.0))  # Adjusting scale for gradient
        depth_first_traversal(node.left, colors, depth + 1)
        depth_first_traversal(node.right, colors, depth + 1)

def breadth_first_traversal(root, colors):
    queue = [root]
    depth = 0

    while queue:
        current_level_size = len(queue)

        for i in range(current_level_size):
            node = queue.pop(0)
            colors[node.id] = rgb2hex(cm.viridis(depth / 10.0))  # Adjusting scale for gradient

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        depth += 1

def draw_tree_traversal(tree_root, traversal_type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_tree_edges(tree, tree_root, pos)

    colors = {}
    if traversal_type == "depth_first":
        depth_first_traversal(tree_root, colors)
    elif traversal_type == "breadth_first":
        breadth_first_traversal(tree_root, colors)

    node_colors = [colors[node] for node in tree.nodes()]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

tree_root = ColoredNode(0)
tree_root.left = ColoredNode(4)
tree_root.left.left = ColoredNode(5)
tree_root.left.right = ColoredNode(10)
tree_root.right = ColoredNode(1)
tree_root.right.left = ColoredNode(3)


if __name__ == '__main__':
    draw_tree_traversal(tree_root, "depth_first")

    draw_tree_traversal(tree_root, "breadth_first")
