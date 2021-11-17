<center>

![logo](logo.png)

## UNIVERSIDADE FEDERAL DE ALAGOAS - UFAL 
## INSTITUTO DE COMPUTAÇÃO - IC
### Engenharia de Computação 

---
# Problema dos Missionários e Canibais

</center>

> ### Três missionários e três canibais estão em um lado do rio, juntamente com um barco que pode conter uma ou duas pessoas. Descubra um meio de fazer todos atravessarem o rio, sem deixar que um grupo de missionários de um lado fique em número menor que o número de canibais nesse lado do rio. Esse problema é famoso em IA, porque foi assunto do primeiro artigo que abordou a formulação de problemas a partir de um ponto de vista analítico (Amarel, 1968). 
> ### Implemente e resolva o problema de forma ótima, utilizando um algoritmo de busca apropriado. É boa idéia verificar a existência de estados repetidos?

<br />

**Para o problema dos Missionários e Canibais, foi utilizado o algoritmo de busca BFS (Breadth-First Search - Busca em Largura).** <br />
**Foi verificada a existência de estados repetidos na lista de estados visitados. Assim, garante que o algoritmo não entre em loop ou explore estados já explorados anteriormente.**

<br />

- O arquivo <code>IA_Missionários_e_Canibais.ipynb</code> contém o acesso da implementação no Google Colab.

- O arquivo <code>ia_missionarios_canibais.py</code> contém o mesmo algoritmo em um arquivo <code>.py</code>. Para executar, basta digitar, após fazer o download do arquivo:

```
py ia_missionarios_canibais.py
```

O resultado da execução é:

```
A solução encontrada para o problema foi:

[ 1º viagem ] movendo 0 missionário(s) e 2 canibal(is) para o lado direito...
[ 2º viagem ] movendo 0 missionário(s) e 1 canibal(is) para o lado esquerdo...
[ 3º viagem ] movendo 0 missionário(s) e 2 canibal(is) para o lado direito...
[ 4º viagem ] movendo 0 missionário(s) e 1 canibal(is) para o lado esquerdo...
[ 5º viagem ] movendo 2 missionário(s) e 0 canibal(is) para o lado direito...
[ 6º viagem ] movendo 1 missionário(s) e 1 canibal(is) para o lado esquerdo...
[ 7º viagem ] movendo 2 missionário(s) e 0 canibal(is) para o lado direito...
[ 8º viagem ] movendo 0 missionário(s) e 1 canibal(is) para o lado esquerdo...
[ 9º viagem ] movendo 0 missionário(s) e 2 canibal(is) para o lado direito...
[ 10º viagem ] movendo 1 missionário(s) e 0 canibal(is) para o lado esquerdo...
[ 11º viagem ] movendo 1 missionário(s) e 1 canibal(is) para o lado direito...

Assim, todos os missionários e canibais foram transportados para o outro lado!
```