from selenium import webdriver
import time

# Chromeのオプション
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Selenium Serverに接続
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub", options=options
)

try:
    # 要素の待機時間を最大10秒に設定
    driver.implicitly_wait(10)

    # https://gihyo.jp を開く
    driver.get("https://gihyo.jp")

    # 検索ボックスに「Ubuntu」を入力
    element_search_form = driver.find_element_by_id("searchFormKeyword")
    element_search_form.send_keys("Ubuntu")

    # 検索ボタンをクリック
    element_search_button = driver.find_element_by_id("searchFormSubmit")
    element_search_button.click()
    time.sleep(5)

    # 検索結果のタイトルを取得して出力
    element_titles = driver.find_elements_by_xpath("//a[@class='gs-title']")
    for element_title in element_titles:
        if not element_title.text.strip():
            continue
        print(element_title.text.strip())

except:
    import traceback

    traceback.print_exc()

finally:
    # Chromeを終了
    input("何かキーを押すと終了します...")
    driver.quit()


"""from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# Chromeのドライバーを初期化
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',options=options)

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
"""
