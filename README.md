# Web Scraper e API para Notebooks

Este projeto cria um web scraper para coletar informações de notebooks do site https://webscraper.io/test-sites/e-commerce/static/computers/laptops, organizando e disponibilizando os dados por meio de uma API FastAPI.

## 🚀 Funcionalidades

- Extrai dados de notebooks do site especificado
- Filtra notebooks por marca
- Organiza notebooks por preço (do mais barato ao mais caro)
- Oferece API REST flexível para acesso aos dados
- Implementa tratamento de erros
- **Novo: Suporte a filtro de marca de notebook**

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

## 🌐 Endpoints da API

### Documentação da API

- **Endpoint**: `http://127.0.0.1:8000/docs`
- **Descrição**: Interface Swagger UI para documentação interativa da API

### Listar Notebooks

- **Endpoint**: `GET http://127.0.0.1:8000/notebooks`
- **Descrição**: Retorna lista de notebooks
- **Parâmetros**:
  - `brand` (opcional): Filtro por marca do notebook
- **Comportamento Padrão**: Retorna notebooks Lenovo ordenados por preço

## 🧪 Exemplos de Uso

### Buscar Notebooks Lenovo (Padrão)

```bash
curl http://127.0.0.1:8000/notebooks
```

### Buscar Notebooks por Marca Específica

```bash
# Exemplo: Buscar notebooks Dell
curl "http://127.0.0.1:8000/notebooks?brand=Dell"
```

### Testando com Python Requests

```bash
# Busca padrão
python -c "import requests; print(requests.get('http://127.0.0.1:8000/notebooks').json())"
# Busca com filtro de marca
python -c "import requests; print(requests.get('http://127.0.0.1:8000/notebooks?brand=Acer').json())"
```

## 📝 Observações

- Sem filtro de marca, a API retorna notebooks Lenovo
- O filtro de marca é case-insensitive
- Notebooks são sempre ordenados do mais barato para o mais caro

---

**Desenvolvido por [Henrique Nascimento](https://www.linkedin.com/in/henriquen-dev/)**🖥️
