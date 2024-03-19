from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Chromeのドライバーを初期化
driver = webdriver.Chrome(ChromeDriverManager().install())

# Googleのページを開く
driver.get("https://itb-hdb2.htdb.jp/ggutk9a/")

# IDとパスワードを入力しエンター押下
ID_box = driver.find_element_by_id("loginId")
Pass_box = driver.find_element_by_id("loginPassword")

ID_box.send_keys("ritsu.sugita")
Pass_box.send_keys("rakus@1234")
ID_box.send_keys(Keys.RETURN)
time.sleep(1)

# iframeというタグが使用されているためdriverをiframeに切り替える
# driverを基のWebページに戻したいときは"switch_to.default_content()"を利用
iframe_side = driver.find_element_by_id("side")
driver.switch_to.frame(iframe_side)

# 　「日報・月報」押下
nippou = driver.find_element_by_id("nav-dbg-100026")
nippou.click()
time.sleep(2)

# 「業務開始DB」を押下
gyoumu = driver.find_element_by_xpath('//*[@id="nav-db-100539"]/a')
gyoumu.click()
time.sleep(1)

# 「業務開始」を押下
gyoumu_start = driver.find_element_by_xpath('//*[@id="menuli_101055"]/a/div')
gyoumu_start.click()
time.sleep(1)

# driver元のWebページに戻す
driver.switch_to_default_content()

# iframeの切替え
iframe_main = driver.find_element_by_id("main")
driver.switch_to.frame(iframe_main)

# テキストボックスに文章挿入
text_field = driver.find_element_by_id("field_103738")
text_field.send_keys("9:00より業務開始")
time.sleep(1)

# 「確定」を押下
# confirm = driver.find_element_by_xpath('//*[@id="saveDisp"]/li[1]')
# confirm.click()

# 「キャンセル」を押下
cancel = driver.find_element_by_xpath('//*[@id="saveDisp"]/li[2]')
cancel.click()
time.sleep(1)

# ブラウザを終了する
driver.quit()
