import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

# use this web to set up yours: http://myhttpheader.com/
url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ja;q=0.8,de;q=0.7"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=465) as connection:
        connection.starttls()
        pw = "<YOUR PASSWORD>"
        result = connection.login("<YOUR EMAIL>", pw)
        print("sending")
        connection.sendmail(
            from_addr="<ENTER EMAIL>",
            to_addrs="<ENTER EMAIL>>",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
