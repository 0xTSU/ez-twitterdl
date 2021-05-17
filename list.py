import requests
import json

class link_list():
    def __init__(self, list = None):
        self.list = self.buildList(list)

    # remove duplicates
    def buildList(self, list):
        links = []
        for i in list:
            if i not in links:
                links.append(i)
        return links

    def downloadImg(self):
        for i in self.list:
            x = 0
            request = requests.get(i)
            if request.status_code == 200:
                with open(x + "." + i[i.find('/')+1:], 'wb') as image:
                    image.write(request.content())
                x = x + 1
