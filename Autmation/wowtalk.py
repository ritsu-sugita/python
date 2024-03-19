from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import unittest
from time import sleep

class wowtalk(unittest.TestCase):
    
    # テスト実行前に実行する処理
    def setUp(self):
        # Chromeのドライバーを起動
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # 最大待機時間を10秒に設定
        self.driver.implicitly_wait(10)
        
    # テスト実行後に実行する処理
    def tearDown(self):
        # ブラウザを閉じる
        self.driver.quit()

    # テストメソッド
    def test_wowtalk(self):
        driver=self.driver
        # rakuplusを直接開く
        driver.get("https://biz.wowtalk.org/webtalk/login")
        # 企業IDを入力
        companyid=driver.find_element_by_id("company_id")
        companyid.clear
        companyid.send_keys("rakus")
       #　ユーザーIDを入力
        userid=driver.find_element_by_id("user_id")
        userid.clear
        userid.send_keys("ritsu-sugita")
       #　パスワードを入力
        password=driver.find_element_by_id("password")
        password.clear
        password.send_keys("rakus123")
       #　エンター押下でログイン
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        
       
      
       # 「了解」をクリック
        elem = driver.find_element_by_xpath('//*[@id="tutorial"]/div/div[2]/button')
        elem.click()
        time.sleep(2)
       #　たましのトーク画面を表示
        tamashi = driver.find_element_by_xpath("//div[@title='玉川詩乃']") 
        tamashi.click()
        time.sleep(5)
      


if __name__ == '__main__':
    unittest.main()
