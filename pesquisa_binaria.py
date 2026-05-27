# Biblioteca importada para cronometrar o tempo de execução de cada algoritmo
import time

# Ferramentas importadas para descrever tipos
from typing import Callable, List, Optional


# DEFINIÇÃO DAS FERRAMENTAS ----------------------------------------------

# minha_lista: List[int] -> Significa "uma lista que contém números inteiros"
# item_procurado: int    -> Significa "um número inteiro"
# -> Optional[int]       -> Significa "esta função retorna um inteiro OU None"

# Função para executar a pesquisa simples
def pesquisa_simples(minha_lista: List[int], item_procurado: int) -> Optional[int]:
    for i in range(len(minha_lista)):
        if minha_lista[i] == item_procurado:
            return i 
    return None  # Se não encontrar, retorna None

# Função para executar a pesquisa binária
def pesquisa_binaria(minha_lista: List[int], item_procurado: int) -> Optional[int]:
    baixo: int = 0
    alto: int = len(minha_lista) - 1

    while baixo <= alto:
        meio: int = (baixo + alto)//2
        chute: int = minha_lista[meio]

        if chute == item_procurado:
            return meio
        
        if chute > item_procurado:
            alto = meio - 1 
        else:
            baixo = meio + 1 
    
    return None


#algoritmo é uma FUNÇÃO (Callable) que recebe como argumento uma lista de inteiros e um inteiro, e que nos devolve um inteiro ou None"
def medir_tempo(algoritmo: Callable[[List[int], int], Optional[int]], 
    minha_lista: List[int], 
    item_procurado: int) -> None:
    # -> None significa "esta função não tem 'return', ela só executa ações"

    inicio = time.perf_counter()
    resultado = algoritmo(minha_lista, item_procurado)
    fim = time.perf_counter()
    tempo_gasto = fim - inicio

    if resultado is not None:
        print(f"Item encontrado no índice: {resultado}")
    else:
        print("Item não encontrado.")

    print(f"Tempo de execução {algoritmo.__name__}: {tempo_gasto:.6f} segundos")


# EXECUÇÃO DOS TESTES (ORQUESTRADOR) ----------------------------------------------
if __name__ == "__main__":
    # Criação da lista
    minha_lista = list(range(10000000))

    item_procurado = int(input("Digite um número entre 1 - 9999999 para ser procurado usando cada um dos algoritmos de busca: "))
    print('--------------------------------------------------')
    print("Buscando usando pesquisa simples...")
    medir_tempo(pesquisa_simples, minha_lista,item_procurado)
    print('--------------------------------------------------')
    print("Buscando usando pesquisa binária...")
    medir_tempo(pesquisa_binaria, minha_lista,item_procurado)