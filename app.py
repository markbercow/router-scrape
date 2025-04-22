from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Set up Chrome options
options = Options()

driver = webdriver.Chrome(options=options)

try:
    # Open router admin page
    driver.get("http://192.168.0.1/webpages/index.html#/")

    # Wait for dynamic content to render
    time.sleep(10)

    # Extract and print info-wrapper divs (for debugging purposes)
    info_divs = driver.find_elements(By.CLASS_NAME, "info-wrapper")
    print(f"Found {len(info_divs)} info-wrapper div(s):\n")

    # Extract mac, ip, and name from each wrapper
    rows = []
    for wrapper in info_divs:
        mac = wrapper.find_element(By.CLASS_NAME, "mac").text.strip()
        ip = wrapper.find_element(By.CLASS_NAME, "ip").text.strip()
        name = wrapper.find_element(By.CLASS_NAME, "name").text.strip()
        if ip:
            rows.append({
                "MAC Address": mac,
                "IP Address": ip,
                "Device Name": name
            })

    # Create and display a pandas DataFrame
    df = pd.DataFrame(rows)
    # df.to_csv('ip-addresses.csv', index=False)

finally:
    driver.quit()
