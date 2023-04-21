import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

class kintai(unittest.TestCase):

    # テスト実行前にChromedriverの最新版を起動
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # テストメソッド実行後に毎回ブラウザを閉じる
    def tearDown(self):
        self.driver.quit()

    # ここからテストメソッド
    def test_kintai(self):
        driver = self.driver

        # e-naviを直接開く
        driver.get(
            "https://www.enavi-ts.net/ts-h-staff/Staff/login.aspx?ID=Ve4ctWhUz")
        time.sleep(2)

        # ユーザーID入力
        UserID = driver.find_element_by_name("TextStaffNo")
        UserID.clear()
        UserID.send_keys("2936")

        # パスワード入力
        password = driver.find_element_by_name("TextPassword")
        password.clear()
        password.send_keys("rakus123")

        # エンターキーを押してログイン
        password.send_keys(Keys.RETURN)
        time.sleep(2)

        # 「日時勤怠」を押下
        days = driver.find_element_by_name("ImgBtnMenuDay")
        days.click()
        time.sleep(2)

        # 「コメント」に文字を入力
        comment = driver.find_element_by_name("TextComment")
        comment.clear
        comment.send_keys("在宅勤務")
        time.sleep(2)

        # 「承認依頼」を押下
        register = driver.find_element_by_name("BtnOkSigndaywork")
        register.click()
        time.sleep(2)
        
        # 2度目の「承認依頼」を押下
        register2 = driver.find_element_by_name("BtnOk")
        register2.click()
        time.sleep(2)
        
        # ポップアップの「OK」を押下
        Alert(driver).accept()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
