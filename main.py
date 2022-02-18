from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

browser = webdriver.Firefox()

browser.get('https://www.instagram.com/')

username_input = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password_input = browser.find_element(By.NAME, 'password')
final_login = browser.find_element(By.TAG_NAME, 'form')

username = input('Please enter username:')
password = input('Please enter password:')

time.sleep(1)

username_input.send_keys(username)
password_input.send_keys(password)
final_login.click()

time.sleep(4)

instagram_button = browser.find_element(By.CLASS_NAME, 's4Iyt')
instagram_button.click()

time.sleep(4)

notification_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm")))
notification_button.click()

time.sleep(2)

for num in range(1,5):
    comment_button = browser.find_element(By.XPATH, '/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[' + str(num) +']/div/div[3]/div/div/section[1]/span[2]/button')
    time.sleep(0.5)
    comment_button.click()
    time.sleep(1)
    comment_input = browser.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
    time.sleep(0.5)
    comment_input.click()
    time.sleep(0.5)
    # ***** REPEAT IMMEDIATE LINE BELOW *****
    browser.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').send_keys('YOUR MESSAGE HERE')
    pyautogui.write("testing x")
    pyautogui.press('enter')
    time.sleep(3)
    x_button = browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/button')
    x_button.click()

while True:
    for x in range(20):
        pyautogui.press('down')
    comment_button = browser.find_element(By.XPATH,'/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[4]/div/div[3]/div/div/section[1]/span[2]/button')
    comment_button.click()
    time.sleep(0.5)
    comment_input = browser.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
    time.sleep(0.5)
    comment_input.click()
    time.sleep(0.5)
    pyautogui.write("testing x")
    pyautogui.press('enter')
    time.sleep(1.5)
    x_button = browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/button')
    x_button.click()
    time.sleep(0.5)
