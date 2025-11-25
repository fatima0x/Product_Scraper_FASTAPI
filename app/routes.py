from fastapi import APIRouter
from scraper.static_scraper import scrape_static
from scraper.selenium_scraper import scrape_with_selenium
from database import SessionLocal
from models import Product



router = APIRouter()

product_urls = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
    
]

# ---------------------------
# API ROUTE 1 – SCRAPE DATA
# ---------------------------
@router.post("/scrape")
def run_scraper():
    db = SessionLocal()
    # ----------------------------------------
    # DELETE OLD DATA BEFORE NEW SCRAPE
    # ----------------------------------------
    db.query(Product).delete()
    db.commit()
    results = []

    for url in product_urls:
        product = scrape_static(url)
        if not product:
            product = scrape_with_selenium(url)

        # Insert into DB
        db_product = Product(
            title=product["Title"],
            price=product["Price"],
            availability=product["Availability"],
            category=product["Category"],
            rating=product["Rating"],
            product_url=product["Product URL"]
        )
        db.add(db_product)
        results.append(product)

    db.commit()
    db.close()
    
    import os
    import pandas as pd
    os.makedirs("output", exist_ok=True)
    df = pd.DataFrame(results)
    df.to_csv("output/products.csv", index=False)

    return {"message": "Scraping complete!", "items": results}

    return {"message": "Scraping complete!", "items": results}



# ---------------------------
# API ROUTE 2 – VIEW PRODUCTS
# ---------------------------
@router.get("/products")
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products
