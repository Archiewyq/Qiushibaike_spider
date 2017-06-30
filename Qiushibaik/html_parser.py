'''
Created on 2017年6月28日

@author: wyq
'''
from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):
    
    
    def get_new_urls(self, page_url, soup):
        new_urls = set()
        
        links = soup.select("ul.pagination li a ")
        
        for link in links:
            if link.find("span", class_="next") != None:
                print("new page")
                new_url = link["href"]
                new_full_url  = urllib.parse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)
        
        return new_urls
    
    
    def get_new_data(self, page_url, soup):
        res_data = []

#         pattern = re.compile('<div.*?class="content">.*?<span>(.*?)</span>.*?</a>'+'(.*?<div.*?"stats".*?</div>)', re.RegexFlag.S)
        pattern = re.compile('<div.*?class="content">\n*?<span.*?</span>\n*?</div>')
        items = re.findall(pattern, str(soup))
        b = '<div class="content"><span>'
#         print(items)
        for item in items:
            temp = item.replace('\n', '')
            temp = temp.replace('</span></div>', '')
            temp = temp.replace('<br/>','')
#             print(temp.replace(b, '')+'\n')
            res_data.append(temp.replace(b, ''))

        return res_data
    
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, "html.parser")
        new_urls =  self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup)

        return new_urls, new_data
    
    



