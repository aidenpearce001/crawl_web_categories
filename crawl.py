from bs4 import BeautifulSoup
import requests
from urllib import parse
from urllib import robotparser
import re
import string
from urllib import request

try:
    url = "https://vnexpress.net/robots.txt"
    r = request.urlopen(url, timeout=10)
    data = r.read()
    text = data.decode()
    text = text.split("\r")
    for i in text:
        if "Sitemap" in i:
            i = i[10:]
            print(i)
            sitemap_index = {}

            r = requests.get(i)
            xml = r.text
            soup = BeautifulSoup(xml,"lxml")
            sitemapTags = soup.find_all("sitemap")
            for sitemap in sitemapTags:
                if "catego" in str(sitemap):
                    print('yes')
                    category_url =sitemap.findNext("loc").text
                    r1 = requests.get(category_url)
                    xml1 = r1.text
                    soup1 = BeautifulSoup(xml1,"lxml")
                    # print(soup1)
                    get_category = soup1.find_all("loc")
                    # print(get_category)
                    for category in get_category:
                        print(category.findNext("loc").text)
except:
    pass

# import requests
# from bs4 import BeautifulSoup
# url = 'https://dantri.com.vn/'
# reqs = requests.get(url)
# soup = BeautifulSoup(reqs.text, 'lxml')
# for ultag in soup.find('ul'):
#     for litag in ultag.find('li'):
#         print(litag)

