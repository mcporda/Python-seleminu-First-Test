import time,requests,urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
star = time.time()
browser = webdriver.Chrome()
n = 1
total = 0
for num in range(48,0,-1):
    browser.get('http://jandan.net/ooxx/page-'+str(num)+'#comments')
    data = browser.page_source
    soup = BeautifulSoup(data,'lxml')
    download_links = []
    folder_path = '/Users/XXXXXX/Desktop/JD/'      #改个路径就行，脚本可以直接运行
# print('===========第' + str(num) + '页===============')
    for pic_tag in soup.find_all('img'):
        pic_link = pic_tag.get('src')
        download_links.append(pic_link)
    for item in download_links:
        try:
            urllib.request.urlretrieve(item,folder_path + item[-10:])
            print('正在下载第{}图片'.format(n))
            total += 1
        except:
            print('第{}张图片下载出错，已跳过'.format(n))
        n += 1
browser.close()
end = time.time()
print('总共用时{}分'.format((end-star)/60))
print('成功下载{}张图片，失败{}张图片'.format(total,n-total))
