# Housing Leads Web Scraper

## Overview

Background: This project was developed to assist an agency providing housing navigation services to individuals experiencing homelessness. Case managers help clients locate available housing units that match their income and credit backgrounds.

Problem: Housing navigation services were inconsistently provided due to the manual and time-consuming process of searching for available units, resulting in delays and non-compliance.

Solution: The Housing Web Scraper is a Python script that utilizes Selenium to automate the retrieval of housing leads from Craigslist. By applying specific location and income filters, it gathers relevant listings and sends email notifications to case managers, ensuring timely access to housing options for clients.

## Features

•	Automated Web Scraping: Gathers housing leads from Craigslist based on predefined filters such as location and income.
•	Email Notification: Automatically sends an email with the scraped listings, including links to the housing pages, directly to case managers.