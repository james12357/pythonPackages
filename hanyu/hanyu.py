import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 "
               "Safari/537.36"}


def get():
    res = requests.get("https://hanyu.baidu.com/s?wd=%E9%BA%BB%E6%9C%A8%E4%B8%8D%E4%BB%81&ptype=zici",
                       headers=headers).text
    return res


a = get()
print(a)
soup = BeautifulSoup(a, "lxml")
f = soup.select("#basicmean-wrapper > div.tab-content.srow > dl > dd > p")
print(f)
