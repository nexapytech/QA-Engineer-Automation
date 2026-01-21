from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_ui_smoke_page_load(live_server):
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(live_server.url + "/ui/")

        # 1️⃣ Page loads
        assert "Expense Tracker" in driver.title

        # 2️⃣ Core UI elements exist
        assert driver.find_element(By.ID, "username")
        assert driver.find_element(By.ID, "apiKeyInput")
        assert driver.find_element(By.TAG_NAME, "button")

    finally:
        driver.quit()
