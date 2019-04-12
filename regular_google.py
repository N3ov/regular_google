import re
import sys
import urllib.parse as UP

import requests
import bs4

def main():
    word = sys.argv[1]
    size = sys.argv[2]
    print('搜尋: %s' %(word))
    print('次數: %s' %(size))

    size = int(size)
    count = 0
    word = UP.quote(word)
    while count < size:
        response = requests.get('https://www.google.com.tw/search?&q=' + word + '&start=%d' %(count))
        # print(response.text)
        # print('')

        d = bs4.BeautifulSoup(response.text, 'html.parser')
        p = d.select('div.g h3.r>a')
        # print(len(p))

        for result in p:
            print('標題: %s' % (result.get_text()))
            href = result.get('href')
            match = re.search(r'/url\?q=(?P<url>.+)&sa=U', href)
            href = match.group('url')
            print('連結: %s' %(href))
            print('')


            count += 1

            if count == size:
                break


    
if __name__ == "__main__":
    main()
