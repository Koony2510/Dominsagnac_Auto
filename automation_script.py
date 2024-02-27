from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Chrome 옵션 설정
chrome_options = webdriver.ChromeOptions()

# 현재 사용 중인 Chrome 브라우저 버전 입력
chrome_version = "121.0.6167"

# Chrome 드라이버 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager(version=chrome_version).install()), options=chrome_options)

# 사이트 접속
driver.get("https://www.betman.co.kr/")

# 게임 구매 클릭
xpath_game_purchase = "//a[@class='lv-3-menu' and text()='게임구매']"
driver.find_element("xpath", xpath_game_purchase).click()

# 적중 결과 클릭
xpath_win_result = "//a[@href=\"javascript:movePage('201010400', '/main/mainPage/gamebuy/winrstList.do');\"]"
driver.find_element("xpath", xpath_win_result).click()

# 게임종류 선택
xpath_game_type = "//select[@class='selectMenu' and @title='게임종류 선택']/option[text()='-축구토토 승무패']"
driver.find_element("xpath", xpath_game_type).click()

# 검색 버튼 클릭
xpath_search_button = "//button[@id='btn_sch']"
driver.find_element("xpath", xpath_search_button).click()

# 최상단 회차 클릭
latest_round_xpath = "//tbody/tr[1]/td[1]/a"
driver.find_element("xpath", latest_round_xpath).click()

# 환급내역 표의 부분을 선택
refund_table = driver.find_element(By.XPATH, "//div[@class='contTitle lybox' and h4='환급내역']/following-sibling::div[@class='tblArea noPadd']//table[@class='tbl tblAuto']")

# 테이블 내의 행 찾기
refund_rows = refund_table.find_elements(By.XPATH, ".//tbody[@id='tb_detlWdlPayo']/tr")

# 페이지 상단 제목 가져오기
page_title = driver.find_element(By.XPATH, "//div[@class='contTitle']/h3/span[@class='titSub']").text

# 각 행의 정보 출력
for row in refund_rows:
    # 각 열의 정보 추출
    category = row.find_element(By.XPATH, "./td[@class='tac']").text
    last_round_rollover_amount = row.find_element(By.XPATH, "./td[@class='tar'][1]").text
    total_refund_amount = row.find_element(By.XPATH, "./td[@class='tar'][2]").text
    consecutive_rollover_count = row.find_element(By.XPATH, "./td[@class='tar'][5]").text
    next_round_rollover_amount = row.find_element(By.XPATH, "./td[@class='tar'][6]").text

    # '1등' 행의 '연속이월회수'가 1보다 크거나 같으면 출력
    if category == '1등' and int(consecutive_rollover_count) >= 1:
        result_text = f"{page_title} - {consecutive_rollover_count}회 연속 이월 : {next_round_rollover_amount}({last_round_rollover_amount})"
        print(result_text)

# WebDriver 종료
driver.quit()
