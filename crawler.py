from selenium import webdriver
import time

class pageCrawler():
    def __init__(self, handle = None):
        self.link = "https://twitter.com/" + handle + "/media"

        # to do
        self.vars = None 
        self.profile = None
        self.gecko = None

        # list to give to requests class
        self.list = []

    def buildPage(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        profile = webdriver.FirefoxProfile(self.profile)
        driver = webdriver.Firefox(firefox_profile=profile, 
                                    options=options, executable_path=self.gecko)
        driver.get(self.link)
        before = driver.execute_script('return document.body.scrollHeight')

        while True:
            tweets = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
            self.appendToList(tweets)
            driver.execute(driver.execute_script('window.scrollTo(0, document.body.scrollHeight);'))
            after = driver.execute_script('return document.body.scrollHeight')

            if before == after:
                break
            before = after
            time.sleep(3)

    def appendToList(self, list):
        tweets = list

        for i in range(len(tweets)):
            tweet = tweets[i]
            image = tweet.find_element_by_xpath('./div[2]/div[2]/div[2]//img').get_attribute('src')
            image_link = image[:image.find("&name=")] + "&name=large"
            self.list.append(image_link)

    def getList(self):
        return self.list
