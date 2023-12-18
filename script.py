from email.message import EmailMessage
import os
import ssl
import smtplib
import certifi
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
import time

barrier = '___________________________'

def scrape_data(driver):
    driver.get("https://orangecounty.craigslist.org/search/santa-ana-ca/apa?availabilityMode=1&lat=33.7631&lon=-117.8173&max_price=1500&search_distance=15#search=1~gallery~0~0")
    title = driver.title 
    driver.implicitly_wait(10)

    rental_list = driver.find_elements(By.XPATH, '//li[contains(@class, "cl-search-result") and contains (@class, "cl-search-view-mode-gallery")]')
    rental_link_list = driver.find_elements(By.XPATH, '//a[contains(@class, "cl-app-anchor") and contains(@class, "text-only") and contains(@class, "posting-title")]')

    max_rentals = 7
    filtered_rentals = []

    for rental, rental_link in zip(rental_list, rental_link_list):
        filtered_rentals.append((rental.text, rental_link.get_attribute('href')))
        if len(filtered_rentals) >= max_rentals:
            break

    scraped_data = "\n".join(f"{rental_tuple[0]}\n{rental_tuple[1]}\n{barrier}" for rental_tuple in filtered_rentals)

    return scraped_data, title

def send_email(sender, password, receiver, subject, content):
    email = EmailMessage()
    email['From'] = sender
    email['To'] = ', '.join(receiver)
    email['Subject'] = subject
    email.set_content(content)

    context = ssl.create_default_context(cafile=certifi.where())

    if os.environ.get('TEST_MODE') == 'True':
        print("Testing mode: Email not sent. Data:")
        print(content)
    else:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.send_message(email)
        print("Email Sent!")
        os.environ['TEST_MODE'] = 'False'

def job():
    print("Running job function at", time.strftime("%Y-%m-%d %H:%M:%S"))

    try:
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument('--headless')
        edge_driver = webdriver.Edge(options=edge_options)

        scraped_data, title = scrape_data(edge_driver)
        intro_content = "Hello Team,\n\nPlease view the following leads:\n"
        email_content = f"{intro_content}\n{title}\n\n{scraped_data}"
        
        receiver = 'tanial@mercyhouse.net', 'ihan@mercyhouse.net', 'nohelyc@mercyhouse.net', 'gisselleb@mercyhouse.net', 'jessicaw@mercyhouse.net', 'joeym@mercyhouse.net', 'kerrya@mercyhouse.net', 'lenar@mercyhouse.net', 'mcastaneda@mercyhouse.net', 'markg@mercyhouse.net', 'moncerratp@mercyhouse.net', 'nataliea@mercyhouse.net', 'rileighh@mercyhouse.net', 'shaheda@mercyhouse.net'
        send_email('ihan.mercyhouse@gmail.com', os.environ.get('MH_PASSWORD'), receiver, 'Housing Leads', email_content)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        try:
            edge_driver.quit()
        except NameError:
            pass  

job()


#def run_job():
 #   current_day = datetime.today().weekday()
  #  target_day = 2

#    if current_day == target_day:
        #job()
 #   else:
        #print(f"Job not scheduled for today (current day: {current_day}).")


#schedule.every().wednesday.at("10:00").do(run_job)

#while True:
    #schedule.run_pending()
    #time.sleep(1)