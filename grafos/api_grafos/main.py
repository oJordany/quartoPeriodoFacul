import json

class GrafoListaAdj:
    """
    :method V(): retorna o número de vértices.
    :method A(): retorna o número de arestas.
    :method AddArestas(u, v): Adicionar arestas.
    :method Adj(v): retorna vértices adjacentes.
    :method DFS(verticeInicial): retorna um dict com todos os antecessores, as cores, o tempo de descoberta, e de finalização de cada vértice
    :method __DFS_VISIT(u): percorre os caminhos em profundidade recursivamente
    """
    
    def __init__(self, vertices, isDirecionado=False):
        """
        instancia um grafo com a quantidade de vertices passada como parâmetro
        :param vertices: int.
        """
        self.vertices = vertices
        self.grafo = [[] for _ in range(self.vertices)]
        self.isDirecionado = isDirecionado


    def V(self):
        """
        :return int quantidade de vértices.
        """
        return self.vertices


    def A(self):
        """
        :return int quantidade de arestas.
        """
        A = 0
        for row in self.grafo:
            A += len(row)
        return A/2


    def addAresta(self, u, v):
        '''
        cria uma nova aresta conectando dois vértices
        :param u: int vértice de origem.
        :param v: int vértice de destino.
        '''
        if (self.isDirecionado):
            self.grafo[u-1].append(v)
        else:
            # Isso para grafos não direcionados 
            self.grafo[u-1].append(v)
            self.grafo[v-1].append(u)


    def adj(self, vertice):
        """
        :param vertice: int.
        :return list lista de vértices adjacentes a vertice.
        """
        return self.grafo[vertice - 1]
    

    def arestasAdj(self):
        """
        :return dict todas as arestas adjacentes para cada vértice.
        """
        arestasAdjacentes = {f'{i+1}':[] for i in range(0,self.vertices)}
        for i, listAdj in enumerate(self.grafo):
            for j in listAdj:
                arestasAdjacentes[f'{i+1}'].append((i+1,j))
        return arestasAdjacentes
    

    def toString(self):
        """
        printa uma representação em string do grafo
        """
        string = ''
        string += 'Lista de adjacência:\n'
        for i in range(self.vertices):
            string += f'{i+1}:'
            for j in self.grafo[i]:
                string += f' {j} →'
            string += '\n'
        return string
    
    def DFS(self, verticeInicial):
        """
        :param verticeInicial: int vértice de onde o caminho começa.
        :return dict com o pi (antecessores de cada vértice), a cor(cor de cada vértice após percorrer todo o caminho), o d(tempo de descoberta de cada vértice) e o f(tempo de finalização de cada vértice)
        """
        self.pi = {}
        self.cor = {}
        for vertice in range(1, len(self.grafo)+1):
            self.cor[vertice] = 'BRANCO'
        self.pi[verticeInicial] = None
        self.tempo = 0 
        self.d = {}
        self.f = {}
        if self.cor[verticeInicial] == "BRANCO":
            self.__DFS_VISIT(verticeInicial)
        return {'pi':self.pi, 'cor':self.cor, 'd':self.d, 'f':self.f}
    
            
    def __DFS_VISIT(self, u):
        """
        visita cada vértice e vai percorrendo o caminho recursivamente
        :param u: int vértice que vai ser visitado.
        """
        self.cor[u] = "CINZA"
        self.tempo += 1
        self.d[u] = self.tempo
        for v in self.adj(u):
            if self.cor[v] == 'BRANCO':
                self.pi[v] = u
                self.__DFS_VISIT(v)
        self.cor[u] = 'PRETO'
        self.tempo += 1
        self.f[u] = self.tempo

    def BFS(self, verticeInicial):
        """
        :param verticeInicial: int vértice de onde o caminho começa.
        :return dict com o pi (antecessores de cada vértice), a cor(cor de cada vértice após percorrer todo o caminho), o d(tempo de descoberta de cada vértice) e o f(tempo de finalização de cada vértice)
        """
        self.pi = {}
        self.cor = {}
        for vertice in range(1, len(self.grafo)+1):
            self.cor[vertice] = 'BRANCO'
        self.d = {}
        self.d[verticeInicial] = 0
        self.pi[verticeInicial] = None
        self.Q = []
        self.Q.append(verticeInicial)
        while(self.Q):
            u = self.Q.pop(0)
            for v in self.adj(u):
                if self.cor[v] == "BRANCO":
                    self.cor[v] = "CINZA"
                    self.d[v] = self.d[u] + 1
                    self.pi[v] = u
                    self.Q.append(v)
            self.cor[u] = "PRETO"
        return {'pi': self.pi, 'cor': self.cor, 'd': self.d}


class GrafoMatrizAdj():
    """
    :method V(): retorna o número de vértices.
    :method A(): retorna o número de arestas.
    :method AddArestas(u, v): Adicionar arestas.
    :method Adj(v): retorna vértices adjacentes.
    """
    def __init__(self, vertices, isDirecionado=False):
        """
        instancia um grafo com a quantidade de vertices passada como parâmetro
        :param vertices: int.
        """
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        self.isDirecionado = isDirecionado

    def V(self):
        """
        :return int quantidade de vértices.
        """
        return self.vertices


    def A(self):
        """
        :return int quantidade de arestas.
        """
        A = 0
        for row in self.grafo:
            for checker in row:
                if checker:
                    A += 1
        return A/2


    def adj(self, vertice):
        """
        :param vertice: int.
        :return list lista de vértices adjacentes a vertice.
        """
        iterable = []
        for i,u in enumerate(self.grafo):
            if u[vertice - 1]:
                iterable.append(i+1)
        return iterable
    

    def arestasAdj(self):
        """
        :return dict todas as arestas adjacentes para cada vértice.
        """
        arestasAdjacentes = {f'{i+1}':[] for i in range(0, self.vertices)}
        for i, row in enumerate(self.grafo):
            for j, checker in enumerate(row):
                if checker:
                    arestasAdjacentes[f'{i+1}'].append((i+1,j+1))
        return arestasAdjacentes


    def addAresta(self, u, v):
        '''
        cria uma nova aresta conectando dois vértices
        :param u: vértice de origem.
        :param v: vértice de destino.
        '''
        if (self.isDirecionado):
            self.grafo[u-1][v-1] = 1 # trocar = por += para grafos com  múltiplas arestas
        else:    
            self.grafo[u-1][v-1] = 1 # trocar = por += para grafos com  múltiplas arestas
            self.grafo[v-1][u-1] = 1 


    def showMatrix(self):
        """
        printa a matriz de adjacência
        """
        print('Matriz de adjacência:')
        for i in range(self.vertices):
            print(self.grafo[i])


    def toString(self):
        """
        printa uma representação em string do grafo
        """
        for u in range(self.vertices):
            for v, checker in enumerate(self.grafo[u]):
                if checker:
                    print(f'{u+1} → {v+1}')            


    def DFS(self, verticeInicial):
        """
        :param verticeInicial: int vértice de onde o caminho começa.
        :return dict com o pi (antecessores de cada vértice), a cor(cor de cada vértice após percorrer todo o caminho), o d(tempo de descoberta de cada vértice) e o f(tempo de finalização de cada vértice)
        """
        self.pi = {}
        self.cor = {}
        for vertice in range(1, len(self.grafo)+1):
            self.cor[vertice] = 'BRANCO'
        self.pi[verticeInicial] = None
        self.tempo = 0 
        self.d = {}
        self.f = {}
        if self.cor[verticeInicial] == "BRANCO":
            self.__DFS_VISIT(verticeInicial)
        return {'pi':self.pi, 'cor':self.cor, 'd':self.d, 'f':self.f}
    
            
    def __DFS_VISIT(self, u):
        """
        visita cada vértice e vai percorrendo o caminho recursivamente
        :param u: int vértice que vai ser visitado.
        """
        self.cor[u] = "CINZA"
        self.tempo += 1
        self.d[u] = self.tempo
        for v in self.adj(u):
            if self.cor[v] == 'BRANCO':
                self.pi[v] = u
                self.__DFS_VISIT(v)
        self.cor[u] = 'PRETO'
        self.tempo += 1
        self.f[u] = self.tempo

    
    def BFS(self, verticeInicial):
        """
        :param verticeInicial: int vértice de onde o caminho começa.
        :return dict com o pi (antecessores de cada vértice), a cor(cor de cada vértice após percorrer todo o caminho), o d(tempo de descoberta de cada vértice) e o f(tempo de finalização de cada vértice)
        """
        self.pi = {}
        self.cor = {}
        for vertice in range(1, len(self.grafo)+1):
            self.cor[vertice] = 'BRANCO'
        self.d = {}
        self.d[verticeInicial] = 0
        self.pi[verticeInicial] = None
        self.Q = []
        self.Q.append(verticeInicial)
        while(self.Q):
            u = self.Q.pop(0)
            for v in self.adj(u):
                if self.cor[v] == "BRANCO":
                    self.cor[v] = "CINZA"
                    self.d[v] = self.d[u] + 1
                    self.pi[v] = u
                    self.Q.append(v)
            self.cor[u] = "PRETO"
        return {'pi': self.pi, 'cor': self.cor, 'd': self.d}

g = GrafoListaAdj(8)
g.addAresta(8,1)
g.addAresta(8,2)
g.addAresta(8,7)
g.addAresta(1,2)
g.addAresta(1,6)
g.addAresta(1,7)
g.addAresta(6,3)
g.addAresta(6,7)
g.addAresta(3,4)
g.addAresta(4,5)
s = g.toString()
print(s)
print("Arestas: ",g.A())
print("Vértices: ",g.V())
print("Vértices adjacentes ao vértice 1: ", g.adj(1))
print('arestas adjacentes: ', g.arestasAdj())
print('dfs: ', g.DFS(3))
print('bfs: ', g.BFS(8))

print('\n')

h = GrafoMatrizAdj(8)
h.addAresta(8,1)
h.addAresta(8,2)
h.addAresta(8,7)
h.addAresta(1,2)
h.addAresta(1,6)
h.addAresta(1,7)
h.addAresta(6,3)
h.addAresta(6,7)
h.addAresta(3,4)
h.addAresta(4,5)
h.toString()
h.showMatrix()
print("Arestas: ",h.A())
print("Vértices: ",h.V())
print("Vértices adjacentes ao vértice 1: ",h.adj(1))
print('arestas adjacentes: ', h.arestasAdj())
print('dfs: ', h.DFS(8))
print('dfs: ', h.BFS(8))