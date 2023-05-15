class Grafo():
    '''
    V(): retorna o número de vértices
    A(): retorna o número de arestas
    AddArestas(u, v): Adicionar arestas
    Adj(v): retorna vértices adjacentes
    '''
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]


    def V(self):
        return self.vertices


    def A(self):
        A = 0
        for row in self.grafo:
            for checker in row:
                if checker:
                    A += 1
        return A/2


    def adj(self, vertice):
        iterable = []
        for i,u in enumerate(self.grafo):
            if u[vertice - 1]:
                iterable.append(i+1)
        return iterable


    def addAresta(self, u, v):
        '''
        u, v: vértices que vão ser conectados
        '''
        self.grafo[u-1][v-1] = 1 # trocar = por += para grafos com  múltiplas arestas
        self.grafo[v-1][u-1] = 1 


    def showMatrix(self):
        print('Matriz de adjacência:')
        for i in range(self.vertices):
            print(self.grafo[i])


    def toString(self):
        for u in range(self.vertices):
            for v, checker in enumerate(self.grafo[u]):
                if checker:
                    print(f'{u+1} → {v+1}')


    
g = Grafo(4)
g.addAresta(1,2)
g.addAresta(1,3)
g.addAresta(2,4)
g.toString()
g.showMatrix()
print(g.A())
print(g.V())
print(g.adj(1))