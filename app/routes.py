from fastapi import APIRouter, Depends
from scraper.static_scraper import scrape_static
from scraper.selenium_scraper import scrape_with_selenium
from database import SessionLocal
from models import Product
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session


from database import get_db

from fastapi.responses import FileResponse
import os



router = APIRouter()

# -----------------------------
# NEW: Model for user URLs
# -----------------------------
class URLList(BaseModel):
    urls: List[str]


# -----------------------------
# NEW: Custom scraping endpoint
# -----------------------------
@router.post("/scrape_custom")
def scrape_custom(data: URLList, db: Session = Depends(get_db)):
    results = []

    for url in data.urls:
        scraped = scrape_static(url)  # get one product dict

        if scraped:
            # Insert into database
            db_product = Product(
                title=scraped["Title"],
                price=scraped["Price"],
                availability=scraped["Availability"],
                category=scraped["Category"],
                rating=scraped["Rating"],
                product_url=scraped["Product URL"]
            )
            db.add(db_product)
            db.commit()
            db.refresh(db_product)

            results.append(scraped)

    # Return scraped data to user
    return {"message": "Scraping done!", "results": results}


@router.get("/download")
def download_csv():
    file_path = os.path.join("output", "products.csv")

    if not os.path.exists(file_path):
        return {"error": "CSV file not found. Run /scrape first."}

    return FileResponse(
        path=file_path,
        media_type="text/csv",
        filename="products.csv"
    )


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




# ---------------------------
# API ROUTE 2 – VIEW PRODUCTS
# ---------------------------
@router.get("/products")
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products
