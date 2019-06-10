#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import requests
import const
from bs4 import BeautifulSoup


def main():
    r = requests.get(const.BASE_URL + const.SCRAPING_URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    # 記事一覧を取得
    news_list = soup.find(class_='news-list')

    # スクレイピング処理
    post_message = ''
    for section in news_list.find_all('section'):
        for target_word in const.TARGET_WORDS:
            if target_word in section.text:
                # 記事投稿日時を取得
                published_date = datetime.datetime.strptime(
                    f"{section.time['datetime'][:10]} {section.time['datetime'][11:16]}", '%Y-%m-%d %H:%M')
                # 記事の投稿が12時間以内だった場合、post_messageに追加する
                if (datetime.datetime.today() - published_date).total_seconds() < 43200:
                    post_message += f"```検出文字列：{target_word}\n"\
                        f"投稿日：{section.time.text}\n"\
                        f"タイトル：{section.h2.text}\n"\
                        f"{const.BASE_URL + section.a['href']}```\n"

    # 新しい記事が見つかった場合Slackに通知する
    if post_message:
        post_json = {
            'token': 'xoxp-XXXXXXXXXX-XXXXXXXXXXXX-XXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXX',   # 通知先のtokenを記載
            'text': f"New Post! {post_message}",
            'channel': '#hiyoko',   # 通知先のチャンネル
            'username': 'Avengers Bot',
            'icon_emoji': ':avengers:'
        }

        requests.post('https://slack.com/api/chat.postMessage', data=post_json)


if __name__ == '__main__':
    main()
