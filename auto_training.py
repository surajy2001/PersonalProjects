from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
#max size window
driver.maximize_window()
#Gnavigate to the URL
driver.get("https://site.gcntraining.com/")
#wait on initial page for 3 seconds
time.sleep(3)


#This locates the login button
link = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/a[2]/img")
#this clicks the button
link.click()


#This waits on the new page for 5 seconds
wait = WebDriverWait(driver, 10)
#Wait on pge until the textbox field is detected
org_ID = wait.until(EC.visibility_of_element_located((By.ID, "org_id")))

#Once detected, add the text
org_ID.send_keys("52245F")

#Finds the submit button 
org_ID_submit = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]")

#CLicks submit button
org_ID_submit.click()


wait2 = WebDriverWait(driver, 20)

user_name = wait2.until(EC.visibility_of_element_located((By.ID, "user_id")))

user_name.send_keys("push5301")



user_submit = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/form[2]/div[1]/button[1]")

user_submit.click()


wait3 = WebDriverWait(driver, 20)

final_submit = wait3.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/form[4]/div/button[1]")))


final_submit.click()


#now we are in the main assignments page

wait4 = WebDriverWait(driver, 20)

#Find an assignment --- THis will need to change
#playground safety 
choose_assignment = wait4.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[1]/form[16]/div[1]")))

try:
    cookie = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/button")))
    cookie.click()
    print("Cookie Accepted")
except:
    print("Cookie Consent Failed")
    

time.sleep(5)

wait5 = WebDriverWait(driver, 20)

start_assignment = wait5.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[1]/form[16]/button")))

start_assignment.click()


time.sleep(5)

wait6 = WebDriverWait(driver, 15)
start_tutorial = wait6.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/a")))

start_tutorial.click()

for _ in range(30):
    time.sleep(5) 
    wait_video = WebDriverWait(driver, 300)
    next_slide = wait_video.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/button[4]")))

    next_slide.click()

time.sleep(100)














time.sleep(100)   

