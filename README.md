# 3 Desafios de Amigo – Python

Este repositório contém três exercícios independentes desenvolvidos em Python com foco em fundamentos de programação: lógica, funções, estruturas de dados, controle de fluxo e simulações simples.

## 1. Desafio: Pontuação de Cartas

Arquivo: `desafio1-calcularPontuacaoCartas.py`

### Descrição
Script que calcula a soma dos valores de uma mão de cartas e exibe o resultado.

### Funcionalidades
- Lista de valores representando cartas.
- Função que soma a lista e atualiza uma variável global de pontuação.
- Impressão do resultado final no console.

### Conceitos trabalhados
- Listas
- Funções
- Variáveis globais
- Soma com `sum()`
- Saída no console

## 2. Desafio: Rolagem de Dados (RPG)

Arquivo: `desafio2-rolagemDados.py`

### Descrição
Função que simula rolagens de um dado de X lados Y vezes.

### Funcionalidades
- Uso da biblioteca `random`.
- Geração de números pseudoaleatórios.
- Retorno de lista com todas as rolagens.

### Conceitos trabalhados
- Importação de módulos
- Loops
- `random.randint()`
- Construção dinâmica de listas

## 3. Desafio: Batalha por Turnos

Arquivo: `desafio3-batalhaPorTurnos.py`

### Descrição
Simulação de combate por turnos entre dois personagens, com ataques normais, especiais e controle de cooldown.

### Funcionalidades
- Modelagem de personagens com dicionários.
- Função que executa um turno considerando ataque, defesa e cooldown.
- Loop que alterna ataques até um personagem ser derrotado.
- Exibição de logs e resultado final.

### Conceitos trabalhados
- Dicionários
- Condicionais
- Estruturas de repetição
- Cálculo de dano
- Atualização de estado (vida, cooldown)

## Estrutura do Repositório
```
3-desafios-de-amigo/
├── desafio1-calcularPontuacaoCartas.py
├── desafio2-rolagemDados.py
└── desafio3-batalhaPorTurnos.py
```

## Como Executar
1. Instale Python 3.x
2. Clone o repositório:
```
git clone https://github.com/Gustavo-Barcellos/3-desafios-de-amigo
```
3. Execute qualquer arquivo:
```
python nome-do-arquivo.py
```

## Objetivo do Projeto
Reforçar fundamentos da programação antes de avançar para projetos mais complexos, consolidando lógica, simulação, estruturação de scripts e práticas básicas da linguagem.
