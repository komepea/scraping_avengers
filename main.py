#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import json
import requests
import const
from bs4 import BeautifulSoup


def main():
    r = requests.get(const.BASE_URL + const.SCRAPING_URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    # 記事一覧を取得
    news_list = soup.find(class_='news-list')

    # スクレイピング処理
    for section in news_list.find_all('section'):
        # 1記事内に存在する検出文字列を捜索
        found_target_words = []
        for target_word in const.TARGET_WORDS:
            if target_word in section.text:
                # 記事投稿日時を取得
                published_date = datetime.datetime.strptime(
                        f"{section.time['datetime'][:10]} {section.time['datetime'][11:16]}", '%Y-%m-%d %H:%M')
                # 記事の投稿が12時間以内だった場合、通知対象とする
                if (datetime.datetime.today() - published_date).total_seconds() < 43200:
                    found_target_words.append(target_word)

        # 検出文字列があった時、Slackに通知する
        if found_target_words:
            post_message = f"検出文字列: {found_target_words}\n"\
                f"投稿日: {section.time.text}\n"\
                f"タイトル: {section.h2.text}\n"\
                f"URL: {const.BASE_URL + section.a['href']}"
            post_slack(post_message)


def post_slack(post_message):
    """Slackに通知する

    Args:
        post_message (str): Slack通知用メッセージ
    """
    post_json = {
        'text': f"New Post! ```{post_message}```",
        'channel': '#hiyoko',
        'username': 'Avengers Bot',
        'icon_emoji': ':avengers:'
    }
    requests.post(const.SLACK_URL, data=json.dumps(post_json))


if __name__ == '__main__':
    main()
