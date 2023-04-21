from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Chromeのドライバーを初期化
driver = webdriver.Chrome(ChromeDriverManager().install())

# Googleのページを開く
driver.get("https://www.google.com")

# 検索ボックスに入力し、Enterキーを押す
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

# ページが完全に読み込まれるまで待機する
time.sleep(3)

# ブラウザを終了する
driver.quit()
