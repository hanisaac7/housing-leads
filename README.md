# Housing Leads

Scrape housing leads from Craigslist and receive list of available/affordable units through email. 

## Overview

Background: This project was developed to assist an agency that services clients experiencing homelessness. A service that is provided to their clients is housing navigation. In other words, helping clients locate available housing units that would accept a client's income and credit background.

Problem: Housing navigation services were not being given to clients consistently.

Solution: This project is a Python script that utilizes Selenium for web scraping to gather housing leads from Craigslist with specific location/income filters. It then sends an email containing the scraped information with a link to the housing lead's respective page for the case manager to provide to the client.

## Features

- Web scraping of housing leads from Craigslist
- Email notifications with scraped housing information

## Getting Started

### Prerequisites

- Python 3.6+
- Selenium library
- Webdriver (e.g., EdgeDriver)
- Email account for sending notifications (Gmail in this example)

### Project Structure

|-- housing_leads_scraper.py
|-- requirements.txt
|-- msedgedriver
|-- README.md

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.
