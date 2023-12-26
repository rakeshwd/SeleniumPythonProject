from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import random

# Specify the website URL
url = "https://sites.google.com/view/sp-inform"  # Replace with the actual URL

# Initialize the WebDriver (replace with the appropriate driver if needed)
driver = webdriver.Chrome()

# Visit the website
driver.get(url)

# Extract HTML content
html = driver.page_source

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# Find all links
links = soup.find_all("a")

# Dump links to a text file
with open("links.txt", "w") as file:
    for link in links:
        href = link.get("href")
        if href:
            file.write(href + "\n")

# Click links with random time intervals and check for broken links
broken_links = []
for link in links:
    href = link.get("href")
    if href:
        try:
            time.sleep(random.randint(2, 5))  # Random interval between 2 and 5 seconds
            link_element = driver.find_element(By.LINK_TEXT, link.text)  # Find link by text
            link_element.click()
            time.sleep(2)  # Wait for page to load
        except NoSuchElementException:
            broken_links.append(href)
        except Exception as e:
            print(f"Error clicking link: {href}. Exception: {e}")

# Close the WebDriver
driver.quit()

# Generate broken link report and log to file
if broken_links:
    with open("broken_links.log", "w") as log_file:
        log_file.write("**** BROKEN LINK REPORT ****\n")
        for link in broken_links:
            log_file.write(f"{link}\n")
