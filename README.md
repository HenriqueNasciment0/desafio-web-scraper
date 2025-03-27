# Web Scraper e API para Notebooks Lenovo

Este projeto cria um web scraper para coletar informações de notebooks Lenovo do site https://webscraper.io/test-sites/e-commerce/static/computers/laptops, organizando e disponibilizando os dados por meio de uma API FastAPI.

## 🚀 Funcionalidades

- Extrai dados de notebooks do site especificado
- Filtra e organiza notebooks Lenovo
- Classifica produtos por preço (do mais barato ao mais caro)
- Oferece API REST para acesso aos dados
- Implementa tratamento de erros

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.13.2
- **Requisições HTTP**: Biblioteca Requests
- **Parsing HTML**: BeautifulSoup4
- **Framework API**: FastAPI
- **Servidor**: Uvicorn (ASGI)

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

## 🔧 Instalação e Configuração

### Clonando o Repositório

```bash
# Opção SSH
git clone git@github.com:HenriqueNasciment0/desafio-web-scraper.git

# Opção HTTPS
git clone https://github.com/HenriqueNasciment0/desafio-web-scraper.git

# Navegue para o diretório do projeto
cd desafio-web-scraper
```

### Configurando Ambiente Virtual

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Linux/MacOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Instalando Dependências

```bash
pip install -r requirements.txt
```

## 🚀 Executando o Projeto

### Iniciando o Web Scraper

```bash
# Execute o script de scraping
python scraper.py
```

### Iniciando a API

```bash
# Inicie o servidor FastAPI
uvicorn api:app --reload
```

## 🌐 Endpoint da API

- **Listar Notebooks**: `GET http://127.0.0.1:8000/notebooks`
  - Retorna lista de notebooks Lenovo
  - Ordenados por preço

## 🧪 Formas de Testar

### Via Navegador

- Acesse `http://127.0.0.1:8000/notebooks`

### Via Terminal

```bash
# Usando curl
curl http://127.0.0.1:8000/notebooks

# Usando Python Requests
python -c "import requests; print(requests.get('http://127.0.0.1:8000/notebooks').json())"
```

---

**Desenvolvido por [Henrique Nascimento](https://www.linkedin.com/in/henriquen-dev/)**🖥️
