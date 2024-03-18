from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

#initilzing Chrome Driver
# ch_options = Options()from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# import time
#
# #initilzing Chrome Driver
# # ch_options = Options()
# #
# # profile_path = r'/Users/surajyerramilli/Library/Application\ Support/Google/Chrome/Profile\ 1'
# # ch_options.add_argument(f'user-data-dir={profile_path}')
# #
# # extension_path = r'/Users/surajyerramilli/Library/Application\ Support/Google/Chrome/Profile\ 1/Extensions/chnccghejnflbccphgkncbmllhfljdfa/1.3.2.0_0'
# # ch_options.add_argument(f'--load-extension={extension_path}')
#
# #options = ch_options
#
# driver = webdriver.Chrome()
# #max size window
# driver.maximize_window()
# #Gnavigate to the URL
# driver.get("https://www.youtube.com/watch?v=Tjb5YZr9IyA&ab_channel=PBDPodcast")
# #wait on initial page for 3 seconds
# script_to_execute = "document.querySelector('video').playbackRate = 5;"
# driver.execute_script(script_to_execute)
# time.sleep(100)
#
# profile_path = r'/Users/surajyerramilli/Library/Application\ Support/Google/Chrome/Profile\ 1'
# ch_options.add_argument(f'user-data-dir={profile_path}')
#
# extension_path = r'/Users/surajyerramilli/Library/Application\ Support/Google/Chrome/Profile\ 1/Extensions/chnccghejnflbccphgkncbmllhfljdfa/1.3.2.0_0'
# ch_options.add_argument(f'--load-extension={extension_path}')

#options = ch_options

driver = webdriver.Chrome()
#max size window
driver.maximize_window()
#Gnavigate to the URL
driver.get("https://www.youtube.com/watch?v=Tjb5YZr9IyA&ab_channel=PBDPodcast")
#wait on initial page for 3 seconds

time.sleep(10)
script_to_execute = "document.querySelector('video').playbackRate = 5;"
driver.execute_script(script_to_execute)
time.sleep(100)

#i want to speed up the video using the chrome extension
