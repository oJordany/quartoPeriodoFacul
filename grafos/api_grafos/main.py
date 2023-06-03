import numpy as np
import heapq # => importando o módulo heapq


class FilaDePrioridade:
    
    def __init__(self):
        self.fila = []
        self.indice = 0
    
    def inserir(self, item, prioridade):
        heapq.heappush(self.fila, (prioridade, self.indice, item))
        self.indice += 1

    def remover(self):
        return heapq.heappop(self.fila)[-1]
    
    def alterarPrioridade(self, item, novaPrioridade):
        for i, elemento in enumerate(self.fila):
            if elemento[2] == item:
                self.fila[i] = (novaPrioridade, elemento[1], item)
                heapq.heapify(self.fila)
                break


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


    def addAresta(self, u, v, peso=None):
        '''
        cria uma nova aresta conectando dois vértices
        :param u: int vértice de origem.
        :param v: int vértice de destino.
        '''
        if (self.isDirecionado):
            self.grafo[u-1].append({'nome': v, 'peso': peso})
        else:
            # Isso para grafos não direcionados 
            self.grafo[u-1].append({'nome': v, 'peso': peso})
            self.grafo[v-1].append({'nome': u, 'peso': peso})


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
        arestasAdjacentes = []
        for i, listAdj in enumerate(self.grafo):
            for j in listAdj:
                arestasAdjacentes.append((i+1,j['nome']))
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
                string += f' {j["nome"]}|peso {j["peso"]} →'
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
            if self.cor[v['nome']] == 'BRANCO':
                self.pi[v['nome']] = u
                self.__DFS_VISIT(v['nome'])
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
                if self.cor[v['nome']] == "BRANCO":
                    self.cor[v['nome']] = "CINZA"
                    self.d[v['nome']] = self.d[u] + 1
                    self.pi[v['nome']] = u
                    self.Q.append(v['nome'])
            self.cor[u] = "PRETO"
        return {'pi': self.pi, 'cor': self.cor, 'd': self.d}
    
    def __w(self, u, v):
        """ 
        Obtém o peso da aresta de u para v
        :param u: int vértice origem
        :param v: int vértice destino
        :return int correspondente ao peso da aresta de u para v
        """
        for adj in self.grafo[u-1]:
            if adj['nome'] == v:
                return adj['peso']
        # return next(filter(lambda d: d.get('nome') == v, self.adj(u)), None)['peso']
    
    def __relax(self, u, v):
        """
        Aplica o relaxamento verificando se é possível relaxar de u para v
        :param u: int vértice origem
        :param v: int vértice destino
        """
        if self.d[v] > self.d[u] + self.__w(u, v):
            self.d[v] = self.d[u] + self.__w(u, v)
            self.pi[v] = u

    def __initializeSingleSource(self, s):
        """
        Inicializa todos os vértices com inf, exceto o vérice fonte que recebe peso 0
        :param s: int vértice fonte
        """
        self.d = {}
        self.pi = {}
        for i in range(1,len(self.grafo)+1):
            self.d[i] = float('Inf')
            self.pi[i] = None
        self.d[s] = 0

    def dijkstra(self, s):
        """ 
        Aplica o algoritmo de Dijkstra no grafo partindo de um vértice fonte s
        :param s: int vértice fonte de onde o algoritmo de Dijkstra vai se iniciar
        :return list S que é uma lista com o caminho mínimo 
        """
        self.__initializeSingleSource(s)
        S = []
        self.Q = FilaDePrioridade()
        for i in range(1, self.V()+1):
            self.Q.inserir(i, self.d[i])
        while self.Q.fila:
            u = int(self.Q.remover())
            S.append(u)
            for v in self.adj(u):
                self.__relax(u, v['nome'])
                self.Q.alterarPrioridade(v['nome'], self.d[v['nome']])
        return S, self.d, self.pi
    
    def bellman_ford(self, s):
        """
        :param s: int vértice fonte de onde o algoritmo de Bellman-Ford vai se iniciar
        :return list contendo o verificador booleano do ciclo negativo, a distância mínima de s para cada vértice e o vetor pi de antecessores
        """
        self.__initializeSingleSource(s)
        for i in range(1, self.V()):
            for aresta in self.arestasAdj():
                self.__relax(aresta[0], aresta[1])
        
        for aresta in self.arestasAdj():
            if self.d[aresta[1]] > self.d[aresta[0]] + self.__w(aresta[0], aresta[1]):
                return [True, self.d, self.pi]
        return [False, self.d, self.pi]
    
    def floyd_warshall(self):
        """
        :return list[|V|][|V|], list[|V|][|V|] sendo a primeira matriz de distâncias mínimas de cada vértice e a segunda matriz de antecessores
        """
        self.A = [[float('Inf')]*self.V() for i in range(self.V())]
        self.pi = [[None]*self.V() for i in range(self.V())]

        for v in range(1, self.V()+1):
            for w in range(1, self.V()+1):
                if v == w:
                    self.A[v-1][w-1] = 0
                else:
                    peso = self.__w(v, w)
                    if peso:
                        self.A[v-1][w-1] = peso
                        self.pi[v-1][w-1] = v

        for k in range(1, self.V()+1):
            for v in range(1, self.V()+1):  
                for w in range(1, self.V()+1):
                    if (self.A[v-1][k-1] + self.A[k-1][w-1]) < self.A[v-1][w-1]:
                        self.A[v-1][w-1] = self.A[v-1][k-1] + self.A[k-1][w-1]
                        self.pi[v-1][w-1] = self.pi[k-1][w-1]

        return self.A, self.pi
    
    def __DFS_AUX(self, verticeInicial):
        """
        :param verticeInicial: int vértice de onde o caminho começa.
        """
        if self.cor[verticeInicial] == "BRANCO":
            self.id[verticeInicial] = self.cont
            self.__DFS_VISIT_AUX(verticeInicial)
            
    def __DFS_VISIT_AUX(self, u):
        """
        visita cada vértice e vai percorrendo o caminho recursivamente
        :param u: int vértice que vai ser visitado.
        """
        self.cor[u] = "CINZA"
        for v in self.adj(u):
            if self.cor[v['nome']] == 'BRANCO':
                self.id[v['nome']] = self.cont
                self.__DFS_VISIT_AUX(v['nome'])
        self.cor[u] = 'PRETO'

    def componentesConectadas(self):
        """ 
        Aplica o DFS com contador para encontrar as componentes conectadas em um Grafo
        :return int, dict sendo o primeiro a quantidade de componentes conectadas e o segundo os IDs de cada vértice que formam uma componente conectada
        """
        self.cor = {}
        self.id = {}
        self.cont = 0
        for vertice in range(1, len(self.grafo)+1):
            self.cor[vertice] = 'BRANCO'
        for vertice in range(1, len(self.grafo)+1):
            if (self.cor[vertice] != 'PRETO'):
                self.__DFS_AUX(vertice)
                self.cont += 1

        return self.cont, self.id

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
        for i,u in enumerate(self.grafo[vertice - 1]):
            if u:
                iterable.append(i+1)
        return iterable
    

    def arestasAdj(self):
        """
        :return dict todas as arestas adjacentes para cada vértice.
        """
        arestasAdjacentes = []
        for i, row in enumerate(self.grafo):
            for j, checker in enumerate(row):
                if checker:
                    arestasAdjacentes.append((i+1,j+1))
        return arestasAdjacentes


    def addAresta(self, u, v, peso=1):
        '''
        cria uma nova aresta conectando dois vértices
        :param u: vértice de origem.
        :param v: vértice de destino.
        '''
        if (self.isDirecionado):
            self.grafo[u-1][v-1] = peso # trocar = por += para grafos com  múltiplas arestas
        else:    
            self.grafo[u-1][v-1] = peso # trocar = por += para grafos com  múltiplas arestas
            self.grafo[v-1][u-1] = peso 


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
    

    def __w(self, u, v):
        """ 
        Obtém o peso da aresta de u para v
        :param u: int vértice origem
        :param v: int vértice destino
        :return int correspondente ao peso da aresta de u para v
        """
        return self.grafo[u-1][v-1] 
    
    def __relax(self, u, v):
        """
        Aplica o relaxamento verificando se é possível relaxar de u para v
        :param u: int vértice origem
        :param v: int vértice destino
        """
        if self.d[v] > self.d[u] + self.__w(u, v):
            self.d[v] = self.d[u] + self.__w(u, v)
            self.pi[v] = u

    def __initializeSingleSource(self, s):
        """
        Inicializa todos os vértices com inf, exceto o vérice fonte que recebe peso 0
        :param s: int vértice fonte
        """
        self.d = {}
        self.pi = {}
        for i in range(1,len(self.grafo)+1):
            self.d[i] = float('Inf')
            self.pi[i] = None
        self.d[s] = 0

    def dijkstra(self, s):
        """ 
        Aplica o algoritmo de Dijkstra no grafo partindo de um vértice fonte s
        :param s: int vértice fonte de onde o algoritmo de Dijkstra vai se iniciar
        :return list S que é uma lista com o caminho mínimo 
        """
        self.__initializeSingleSource(s)
        S = []
        self.Q = FilaDePrioridade()
        for i in range(1, self.V()+1):
            self.Q.inserir(i, self.d[i])
        while self.Q.fila:
            u = int(self.Q.remover())
            S.append(u)
            for v in self.adj(u):
                self.__relax(u, v)
                self.Q.alterarPrioridade(v, self.d[v])
        return S, self.d, self.pi
    

    def bellman_ford(self, s):
        """
        :param s: int vértice fonte de onde o algoritmo de Bellman-Ford vai se iniciar
        :return list contendo o verificador booleano do ciclo negativo, a distância mínima de s para cada vértice e o vetor pi de antecessores
        """
        self.__initializeSingleSource(s)
        for i in range(1, self.V()):
            for aresta in self.arestasAdj():
                self.__relax(aresta[0], aresta[1])
        
        for aresta in self.arestasAdj():
            if (self.d[aresta[1]] > self.d[aresta[0]]) + self.__w(aresta[0], aresta[1]):
                return [True, self.d, self.pi]
        return [False, self.d, self.pi]
    
    def floyd_warshall(self):
        """
        :return list[|V|][|V|], list[|V|][|V|] sendo a primeira matriz de distâncias mínimas de cada vértice e a segunda matriz de antecessores
        """
        self.A = [[float('Inf')]*self.V() for i in range(self.V())]
        self.pi = [[None]*self.V() for i in range(self.V())]

        for v in range(1, self.V()+1):
            for w in range(1, self.V()+1):
                if v == w:
                    self.A[v-1][w-1] = 0
                else:
                    peso = self.__w(v, w)
                    if peso:
                        self.A[v-1][w-1] = peso
                        self.pi[v-1][w-1] = v

        for k in range(1, self.V()+1):
            for v in range(1, self.V()+1):  
                for w in range(1, self.V()+1):
                    if (self.A[v-1][k-1] + self.A[k-1][w-1]) < self.A[v-1][w-1]:
                        self.A[v-1][w-1] = self.A[v-1][k-1] + self.A[k-1][w-1]
                        self.pi[v-1][w-1] = self.pi[k-1][w-1]

        return self.A, self.pi
    
    def __DFS_AUX(self, verticeInicial):
        """
        :param verticeInicial: int vértice de onde o caminho começa.
        """

        if self.cor[verticeInicial] == "BRANCO":
            self.id[verticeInicial] = self.cont
            self.__DFS_VISIT_AUX(verticeInicial)
            
    def __DFS_VISIT_AUX(self, u):
        """
        visita cada vértice e vai percorrendo o caminho recursivamente
        :param u: int vértice que vai ser visitado.
        """
        self.cor[u] = "CINZA"
        for v in self.adj(u):
            if self.cor[v] == 'BRANCO':
                self.id[v] = self.cont
                self.__DFS_VISIT_AUX(v)
        self.cor[u] = 'PRETO'

    def componentesConectadas(self):
        """ 
        Aplica o DFS com contador para encontrar as componentes conectadas em um Grafo
        :return int, dict sendo o primeiro a quantidade de componentes conectadas e o segundo os IDs de cada vértice que formam uma componente conectada
        """
        self.cor = {}
        self.id = {}
        self.cont = 0
        for vertice in range(1, len(self.grafo)+1):
            self.cor[vertice] = 'BRANCO'
        for vertice in range(1, len(self.grafo)+1):
            if (self.cor[vertice] != 'PRETO'):
                self.__DFS_AUX(vertice)
                self.cont += 1

        return self.cont, self.id


converter = {
            's': 1,
            'u': 2,
            'x': 3,
            'v': 4,
            'y': 5
            }

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
# Dijkstra
gL = GrafoListaAdj(6, True)
gL.addAresta(0+1,1+1,1)
gL.addAresta(1+1,2+1,1)
gL.addAresta(2+1,3+1,1)
gL.addAresta(3+1,4+1,1)
gL.addAresta(4+1,5+1,1)
gL.addAresta(0+1,2+1,3)
gL.addAresta(0+1,5+1,6)
print(gL.toString())
s, d, pi = gL.dijkstra(converter['s'])
print(f'Dijkstra: S= {s}')
print(f'Dijkstra: d= {d}')
print(f'Dijkstra: pi= {pi}')
gBF = GrafoListaAdj(5, True)
# Bellman-Ford
gBF.addAresta(1,5,1)
gBF.addAresta(1,2,1)
gBF.addAresta(2,3,1)
gBF.addAresta(2,4,2)
gBF.addAresta(3,4,4)
gBF.addAresta(3,5,2)
gBF.addAresta(4,1,3)
gBF.addAresta(5,1,2)
gBF.addAresta(5,4,1)
print(np.matrix(gBF.arestasAdj()))
print(gBF.toString())
result = gBF.bellman_ford(1)
print(f"Bellman-Ford:\n{result}")
#Floyd-Warshall
gFW = GrafoListaAdj(5, True)
gFW.addAresta(1,5,1)
gFW.addAresta(1,2,1)
gFW.addAresta(2,3,1)
gFW.addAresta(2,4,2)
gFW.addAresta(3,4,4)
gFW.addAresta(3,5,2)
gFW.addAresta(4,1,3)
gFW.addAresta(5,1,2)
gFW.addAresta(5,4,1)
A, pi = gFW.floyd_warshall()
print('matriz de distância: \n', np.matrix(A))
print('matriz de antecessores: \n', np.matrix(pi))
#COMPONENTE CONECTADAS
gFW = GrafoListaAdj(13)
gFW.addAresta(1,2)
gFW.addAresta(1,3)
gFW.addAresta(1,7)
gFW.addAresta(6,5)
gFW.addAresta(6,4)
gFW.addAresta(5,4)
gFW.addAresta(5,7)
gFW.addAresta(8,9)
gFW.addAresta(10,11)
gFW.addAresta(10,12)
gFW.addAresta(10,13)
gFW.addAresta(12,13)
cont, ids = gFW.componentesConectadas()
print('Quantidade de componentes conectadas: \n', cont)
print('Componentes conectadas: \n', ids)

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
print("Vértices adjacentes ao vértice 1: ",h.adj(2))
print('arestas adjacentes: ', h.arestasAdj())
print('dfs: ', h.DFS(8))
print('bfs: ', h.BFS(8))
# Dijkstra
gM = GrafoMatrizAdj(5, True)
gM.addAresta(converter['s'], converter['u'], 10)
gM.addAresta(converter['s'], converter['x'], 5)
gM.addAresta(converter['u'], converter['v'], 1)
gM.addAresta(converter['u'], converter['x'], 2)
gM.addAresta(converter['x'], converter['u'], 3)
gM.addAresta(converter['x'], converter['v'], 9)
gM.addAresta(converter['x'], converter['y'], 2)
gM.addAresta(converter['v'], converter['y'], 4)
gM.addAresta(converter['y'], converter['s'], 7)
gM.addAresta(converter['y'], converter['v'], 6)
gM.showMatrix()
print(gM.adj(1))
s, d, pi = gM.dijkstra(converter['s'])
print(f'Dijkstra: S= {s}')
print(f'Dijkstra: d= {d}')
print(f'Dijkstra: pi= {pi}')
# Bellman-Ford
gBF = GrafoMatrizAdj(4, True)
gBF.addAresta(1,2,5)
gBF.addAresta(1,3,4)
gBF.addAresta(2,4,3)
gBF.addAresta(3,2,-6)
gBF.addAresta(4,3,2)
result = gBF.bellman_ford(1)
gBF.showMatrix()
print(f'Bellman-Ford: checker = {result[0]}')
print(f'Bellman-Ford: d = {result[1]}')
print(f'Bellman-Ford: pi = {result[2]}')
#Floyd-Warshall
gFW = GrafoMatrizAdj(5, True)
gFW.addAresta(1,5,1)
gFW.addAresta(1,2,1)
gFW.addAresta(2,3,1)
gFW.addAresta(2,4,2)
gFW.addAresta(3,4,4)
gFW.addAresta(3,5,2)
gFW.addAresta(4,1,3)
gFW.addAresta(5,1,2)
gFW.addAresta(5,4,1)
A, pi = gFW.floyd_warshall()
print('matriz de distância: \n', np.matrix(A))
print('matriz de antecessores: \n', np.matrix(pi))
#COMPONENTE CONECTADAS
gFW = GrafoMatrizAdj(13)
gFW.addAresta(1,2)
gFW.addAresta(1,3)
gFW.addAresta(1,7)
gFW.addAresta(6,5)
gFW.addAresta(6,4)
gFW.addAresta(5,4)
gFW.addAresta(5,7)
gFW.addAresta(8,9)
gFW.addAresta(10,11)
gFW.addAresta(10,12)
gFW.addAresta(10,13)
gFW.addAresta(12,13)
cont, ids = gFW.componentesConectadas()
print('Quantidade de componentes conectadas: \n', cont)
print('Componentes conectadas: \n', ids)