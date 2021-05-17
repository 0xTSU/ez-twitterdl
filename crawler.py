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
        options.headless = False
        #profile = webdriver.FirefoxProfile(self.profile)
        driver = webdriver.Firefox(firefox_profile="xla56yi1.default-release-1621240391341", 
                                    options=options, executable_path="geckodriver.exe")
        driver.get(self.link)
        before = driver.execute_script('return document.body.scrollHeight')

        while True:
            tweets = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
            self.appendToList(tweets)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)
            after = driver.execute_script('return document.body.scrollHeight')
            if before == after:
                break
            before = after

    def appendToList(self, list):
        tweets = list
        image_link = ""
        for i in range(len(tweets)):
            tweet = tweets[i]
            image_link = " "

            try:
                image = tweet.find_element_by_xpath('./div[2]/div[2]/div[2]//img').get_attribute('src')
                image_link_index = image.split('\n')
                for i in image_link_index:
                    if i.find('&name=') > 0:
                        image_link = i[:i.find('&name=')] + '&name=large'
                    else:
                        image_link = i
            except:
                try:
                    image = tweet.find_element_by_xpath('./div[2]/div[2]/div[2]//vid').get_attribute('src')
                    vid_link_index = image.split('\n')
                    for i in vid_link_index:
                        if i.find('&name=') > 0:
                            image_link = i[:i.find('&name=')] + '&name=large'
                        else:
                            image_link = i
                except:
                    pass
            finally:
                pass
            
            if len(image_link) > 2: 
                self.list.append(image_link)

    def getList(self):
        return self.list
