from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

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
    if "Ashok Pillar, Chennai" in r.text:
        r.click()
        break

wait.until(EC.presence_of_element_located((By.XPATH,"(//div[contains(@class,'srcDestWrapper')])[2]"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'inputField___a5ec46')]"))).send_keys("Sarj")
time.sleep(1)
to_results = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//div[contains(@class,'leftContent')]/div[contains(@class,'listHeader')]")))
for t in to_results:
    if "Sarjapura Road Signal, Bangalore" in t.text:
        t.click()
        break
time.sleep(2)
date_cal = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'dojWrapper')]")))
print(date_cal.is_displayed(),date_cal.is_enabled())
date_cal.click()



driver.quit()


