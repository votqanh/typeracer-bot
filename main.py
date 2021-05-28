from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver_path = '/Users/anhvo/Downloads/chromedriver'

with webdriver.Chrome(driver_path) as driver:
    driver.get('https://play.typeracer.com')

    el = '//*[@id="gwt-uid-1"]/a'
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, el)))
    driver.find_element_by_xpath(el).click()

    el = 'span[unselectable]'
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, el)))
    txt = driver.find_elements_by_css_selector(el)

    txt = [x.text for x in txt]
    txt = ' '.join([''.join(txt[0:len(txt)-1]), txt[-1]])

    el = '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input'
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, el)))

    for i in range(0, len(txt), 4):
        driver.find_element_by_xpath(el).send_keys(txt[i:i+4])

    sleep(20)
