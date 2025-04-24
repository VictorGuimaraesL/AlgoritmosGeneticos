# Algoritmo Genético para o Problema da Mochila (Knapsack)

Um algoritmo genético em Python que resolve o **problema da mochila binária**, otimizando a seleção de itens para maximizar o lucro sem ultrapassar a capacidade máxima.

## 📌 Contexto do Projeto
- **Problema**: Dada uma mochila com capacidade limitada e um conjunto de itens (cada um com peso e lucro), selecionar quais itens levar sem exceder o peso máximo, maximizando o lucro.
- **Solução**: Algoritmo genético com:
  - **Seleção por roleta** (roulette wheel selection).
  - **Crossover** em ponto único.
  - **Mutação** bit a bit.
- **Dataset**: Dados do arquivo `P08-cwp.csv` (24 itens, capacidade = 6.404.180).

## 🛠️ Tecnologias
- Python 3.x
- Bibliotecas: `pandas`, `numpy`

▶️ Como Executar

Instale as dependências:

    pip install pandas numpy

Execute o algoritmo:
    
    python main.py

📊 Saída Esperada

O programa imprimirá:

    A lista de itens (peso e lucro).

    A melhor solução encontrada (cromossomo binário, onde 1 = item selecionado).

    Peso total e lucro da solução ótima.

Exemplo:

    Best solution: [1, 0, 1, ..., 0]  # Cromossomo da melhor solução
    Total Weight: 6.200.000
    Total Profit: 12.540.000

⚙️ Parâmetros do Algoritmo

| Parâmetro  | Valor Padrão | Descrição |
| ------------- | ------------- | ------------- |
| Tamanho da população |	10	| Número de indivíduos por geração | 
|  Taxa de mutação | 0.01 (1%) | Probabilidade de mutação por gene |  
|  Taxa de crossover | 0.97 (97%) | Probabilidade de crossover |
| Elitismo | 2 | Melhores indivíduos preservados |
| Gerações máximas | 100 | Critério de parada |
  
📂 Estrutura do Código

|Arquivo | Função |
| ------------- | ------------- |
| main.py	| Configura e executa o algoritmo |
| genetic_algorithm.py	| Lógica do algoritmo genético |
| individual.py	| Representação de um indivíduo |
| population.py	| Gerenciamento da população |

📝 Melhorias Futuras

    Adicionar visualização da convergência do algoritmo.

    Testar outros métodos de seleção (ex: torneio).

    Paralelizar avaliação da população.

Nota: Este projeto foi desenvolvido como parte de estudos em Engenharia de Automação. Para dúvidas, entre em contato: victorguimaraes980@gmail.com.
