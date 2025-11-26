
## 📄 Documentação do Sistema: Jogo da Velha (UNIFOR Edition)

### 1. Visão Geral do Projeto

O **Jogo da Velha (UNIFOR Edition)** é uma aplicação web simples e completa (Single Page Application) desenvolvida para demonstrar a lógica clássica do jogo em um ambiente digital, utilizando a identidade visual da Universidade de Fortaleza (UNIFOR). O projeto é totalmente autônomo, não dependendo de servidores externos ou bibliotecas complexas.

| Característica | Detalhe |
| :--- | :--- |
| **Nome** | Jogo da Velha UNIFOR |
| **Versão** | 1.0 |
| **Plataforma** | Web (HTML5, CSS3, JavaScript) |
| **Tipo** | Jogo para Dois Jogadores (Local) |
| **Tema** | Azul e Laranja Institucional da UNIFOR |

---

### 2. Arquitetura e Componentes Técnicos

O sistema é contido em um único arquivo HTML, com as três tecnologias essenciais (HTML, CSS e JavaScript) devidamente encapsuladas.

#### 2.1. Estrutura (HTML)

A estrutura define os elementos visuais do jogo:

* **Logo:** Utiliza uma *tag* `<img>` que carrega o logo oficial da UNIFOR a partir de um link externo (`https://upload.wikimedia.org/...`).
* **Status (`div#status`):** Exibe a vez do jogador atual ou o resultado final (Vitória/Empate).
* **Tabuleiro (`div#board`):** Um contêiner que utiliza **CSS Grid** para criar a grade $3 \times 3$.
* **Células (`div.cell`):** Nove divs que representam os espaços clicáveis do tabuleiro. Cada uma possui o atributo `data-index="n"` para mapeamento com a lógica JavaScript.
* **Botão (`button#restartBtn`):** Usado para resetar o jogo.

#### 2.2. Estilos (CSS)

O CSS é a parte que aplica o tema UNIFOR:

* **Paleta de Cores:**
    * `--unifor-blue`: Azul Institucional (`#003366`)
    * `--unifor-orange`: Laranja de Destaque (`#F58025`)
* **Background:** Aplica um `linear-gradient` com tons de azul escuro.
* **Marcações:** O jogador **X** usa a cor **Laranja UNIFOR** e o jogador **O** usa a cor **Azul UNIFOR**.
* **Filtro do Logo:** A propriedade `filter: brightness(0) invert(1)` é usada para transformar o logo, originalmente escuro, em **branco** para garantir a legibilidade contra o fundo azul escuro.

#### 2.3. Lógica (JavaScript)

O código JavaScript gerencia o estado e a funcionalidade do jogo.

| Variável/Array | Descrição |
| :--- | :--- |
| `gameActive` | **Boolean** que indica se o jogo pode receber novos cliques. |
| `currentPlayer` | **String** (`"X"` ou `"O"`) que indica o jogador atual. |
| `gameState` | **Array** de 9 posições (`["", "", ..., ""]`) que armazena o estado atual do tabuleiro. |
| `winningConditions` | **Array de Arrays** que lista todas as 8 combinações de índices que resultam em vitória (3 linhas, 3 colunas, 2 diagonais). |

| Função | Descrição |
| :--- | :--- |
| `handleCellClick()` | Função principal disparada pelo clique na célula. Verifica se o movimento é válido e chama as próximas etapas. |
| `handleCellPlayed()` | Atualiza o `gameState` e o conteúdo HTML da célula. |
| `handleResultValidation()` | **Verificação de Vitória/Empate.** Percorre o `winningConditions` para checar se algum jogador preencheu uma sequência. Se o tabuleiro estiver cheio e não houver vencedor, declara empate. |
| `handlePlayerChange()` | Alterna o `currentPlayer` de "X" para "O" ou vice-versa. |
| `handleRestartGame()` | Zera o `gameState`, limpa o tabuleiro visualmente e redefine o `currentPlayer` para "X". |

---

### 3. Implementação e Execução

O sistema é projetado para ser executado diretamente no navegador.

#### 3.1. Pré-requisitos
* Um navegador web moderno (Chrome, Firefox, Edge, Safari).
* Conexão com a internet (necessária apenas para carregar o logo da UNIFOR).

#### 3.2. Instruções de Instalação/Execução
1.  Salve o código HTML em um arquivo (ex: `jogo-unifor.html`).
2.  Abra o arquivo diretamente em qualquer navegador web.

O jogo será carregado instantaneamente, pronto para dois jogadores.