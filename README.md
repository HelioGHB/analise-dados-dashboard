# Dashboard de Análise de Dados Interativo 📊

Um aplicativo web interativo e de página única desenvolvido em **Python** utilizando a biblioteca **Streamlit**. O objetivo principal deste projeto é permitir que qualquer usuário faça o upload de uma base de dados (em formato Excel ou CSV) e obtenha instantaneamente uma visão analítica com resumos estatísticos e gráficos customizáveis.

---

## 🚀 Funcionalidades

- **Upload de Arquivos Dinâmico:** Suporte nativo para arquivos nos formatos `.csv` e `.xlsx` (Excel).
- **Visualização de Dados:** Exibição interativa das primeiras linhas da tabela para validação rápida da estrutura dos dados.
- **Resumo Estatístico Automatizado:** Geração instantânea de métricas descritivas essenciais (média, mediana, valores mínimos/máximos, desvio padrão) com apenas um clique.
- **Gráficos Interativos (Plotly):** Interface interativa que permite ao usuário escolher os eixos (X e Y) e alternar dinamicamente entre diferentes tipos de visualização:
  - Gráfico de Barras
  - Gráfico de Linhas
  - Gráfico de Dispersão (Scatter Plot)

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes ferramentas do ecossistema Python:

* [Streamlit](https://streamlit.io/) - Framework para criação da interface web e reatividade do app.
* [Pandas](https://pandas.pydata.org/) - Manipulação, tratamento e análise estruturada dos dados.
* [Plotly Express](https://plotly.com/python/) - Criação de gráficos interativos e responsivos.

---

## 🔧 Como Executar o Projeto Localmente

### Pré-requisitos
Antes de começar, certifique-se de ter o **Python 3.8+** instalado em sua máquina.

### Passos para execução:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/analise-dados-dashboard.git](https://github.com/SEU_USUARIO/analise-dados-dashboard.git)
   cd analise-dados-dashboard

2. **Crie e ative o ambiente virtual:**

No macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate
No Windows:

python -m venv .venv
.venv\Scripts\activate

3. **Instale as dependências necessárias:**

pip install -r requirements.txt

4. **Execute a aplicação:**

streamlit run app.py

5. **O dashboard abrirá automaticamente no seu navegador padrão (ou utilize o endereço local http://localhost:8501).**

📁 **Estrutura do Repositório**
O projeto está organizado da seguinte forma:

Plaintext
├── app.py                  # Código principal da aplicação Streamlit
├── requirements.txt        # Dependências e bibliotecas do projeto
├── .gitignore              # Arquivos e pastas ignorados pelo Git (ex: .venv)
└── README.md               # Documentação do projeto

📸 *Demonstração*
(Dica: Quando o seu dashboard estiver rodando na tela, tire um print bonito dele, salve a imagem na raiz do projeto com o nome dashboard.png e descomente a linha abaixo para exibi-la no GitHub!)

Desenvolvido por Seu Nome


### Por que adicionar a "Estrutura do Repositório"?
Isso ajuda muito os recrutadores ou outros desenvolvedores a entenderem o design do seu projeto num piscar de olhos, mostrando que você sabe organizar um ambiente de desenvolvimento limpo (com `.gitignore` e `requirements.txt`). 

Depois de colar esse final no seu arquivo e trocar os campos `SEU_USUARIO` e `Seu Nome`, é só dar o `git commit` e mandar bala!