import requests
from bs4 import BeautifulSoup

def scrape_static(url):
    response = requests.get(url, timeout=5)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").text.strip()
    price = soup.find("p", class_="price_color").text.strip()
    availability = soup.find("p", class_="instock availability").text.strip()
    category = soup.find("ul", class_="breadcrumb").find_all("li")[2].text.strip()
    rating = soup.find("p", class_="star-rating")["class"][1]

    return {
        "Title": title,
        "Price": price,
        "Availability": availability,
        "Category": category,
        "Rating": rating,
        "Product URL": url
    }
