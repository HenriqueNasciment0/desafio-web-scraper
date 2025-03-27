from fastapi import FastAPI, HTTPException
from scraper import get_lenovo_products_sorted
from typing import List

app = FastAPI(title="API de Notebooks Lenovo",
              description="API que retorna os notebooks Lenovo extraídos do site",
              version="1.0.0")

@app.get("/notebooks", response_model=List[dict])
def get_notebooks():
    """
    Endpoint que retorna a lista de notebooks Lenovo ordenados do mais barato para o mais caro.
    """
    products = get_lenovo_products_sorted()
    if not products:
        raise HTTPException(status_code=404, detail="Nenhum produto encontrado.")
    return products

