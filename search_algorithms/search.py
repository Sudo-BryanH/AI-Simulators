class Node:
    def __init__(self, dataval):
        self.data = dataval
        self.neigbors = []

class Stack:
    def __init__(self):
        self.nodes = []
    def push(self, item):
        self.nodes.append(item)
    def pop(self):
        return self.nodes.pop()
    def empty(self):
        return len(self.nodes) == 0


class Queue:
    def __init__(self):
        self.nodes = []
    def push(self, item):
        self.nodes.insert(0, item)
    def pop(self):
        return self.nodes.pop()
    def empty(self):
        return len(self.nodes) == 0


def search(front, goal, start_node):
    '''
    while frontier is not empty:
        select and remove path <no,....,nk> from frontier
        if goal(nk)
            return <no,....,nk>
        for every neighbor n of nk
        add <no,....,nk, n> to frontier
    return NULL
    '''
    start = []
    start.append(start_node)
    frontier = front;
    frontier.push(start)
    while frontier.empty:
        path = frontier.pop()
        last = path[len(path)-1]
        print(f"{last.data} Expanded")
        
        if last.data == goal.data:
            print(f"Goal node {last.data} found")
            return path
        for n in last.neighbors:
            new_path = path.copy()
            new_path.append(n)
            
            print([n.data for n in new_path], "appended")
            frontier.push(new_path)


    return []   
    
def main():
    
    S = Node("S")
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    H = Node("H")
    Z = Node("Z")

    S.neighbors = {C, B, A}
    A.neighbors = B.neighbors = {C}
    C.neighbors = {F, E, D}
    D.neighbors = E.neighbors = {F}
    F.neighbors = {Z, H, G}
    G.neighbors = F.neighbors = {Z}

    q = Queue()
    st = Stack()

    BFS_soln = search(q, Z, S)
    print("BFS soln:", [n.data for n in BFS_soln])
    DFS_soln = search(st, Z, S)
    print("DFS soln:", [n.data for n in DFS_soln])

if __name__ == "__main__":
    main()
    # python search.py