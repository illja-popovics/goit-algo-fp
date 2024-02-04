import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph
def dfs_traversal(tree_root):
    visited = set()
    dfs_result = []
    
    def dfs(node):
        if node is not None and node.id not in visited:
            visited.add(node.id)
            dfs_result.append(node.id)
            dfs(node.left)
            dfs(node.right)
    
    dfs(tree_root)
    return dfs_result

def bfs_traversal(tree_root):
    visited = set()
    bfs_result = []
    queue = deque([tree_root])
    
    while queue:
        node = queue.popleft()
        if node is not None and node.id not in visited:
            visited.add(node.id)
            bfs_result.append(node.id)
            queue.append(node.left)
            queue.append(node.right)
    
    return bfs_result

def draw_tree(tree_root, traversal_type):
    if traversal_type == "BFS":
        traversal_sequence = bfs_traversal(tree_root)
        distances = get_distances(tree_root)
    elif traversal_type == "DFS":
        traversal_sequence = dfs_traversal(tree_root)
    else:
        raise ValueError("Invalid traversal type. Please use 'BFS' or 'DFS'.")

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if traversal_type == "DFS":
        colors = [f'#{i:02x}{i:02x}{i:02x}' for i in range(0, 256, int(256/len(traversal_sequence)))]
        node_colors = {node_id: colors[i] for i, node_id in enumerate(traversal_sequence)}
    else:  
        max_distance = max(distances.values())
        colors = [f'#{i:02x}{i:02x}{i:02x}' for i in range(0, 256, int(256/(max_distance + 1)))]
        node_colors = {node_id: colors[distances[node_id]] for node_id in traversal_sequence}

    labels = {node[0]: tree.nodes[node[0]]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=list(node_colors.values()))
    plt.show()

def get_distances(tree_root):
    distances = {tree_root.id: 0}
    queue = deque([(tree_root, 0)])

    while queue:
        node, distance = queue.popleft()
        for neighbor in [node.left, node.right]:
            if neighbor and neighbor.id not in distances:
                distances[neighbor.id] = distance + 1
                queue.append((neighbor, distance + 1))

    return distances


if __name__ == '__main__':
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення дерева
    draw_tree(root, "DFS")

    draw_tree(root, "BFS")