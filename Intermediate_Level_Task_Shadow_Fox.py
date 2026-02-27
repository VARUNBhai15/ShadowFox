import requests
from bs4 import BeautifulSoup
import csv
url = "https://quotes.toscrape.com"


headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, "html.parser")

    
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    print("\n Quotes Extracted:\n")

    # Save to TXT file
    with open("quotes.txt", "w", encoding="utf-8") as txt_file:
        for quote, author in zip(quotes, authors):
            line = f"{quote.text} — {author.text}"
            print(line)
            txt_file.write(line + "\n")

    # Save to CSV file
    with open("quotes.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Quote", "Author"])  

        for quote, author in zip(quotes, authors):
            writer.writerow([quote.text, author.text])

    print("\n Data saved to quotes.txt and quotes.csv")

except requests.exceptions.RequestException as e:
    print(" Error occurred while fetching the website:")
    print(e)

