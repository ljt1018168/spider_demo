import requests
from bs4 import BeautifulSoup
import threading

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(e)
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.title.string
    print(title)

def crawl(url):
    html = get_html(url)
    if html:
        parse_html(html)

if __name__ == '__main__':
    urls = ['https://www.baidu.com', 'https://www.sogou.com', 'https://www.so.com', 'https://cn.bing.com']
    threads = []
    for url in urls:
        t = threading.Thread(target=crawl, args=(url,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# 优化一下
# 使用线程池来提高爬虫效率
from concurrent.futures import ThreadPoolExecutor

if __name__ == '__main__':
    urls = ['https://www.baidu.com', 'https://www.sogou.com', 'https://www.so.com', 'https://cn.bing.com']
    with ThreadPoolExecutor(max_workers=4) as executor:
        for url in urls:
            executor.submit(crawl, url)



