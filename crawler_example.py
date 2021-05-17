from selenium import webdriver
import time


options = webdriver.FirefoxOptions()
profile = webdriver.FirefoxProfile('xla56yi1.default-release-1621240391341')
options.headless = True
driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path="geckodriver.exe")
driver.get('https://twitter.com/akaihaato/media')




driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(3)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')



tweets = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
for i in range(len(tweets)):
    tweet = tweets[i]
    print(tweet.find_element_by_xpath('./div[2]/div[2]/div[2]//img').get_attribute('src'))
