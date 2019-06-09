#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import const
from bs4 import BeautifulSoup


def main():
    r = requests.get(const.BASE_URL + const.SCRAPING_URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    # 記事一覧を取得
    news_list = soup.find(class_='news-list')

    # スクレイピング
    for section in news_list.find_all('section'):
        for target_word in const.TARGET_WORDS:
            if target_word in section.text:
                print(section.time.text)
                print(section.h2.text)
                print(const.BASE_URL + section.a["href"])


if __name__ == '__main__':
    main()
