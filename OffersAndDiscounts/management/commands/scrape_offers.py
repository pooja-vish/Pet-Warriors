from django.core.management.base import BaseCommand
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Command(BaseCommand):
    help = 'Scrapes offers from PetSmart and saves them to the database'

    def handle(self, *args, **kwargs):
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        try:
            driver.get('https://www.petsmart.com/sale/')
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'sparky-c-horizontal-overflow-carousel__list'))
            )
            for i in range(10):
                ordered_list = driver.find_element(By.CLASS_NAME, 'sparky-c-horizontal-overflow-carousel__list')
                list_items = ordered_list.find_elements(By.TAG_NAME, 'li')
                if i >= len(list_items):
                    print(f"Less than {i + 1} list items available.")
                    break

                item = list_items[i]
                print(f"Processing item {i + 1}/{len(list_items)}")
                animal_name = item.find_elements(By.TAG_NAME, 'span')[0].text
                print(f"Processing animal: {animal_name}")
                file = open(f"{animal_name}.txt", "w")
                anchors = item.find_elements(By.TAG_NAME, 'a')
                if not anchors:
                    print("No anchor tag found in this list item.")
                    continue

                link = anchors[0].get_attribute('href')
                print(f"Navigating to {link}")

                # Open the link in the current tab
                driver.get(link)

                # Wait for the new page to load
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.ID, 'search-result-items'))
                )
                file.close()
                try:
                    product_list = driver.find_element(By.ID, 'search-result-items')
                    list_items1 = product_list.find_elements(By.TAG_NAME, 'li')[:10]
                    file = open(f"{animal_name}.txt", "a")
                    for element in list_items1:

                        title = element.find_element(By.CLASS_NAME, 'product-name').text
                        file.write(title+"\n")
                        url = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
                        file.write(url+"\n")
                        sale_price = element.find_element(By.CLASS_NAME, 'product-price').text
                        file.write(sale_price+"\n")
                    file.close()

                except Exception as e:
                    print(f"Failed to extract products: {e}")
                driver.back()
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'sparky-c-horizontal-overflow-carousel__list'))
                )

        finally:
            driver.quit()