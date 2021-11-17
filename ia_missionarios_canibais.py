from queue import Queue
import numpy as np

class Estado():

  movimentos = [[1, 0], [2, 0], [0, 1], [0, 2], [1, 1]]

  # estado[0] -> quant de missionarios
  # estado[1] -> quant de canibais
  # estado[2] -> lado em que o barco se encontra
  def __init__(self, estado, pai, acoes, nivel):
    self.estado = estado
    self.pai = pai
    self.acoes = acoes
    self.nivel = nivel
  
  # Checa se o estado é um estado final
  def estado_final(self):
    if self.estado == [0, 0, -1]:
        return True
    return False
  
  # Checa se é um estado dentro dos limites válidos do problema
  def estado_valido(self):
    missionarios = self.estado[0]
    canibais = self.estado[1]
    barco = self.estado[2]

    if missionarios < 0 or missionarios > 3:
      return False
    if canibais < 0 or canibais > 3:
      return False
    if barco != -1 and barco != 1:
      return False
    return True
  
  # Checa se é um estado em que se perde o jogo
  def estado_morto(self):
    missionarios = self.estado[0]
    canibais = self.estado[1]
    if missionarios < canibais  and missionarios > 0:
      return True
    if (3 - missionarios) < (3 - canibais) and (3 - missionarios) > 0:
      return True

  # Gerar os movimentos possíveis em relação ao estado atual
  def gerar_movimentos(self):
    movimento = []
    nivel = self.nivel + 1
    barco = (-1) * self.estado[2]

    for i in range(5):
      novo_estado = self.estado.copy()
      novo_estado[0] += barco * self.movimentos[i][0]
      novo_estado[1] += barco * self.movimentos[i][1]
      novo_estado[2] = barco
      acoes = [self.movimentos[i][0], self.movimentos[i][1]]
      estado = Estado(novo_estado, self, acoes, nivel)
      if self.movimentos[i][0] + self.movimentos[i][1] > 0 and self.movimentos[i][0] + self.movimentos[i][1] < 3:
         movimento.append(estado)
    return movimento

  # Pegar as ações realizadas para se chegar na solução   
  def eh_solucao(self):
    solucao = []
    solucao.append(self.acoes)
    path = self
    while path.pai != None:      
      path = path.pai
      solucao.append(path.acoes)

    solucao = solucao[:-1]
    solucao.reverse()
    return solucao

  # Imprimir as viagens feitas para se chegar na solução
  def printar_solucao(self):
    passos = []
    passo = "\nAssim, todos os missionários e canibais foram transportados para o outro lado!"
    passos.append(passo)
    path = self
    while path.pai != None:
      if path.estado[2] == -1:
        passo = "[ " + (str(path.nivel) + "º viagem ] movendo " + str(path.acoes[0]) + " missionário(s) e " + str(path.acoes[1]) + " canibal(is) para o lado direito...")
      else:
        passo = "[ " + (str(path.nivel) + "º viagem ] movendo " + str(path.acoes[0]) + " missionário(s) e " + str(path.acoes[1]) + " canibal(is) para o lado esquerdo...")
      
      passos.append(passo)
      path = path.pai
    passos.reverse()
    return passos

def bfs(estado_inicial):

  raiz = Estado(estado_inicial, None, None, 0)
  
  # Checa se a raiz é a solução
  if raiz.estado_final():
    return raiz.eh_solucao()
  
  q = Queue()
  q.put(raiz)

  visitados = []
  
  # Loop para percorrer os estados
  while not(q.empty()):
    no = q.get()

    visitados.append(no.estado)
    movimentos = no.gerar_movimentos()

    if not no.estado_morto():

      for movimento in movimentos:

        # Checa, sendo não morto, válido e não visitado, se o estado é uma solução
        if movimento.estado_valido():

          if movimento.estado not in visitados:

            if movimento.estado_final():
              return movimento.printar_solucao()

            # Caso não seja, coloca na fila para gerar os sucessores
            else:
              q.put(movimento)
              visitados.append(movimento.estado)
  
  return

estado_inicial = [3, 3, 1]

solucao = bfs(estado_inicial)

print("A solução encontrada para o problema foi:\n")
for i in range(len(solucao)):
  print(solucao[i])



