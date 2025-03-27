from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from scraper import get_lenovo_products_sorted

app = FastAPI(title="API de Notebooks Lenovo",
              description="API que retorna notebooks filtrados por marca. Por padrão, sem filtro, retorna notebooks Lenovo ordenados do mais barato para o mais caro.",
              version="1.0.0")

class Product(BaseModel):
    id: int
    title: str
    price: Optional[float]
    description: str
    reviews: int
    image: Optional[str]
    details_url: Optional[str]

class NotebooksResponse(BaseModel):
    total_count: int
    products: List[Product]

@app.get("/notebooks", response_model=NotebooksResponse)
async def get_notebooks(brand: Optional[str] = Query(None, description="Filtro de marca do notebook")):
    """
    Endpoint que retorna a lista de notebooks ordenados do mais barato para o mais caro.
    Se nenhuma marca for especificada, retorna notebooks Lenovo por padrão.
    """
    products, total_count = await get_lenovo_products_sorted(brand)
    if not products:
        raise HTTPException(status_code=404, detail="Nenhum produto encontrado.")
    return {
        "total_count": total_count,
        "products": products
    }