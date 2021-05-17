import requests
from crawler import pageCrawler
import os

class link_list():
    def __init__(self, handle, list = None):
        self.list = self.buildList(list)
        self.handle = handle

    # remove duplicates
    def buildList(self, list):
        links = []
        for i in list:
            if i not in links:
                links.append(i)
        return links

    def downloadImg(self):
        x = 0
        for i in self.list:
            request = requests.get(i)
            type = request.headers.get('content-type')

            if not os.path.exists(self.handle):
                os.makedirs(self.handle)

            if request.status_code == 200:
                with open(self.handle + "/" + self.handle + "_" + str(x) + "." + type[type.find("/") + 1:], 'wb') as image:
                    image.write(request.content)
                print(self.handle + "_" + str(x) + "." + type[type.find("/") + 1:] + " downloaded.")
                x += 1 
