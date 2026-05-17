import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_events():
    events = []

    url = "https://books.toscrape.com/index.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    st.write("books")
    st.write(books)

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        stock = book.find("p", class_="instock availability").text.strip()

        events.append({
            "title": title,
            "price": price,
            "stock": stock
        })

    return events