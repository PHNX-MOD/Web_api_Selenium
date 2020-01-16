from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Firefox()

	def closeBrowser(self):
		self.driver.close()

	def login(self):
		driver = self.driver
		driver.get("https://www.instagram.com/")
		time.sleep(2)
		login_button=driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
		login_button.click()
		time.sleep(2)
		user_name_elem = driver.find_element_by_xpath("//input [@name='username']")
		user_name_elem.clear()
		user_name_elem.send_keys(self.username)
		password_ele = driver.find_element_by_xpath("//input [@name='password']")
		password_ele.clear()
		password_ele.send_keys(self.password)
		password_ele.send_keys(Keys.RETURN)
		time.sleep(2)

	def like_photo(self, hashtag):
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
		time.sleep(2)

		pic_hrefs = []
		for i in range(1, 7):
			try:
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(2)

				hrefs_in_view = driver.find_elements_by_tag_name('a')

				hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
								 if '.com/p/' in elem.get_attribute('href')]

				[pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]

			except Exception:
				continue

		unique_photos = len(pic_hrefs)
		for pic_href in pic_hrefs:
			driver.get(pic_href)
			time.sleep(2)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			try:
				time.sleep(random.randint(2, 4))
				follow_button = lambda: driver.find_element_by_xpath('//button[@class="oW_lN sqdOP yWX7d    y3zKF     "]/span[@type="button"]').click()
				follow_button().click()
				for second in reversed(range(0, random.randint(18, 28))):
					print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
									+ " | Sleeping " + str(second))
					time.sleep(1)
			except Exception as e:
				time.sleep(2)
			unique_photos -= 1

if __name__ == "__main__":

	username = "username"
	password = "password"
	ig = InstagramBot(username, password)
	ig.login()
	ig.like_photo('followforfollowback')
	hashtags = ['amazing', 'beautiful', 'adventure', 'photography', 'nofilter',
				'newyork', 'artsy', 'alumni', 'lion', 'best', 'fun', 'happy',
				'art', 'funny', 'me', 'followme', 'follow', 'cinematography', 'cinema',
				'love', 'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy',
				'street', 'canon', 'beauty', 'studio', 'pretty', 'vintage', 'fierce']




