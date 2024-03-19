from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import unittest
from time import sleep



class TestGoogleSearch(unittest.TestCase):
    
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
    def test_search_rakuplus_on_google(self):
        # rakuplusを直接開く
        self.driver.get("https://rakuplus.jp/")
        mail=self.driver.find_element_by_id("user_login")
        mail.send_keys("ritsu.sugita@rakus-partners.co.jp")
        password=self.driver.find_element_by_id("user_pass")
        password.send_keys("ritsu.sugita@rakus-partners.co.jp")
        password.send_keys(Keys.RETURN)
        time.sleep(2)
      


if __name__ == '__main__':
    unittest.main()
