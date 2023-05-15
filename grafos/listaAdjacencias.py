class Grafo:

    
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for _ in range(self.vertices)]


    def V(self):
        return self.vertices


    def A(self):
        A = 0
        for row in self.grafo:
            A += len(row)
        return A/2


    def addAresta(self, u, v):
        # Isso para grafos não direcionados 
        self.grafo[u-1].append(v)
        self.grafo[v-1].append(u)


    def adj(self, vertice):
        return self.grafo[vertice - 1]
    

    def toString(self):
        print('Lista de adjacência:')
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  →', end='  ')
            print('')


g = Grafo(4)
g.addAresta(1,2)
g.addAresta(1,3)
g.addAresta(2,4)
g.addAresta(1,4)
g.toString()
print(g.A())
print(g.V())
print(g.adj(1))