# Implementação de Algoritmos de Busca: Simples vs. Binária

Lendo o livro *"Entendendo Algoritmos: Um Guia Ilustrado para Programadores e Outros Curiosos"*, do engenheiro de software Aditya Y. Bhargava, decidi implementar os algoritmos apresentados para consolidar o conhecimento prático de complexidade de tempo.

Neste projeto, o objetivo foi utilizar uma arquitetura limpa, modular e tipada em Python para comparar duas abordagens de busca, além de construir um ecossistema de testes automatizado.

---

## Os Algoritmos Implementados

* **Pesquisa Simples (Busca Linear):** Percorre a estrutura de dados índice por índice, de forma sequencial, até encontrar o `item_procurado`. Possui uma complexidade de tempo de **$O(n)$**.
* **Pesquisa Binária:** Utiliza a estratégia de *divisão e conquista*. O algoritmo divide a lista ordenada ao meio e faz sucessivas reduções do espaço de busca utilizando limites inferiores (`baixo`) e superiores (`alto`). Possui uma complexidade de tempo de **$O(\log n)$**.

---

## Arquitetura do Código

Para garantir boas práticas de Engenharia de Software, o script foi desenhado seguindo três pilares fundamentais:

1. **Separação de Responsabilidades (SRP):** As funções de busca cuidam estritamente da lógica matemática de busca, sem interferência de logs ou cronômetros.
2. **Injeção de Dependência:** Foi criada uma função gerenciadora chamada `medir_tempo` que recebe o algoritmo dinamicamente como parâmetro (`Callable`), centralizando a cronometragem através da biblioteca `time.perf_counter()`.
3. **Tipagem Estática (*Type Hints*):** Todo o código foi documentado com anotações de tipo para garantir segurança e legibilidade do fluxo de dados.

---

## Comparativo de Desempenho (Resultados Práticos)

Abaixo está o resultado empírico coletado diretamente no terminal ao buscar o pior cenário possível (o último elemento) em uma lista ordenada de **10.000.000 (10 milhões)** de elementos:

```text
Buscando usando pesquisa simples...
Item encontrado no índice: 9999999
Tempo de execução pesquisa_simples: 0.160076 segundos
--------------------------------------------------
Buscando usando pesquisa binária...
Item encontrado no índice: 9999999
Tempo de execução pesquisa_binaria: 0.000011 segundos
