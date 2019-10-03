import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Sony-Interchangeable-Digital-28-70mm-Accessory/dp/B00R1P93SC/ref=sr_1_2_sspa?keywords=sony+a7&qid=1570119316&s=gateway&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExT0VKRUNMMEVKS0NRJmVuY3J5cHRlZElkPUEwOTkwMjIyMjlKRkNPSFlESFNBWSZlbmNyeXB0ZWRBZElkPUExMDMyNTczM08yTlJEMlFQRzJIVCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    # print(soup.prettify())

    title = soup2.find(id= "productTitle")
    price = soup2.find(id="priceblock_saleprice")
    print(price)
    converted_price = float(price[0.7])
    if(converted_price < 1.000):
        send_mail()

    print(converted_price)
    print(title)

    # if(price > 1.300):
    #     send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email@gmail.com', 'password')
    subject = 'price drop'
    body = 'check product link https://www.amazon.com/Sony-Interchangeable-Digital-28-70mm-Accessory/dp/B00R1P93SC/ref=sr_1_2_sspa?keywords=sony+a7&qid=1570119316&s=gateway&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExT0VKRUNMMEVKS0NRJmVuY3J5cHRlZElkPUEwOTkwMjIyMjlKRkNPSFlESFNBWSZlbmNyeXB0ZWRBZElkPUExMDMyNTczM08yTlJEMlFQRzJIVCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    
    # msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'email@gmail.com',
        'email@gmail.com',
        subject,
        body

    )
    print('Hey Email Has Been Sent')
    server.quit()

while(True):
    check_price()
    time.sleep(60)