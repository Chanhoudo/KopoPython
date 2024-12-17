from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

# ChromeDriver 경로 설정
CHROMEDRIVER_PATH = 'C:/tools/chromedriver/chromedriver.exe'  # ChromeDriver 경로

# ChromeDriver 설정
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')  # GPU 비활성화
# chrome_options.add_argument('--headless')   # 필요 시 헤드리스 모드 (브라우저 숨김)

# 웹 드라이버 초기화
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome()
driver.maximize_window()
# 접속할 URL 목록 (101 ~ 110)
base_url = "https://172.16.106."
urls = [f"{base_url}{i}/doc/index.html#/portal/login" for i in range(101, 111)]

count = 1
# 로그인 정보
username = "id"
password = "password"
while(1):
    # 작업 수행
    for idx, url in enumerate(urls):
        try:
            # 첫 번째 URL은 기본 탭에서 실행
            if idx == 0:
                driver.get(url)
            else:
                # 새로운 탭 열기
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(url)
            
            time.sleep(2)  # 페이지 로드 대기

            # "고급" 버튼 클릭
            try:
                advanced_button = driver.find_element(By.ID, "details-button")
                advanced_button.click()
                print("고급 버튼을 클릭했습니다.")
                time.sleep(1)
            except:
                print("고급 버튼이 없습니다.")

            # "안전하지 않음" 링크 클릭
            try:
                proceed_link = driver.find_element(By.ID, "proceed-link")
                proceed_link.click()
                print("안전하지 않음 링크를 클릭했습니다.")
                time.sleep(2)  # 클릭 후 페이지 로드 대기
            except:
                print("안전하지 않음 링크가 없습니다.")
            time.sleep(5)
            # 로그인 작업 수행
            try:
                id_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='사용자 이름']")
                id_input.send_keys(username)

                pw_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='비밀번호']")
                pw_input.send_keys(password)

                login_button = driver.find_element(By.CSS_SELECTOR, "button.login-btn")
                login_button.click()
                print(f"{url} 로그인 작업 완료.")
                time.sleep(5)
                pyautogui.press('f2') #녹화 시작
                time.sleep(12)

                # 첫 번째 메뉴 클릭 후 5초 뒤 F3
                print("첫 번째 메뉴 클릭...")
                first_menu = driver.find_element(By.CSS_SELECTOR, "i.ic-icon_smartshow_nor")
                first_menu.click()
                time.sleep(5)
                print("첫 번째 메뉴 완료.")
                time.sleep(2)

                # 두 번째 메뉴 클릭 후 5초 뒤 F3
                print("두 번째 메뉴 클릭...")
                second_menu = driver.find_element(By.CSS_SELECTOR, "i.ic-icon_appmanage_nor")
                second_menu.click()
                time.sleep(5)
                print("두 번째 메뉴 완료.")
                time.sleep(2)

                # 세 번째 메뉴 클릭 후 5초 뒤 F3
                print("세 번째 메뉴 클릭...")
                third_menu = driver.find_element(By.CSS_SELECTOR, "i.ic-icon_camerasetting_nor")
                third_menu.click()
                time.sleep(5)
                print("세 번째 메뉴 완료.")
                time.sleep(2)

                # "영상" 메뉴 클릭 후 5초 뒤 F3
                print("'영상' 메뉴 클릭...")
                video_menu = driver.find_element(By.XPATH, "//li[@title='영상']/span[contains(@class, 'el-menu-item--text')]")
                video_menu.click()
                time.sleep(15)
                print("'영상' 메뉴 F2 입력 완료.")
                time.sleep(2)
                
                # "OSD 설정" 클릭 후 5초 뒤 F3
                print("'OSD 설정' 클릭...")
                osd_settings = driver.find_element(By.ID, "tab-osd")
                osd_settings.click()
                time.sleep(15)
                print("'OSD' 메뉴 F2 입력 완료.")
                time.sleep(2)

                # "사생활 보호" 클릭 후 5초 뒤 F3
                print("'사생활 보호' 클릭...")
                osd_settings = driver.find_element(By.ID, "tab-privacyMask")
                osd_settings.click()
                time.sleep(15)
                
                print("'사생활 보호' 메뉴 F2 입력 완료.")
                time.sleep(2)
                
                # "사생활 보호" 클릭 후 5초 뒤 F3
                print("'캡쳐 이미지 오버레이' 클릭...")
                osd_settings = driver.find_element(By.ID, "tab-pictureOverlay")
                osd_settings.click()
                time.sleep(15)

                print("'캡쳐 이미지 오버레이' 메뉴 F2 입력 완료.")
                time.sleep(2)

                # 네 번째 메뉴 클릭 후 5초 뒤 F3
                print("네 번째 메뉴 클릭...")
                fourth_menu = driver.find_element(By.CSS_SELECTOR, "i.ic-icon_safety_nor")
                fourth_menu.click()
                time.sleep(5)
                print("네 번째 메뉴 완료.")

                pyautogui.press('f2') #녹화 종료
            except Exception as e:
                print(f"{url} 로그인 실패: {e}")

        except Exception as e:
            print(f"{url} 접속 중 오류 발생: {e}")

    # 모든 작업 완료
    print(f"모든 사이트 작업이 {count}만큼 완료되었습니다.")
    count += 1
    time.sleep(5)

# 드라이버 종료
# driver.quit()
