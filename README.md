# scraping_avengers

## Summary

シネマカフェ（<https://www.cinemacafe.net/>） からアベンジャーズやマーベルに関する記事を抽出する。

## Usage

```shell
# Incoming Webhook URLの設定
cd scraping_avengers
echo "WEBHOOK_URL = 'https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX'" > slack.py
```

```shell
# 実行
python main.py
```

## Requirements

* python3.7
* bs4==0.0.1
* requests==2.21.0
