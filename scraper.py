import requests
from bs4 import BeautifulSoup

BASE_URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="

def fetch_html(url):

    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.text
    except requests.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return None

def get_max_page_number(html):

    soup = BeautifulSoup(html, 'html.parser')
    pagination_div = soup.find("div", id="static-pagination")
    max_page = 1
    if pagination_div:
        for a in pagination_div.find_all("a", class_="page-link"):
            text = a.get_text(strip=True)
            if text.isdigit():
                num = int(text)
                if num > max_page:
                    max_page = num
    return max_page

def parse_products(html, brand_filter=None):

    soup = BeautifulSoup(html, 'html.parser')
    products = []
    page_count = 0
    
    product_cards = soup.find_all("div", class_="card thumbnail")
    
    for card in product_cards:
        caption = card.find("div", class_="caption")
        if not caption:
            continue
        
        title_tag = caption.find("a", class_="title")
        if not title_tag:
            continue
        
        full_title = title_tag.get("title") or title_tag.get_text(strip=True)
        
        if brand_filter is None:
            if "Lenovo" not in full_title:
                continue
        else:
            if brand_filter.lower() not in full_title.lower():
                continue
        
        page_count += 1
        price_tag = caption.find("h4", class_="price")
        try:
            price = float(price_tag.get_text(strip=True).replace("$", "")) if price_tag else None
        except ValueError:
            price = None
        
        description_tag = caption.find("p", class_="description")
        description = description_tag.get_text(strip=True) if description_tag else ""
        
        image_tag = card.find("img", class_="img-responsive")
        image = image_tag["src"] if image_tag and image_tag.has_attr("src") else None
        
        ratings_div = card.find("div", class_="ratings")
        review_count = 0
        if ratings_div:
            review_tag = ratings_div.find("p", class_="review-count")
            if review_tag:
                review_text = review_tag.get_text(strip=True)
                review_count = int(review_text.split()[0]) if review_text.split()[0].isdigit() else 0
        
        details_url = title_tag["href"] if title_tag.has_attr("href") else None
        id_item = int(title_tag["href"].split("/")[-1]) if title_tag.has_attr("href") else None

        
        product = {
            "id": id_item,
            "title": full_title,
            "price": price,
            "description": description,
            "reviews": review_count,
            "image": image,
            "details_url": details_url
        }
        products.append(product)
    
    return products, page_count


def get_lenovo_products_sorted(brand_filter=None):  

    first_page_html = fetch_html(BASE_URL + "1")
    if first_page_html is None:
        return []
    
    max_page = get_max_page_number(first_page_html)
    print(f"Número máximo de páginas encontrado: {max_page}")
    
    all_products = []
    total_count = 0

    for page in range(1, max_page + 1):
        url = BASE_URL + str(page)
        print(f"Consultando: {url}")
        html = fetch_html(url)
        if html is None:
            continue
        products, page_count = parse_products(html, brand_filter)
        all_products.extend(products)
        total_count += page_count
    

    sorted_products = sorted(all_products, key=lambda x: x["price"] if x["price"] is not None else float('inf'))
    return sorted_products, total_count

if __name__ == "__main__":
    products = get_lenovo_products_sorted()
    for p in products:
        print(p)
