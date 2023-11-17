from email.message import EmailMessage
import os
import ssl
import smtplib
import certifi
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
import time

def scrape_data():
    global scraped_data, edge_driver_title

    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument('--headless')

    edge_driver = webdriver.Edge(options=edge_options)
    edge_driver.get("https://orangecounty.craigslist.org/search/santa-ana-ca/apa?availabilityMode=1&lat=33.7631&lon=-117.8173&max_price=1500&search_distance=15#search=1~gallery~0~0")
    edge_driver_title = edge_driver.title 
    edge_driver.implicitly_wait(10)

    rentals = edge_driver.find_elements('xpath', '//li[contains(@class, "cl-search-result") and contains (@class, "cl-search-view-mode-gallery")]')

    max_rentals = 10
    filtered_rentals = []
    for rental in rentals:
        if len(filtered_rentals) >= max_rentals:
            break
        filtered_rentals.append(rental)

        rental_link_element = rental.find_element(By.XPATH, '//a[contains(@class, "cl-app-anchor") and contains(@class, "text-only") and contains(@class, "posting-title")]')
        rental_link = rental_link_element.get_attribute('href')

    scraped_data = "\n".join(f"{rental.text}\n{rental_link}" + '_________________' for rental in filtered_rentals)

    edge_driver.quit()

def send_email():
    mh_password = os.environ.get('MH_PASSWORD')
    email_sender = 'ihan.mercyhouse@gmail.com'
    email_password = mh_password
    email_receiver = 'ihan@mercyhouse.net'

    email = EmailMessage()
    email['From'] = email_sender
    email['To'] = email_receiver
    email['Subject'] = "Housing Leads"
    
    email.set_content(f"{edge_driver_title}\n\n{scraped_data}")

    context = ssl.create_default_context(cafile=certifi.where())

    if os.environ.get('TEST_MODE') == 'True':
        print("Testing mode: Email not sent. Data:")
        print(f"{edge_driver_title}\n\n{scraped_data}")
    else:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.send_message(email)
        print("Email Sent!")
        os.environ['TEST_MODE'] = 'False'

def go():
    print("Running go function at", time.strftime("%Y-%m-%d %H:%M:%S"))
    scrape_data()
    send_email()

go()