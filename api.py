from fastapi import FastAPI, HTTPException, Query
from scraper import get_lenovo_products_sorted
from typing import List, Optional

app = FastAPI(title="API de Notebooks Lenovo",
              description="API que retorna notebooks filtrados por marca. Por padrão, sem filtro, retorna notebooks Lenovo ordenados do mais barato para o mais caro.",
              version="1.0.0")

@app.get("/notebooks", response_model=List[dict])
def get_notebooks(brand: Optional[str] = Query(None, description="Filtro de marca do notebook")):
    """
    Endpoint que retorna a lista de notebooks ordenados do mais barato para o mais caro.
    Se nenhuma marca for especificada, retorna notebooks Lenovo por padrão.
    """
    products = get_lenovo_products_sorted(brand)
    if not products:
        raise HTTPException(status_code=404, detail="Nenhum produto encontrado.")
    return products

