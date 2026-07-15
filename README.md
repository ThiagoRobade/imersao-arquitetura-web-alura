# Alura Album - Copa do Mundo Tech

O **Alura Album** é um tributo digital e interativo à história e evolução do desenvolvimento de software, reunindo mentes brilhantes nacionais e internacionais que moldaram e continuam moldando o futuro da tecnologia. 

Este projeto simula um álbum de figurinhas físico em formato de livro digital (flipbook), onde cada página é dedicada a uma categoria da tecnologia, e as figurinhas são carregadas e "coladas" dinamicamente a partir de uma API.

---

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é criar uma experiência de usuário imersiva, moderna e visualmente premium para colecionar figurinhas de grandes nomes da tecnologia, abrangendo:
* **Pioneiros da Inteligência Artificial** (Alan Turing, Geoffrey Hinton, etc.)
* **Arquitetos da Simplicidade (Python)** (Guido van Rossum, Tim Peters, etc.)
* **Arquitetos de Bancos de Dados** (Edgar F. Codd, Michael Widenius, etc.)
* **Arquitetos de Sistemas Operacionais** (Linus Torvalds, Dennis Ritchie, etc.)
* **Celebridades Tech do Brasil** (Paulo Silveira, Rafaela Ballerini, Gustavo Guanabara, entre outros)

---

## 🛠️ Arquivos e Funcionalidades

O projeto é construído sobre uma arquitetura Web simples de três arquivos base na raiz, cada um responsável por uma camada da aplicação:

### 1. `index.html` (Estrutura e Conteúdo)
* **Função:** Organiza a marcação estrutural e os blocos de conteúdo da aplicação.
* **Componentes principais:**
  * **Capa e Contracapa:** Páginas com estilo diferenciado e elementos holográficos decorativos.
  * **Páginas de Categorias:** Telas contendo uma grade de colecionáveis (*slots*) numerados (`#01` a `#30`), onde os nomes e papéis de cada personalidade já vêm predefinidos.
  * **Painéis de Interface:** Botões de navegação lateral (anterior e próximo) e botão de controle de som.
  * **Dependências:** Importa a folha de estilo (`style.css`), fontes do Google Fonts, a biblioteca externa de manipulação de páginas (`page-flip.browser.min.js`) via CDN, e o script de comportamento (`app.js`).

### 2. `style.css` (Aparência, Layout e Animações)
* **Função:** Fornece a identidade visual futurista, o design responsivo e efeitos gráficos avançados para dar vida ao álbum.
* **Recursos de Design:**
  * **Paleta de Cores Premium:** Tons de azul escuro espacial combinados com detalhes brilhantes em ciano e branco neve.
  * **Simulação Tridimensional:** Sombreamento gradual dinâmico nas bordas e no centro das páginas que acompanha o folheamento, simulando a profundidade do papel e da lombada física.
  * **Efeitos de Micro-animações:**
    * Efeito de interferência digital (*glitch*) nos títulos da capa.
    * Animação tridimensional com anéis giratórios para a esfera tecnológica central.
    * Mini-cards flutuantes com animação de levitação na capa.
    * Efeito de colagem animada (`sticker-aparecer`) para dar impacto visual ao preenchimento de figurinhas novas.

### 3. `app.js` (Interação, Integração com API e Efeitos Sonoros)
* **Função:** Gerencia toda a lógica de negócios, o comportamento dinâmico da interface e a comunicação externa.
* **Principais Mecanismos:**
  * **Integração com Backend (API):** Consome de forma assíncrona o endpoint da API (`http://localhost:8000/figurinhas`) para recuperar o banco de dados de figurinhas disponíveis. Assim que as imagens carregam com sucesso, altera a classe dos slots no HTML para renderizar a figurinha "colada" com sua respectiva foto.
  * **Motor do Flipbook:** Inicializa a biblioteca `St.PageFlip` configurando dimensões dinâmicas, limites e o tempo de transição (800ms).
  * **Gesto de Arraste Customizado:** Substitui o comportamento padrão de clique da biblioteca por um sistema robusto que diferencia cliques comuns de arrastes intencionais por mouse ou toque em dispositivos móveis.
  * **Efeitos de Áudio (Web Audio API):** Gera e sintetiza matematicamente um som realista de vento e atrito de papel folheando (utilizando ruído branco modulado por frequências dinâmicas) direto no navegador, sem a necessidade de arquivos de áudio externos pesados.
  * **Controles do Usuário:** Habilita navegação tanto por botões da tela quanto por setas do teclado (`ArrowLeft` e `ArrowRight`), além de gerenciar o estado mutado/desmutado do app.

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter um servidor backend rodando na porta `8000` (ex: rodando a API do FastAPI com `uvicorn main:app --reload`).
2. Abra o arquivo `index.html` em seu navegador. Recomendamos a utilização de um servidor local simples como a extensão Live Server do VS Code ou executando:
   ```bash
   # Utilizando Python
   python -m http.server 3000
   
   # Ou utilizando Node.js
   npx serve .
   ```
3. Acesse `http://localhost:3000` no seu navegador para ver o álbum interativo funcionando e consumindo a API.
