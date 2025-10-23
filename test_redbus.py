from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time,traceback

def test_redbus():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-fullscreen")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver,25)
    action = ActionChains(driver)
    driver.get("https://www.redbus.in/")
    wait.until(EC.presence_of_element_located((By.XPATH,"(//div[contains(@class,'srcDestWrapper')])[1]"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='srcDest']"))).send_keys("che")
    time.sleep(2)
    from_results = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//div[contains(@class,'leftContent')]/div[contains(@class,'listHeader')]")

    ))
    for r in from_results:
        if "Chennai" in r.text:
            r.click()
            break

    wait.until(EC.presence_of_element_located((By.XPATH,"(//div[contains(@class,'srcDestWrapper')])[2]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'inputField___a5ec46')]"))).send_keys("Bang")
    time.sleep(1)
    to_results = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//div[contains(@class,'leftContent')]/div[contains(@class,'listHeader')]")))
    for t in to_results:
        if "Bangalore" in t.text:
            t.click()
            break
    time.sleep(1)

    try:
        date_cal = wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='dateWrapper___5e7fce']/div/div)[1]")))
        time.sleep(2)
        action.move_to_element(date_cal).click().perform()
        print("clicked")
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, "(//i[@role='button'])[2]")))
        for i in range(2):
            next_button.click()
            time.sleep(0.5)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-date='1765823400000']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search buses')]"))).click()
        time.sleep(10)


    
    except Exception as e:
        traceback.print_exc()
    driver.quit()