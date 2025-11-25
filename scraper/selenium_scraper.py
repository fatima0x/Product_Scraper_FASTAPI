from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)

    title = driver.find_element(By.TAG_NAME, "h1").text
    price = driver.find_element(By.CLASS_NAME, "price_color").text
    availability = driver.find_element(By.CLASS_NAME, "instock").text
    category = driver.find_elements(By.CSS_SELECTOR, "ul.breadcrumb li")[2].text
    rating = driver.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class").split()[1]

    driver.quit()

    return {
        "Title": title,
        "Price": price,
        "Availability": availability,
        "Category": category,
        "Rating": rating,
        "Product URL": url
    }
