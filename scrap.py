from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
def get_reviews(rlist):
	for r in rlist:
		d_r = r.find('button',class_='section-review-action-menu')['data-review-id']
		username = r.find('div',class_='section-review-title').find('span').text
		try:
			review_text = r.find('span', class_='section-review-text').text
			print(review_text)
		except Exception:
			review_text = None
		rating = r.find('span', class_='section-review-stars')['aria-label']
		rel_date = r.find('span', class_='section-review-publish-date').text
	
		with open('TWWReviews.csv', 'a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([username, review_text, rating,rel_date])


options = Options()
options.add_argument("--lang=en")
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
#url = "https://www.google.it/maps/place/SARDAR+VALLABHBHAI+PATEL+STATUE/@21.8968583,73.491444,17z/data=!4m7!3m6!1s0x396007141130d727:0xc9d8aa726a506fca!8m2!3d21.8968583!4d73.4936327!9m1!1b1"
#url = "https://www.google.it/maps/place/LDRP+Institute+of+Technology+and+Research/@23.239165,72.6363606,17z/data=!4m7!3m6!1s0x395c2b933477ba9f:0xe440409e66bea08a!8m2!3d23.239165!4d72.6385493!9m1!1b1"
#url = "https://www.google.it/maps/place/KSV+University/@23.2388113,72.6376165,17z/data=!4m7!3m6!1s0x395c2b9338c0dbf1:0x17fdfeca417ac752!8m2!3d23.2388113!4d72.6398052!9m1!1b1"
#url ="https://www.google.it/maps/place/Taj+Mahal/@27.1751448,78.0399535,17z/data=!4m7!3m6!1s0x39747121d702ff6d:0xdd2ae4803f767dde!8m2!3d27.1751448!4d78.0421422!9m1!1b1"
#url = "https://www.google.it/maps/place/Anne+Frank+House/@52.3752182,4.8817878,17z/data=!4m7!3m6!1s0x47c609c5213e1149:0xd49a5d653e635b0a!8m2!3d52.3752182!4d4.8839765!9m1!1b1"
#url = "https://www.google.it/maps/place/Sabarmati+Ashram/@23.0607723,72.5786981,17z/data=!4m7!3m6!1s0x395e8479e05f1901:0x16cbb1101e5729a3!8m2!3d23.0607723!4d72.5808868!9m1!1b1"
url = "https://www.google.it/maps/place/The+Wizarding+World+Of+Harry+Potter/@34.1383928,-118.3559601,17z/data=!4m7!3m6!1s0x80c2be49258fcd69:0x907f5454583f35eb!8m2!3d34.1380863!4d-118.3533177!9m1!1b1"
driver.get(url)
wait = WebDriverWait(driver, 10)
menu_bt = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-value=\'Sort\']')))  
menu_bt.click()
with open('TWWReviews.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(['UserName','Reviews','Rating','Date'])

for i in range(0,100):
	scrollable_div = driver.find_element_by_css_selector('div.section-layout.section-scrollbox.scrollable-y.scrollable-show')
	driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',scrollable_div)
	time.sleep(0.5)
response = BeautifulSoup(driver.page_source, 'html.parser')
rlist = response.find_all('div', class_='section-review-content')
get_reviews(rlist)
