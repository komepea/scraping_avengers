# スクレイピング対象のURL（シネマカフェ）
BASE_URL = "https://www.cinemacafe.net"
SCRAPING_URL = "/category/cinema/foreign/latest/"

# 検出文字列
TARGET_WORDS = ["アベンジャーズ", "MARVEL",
                "アイアンマン", "ロバート・ダウニー", "ペッパー・ポッツ", "グウィネス・パルトロー",
                "キャプテン・アメリカ", "クリス・エヴァンス", "ウィンター・ソルジャー",
                "マイティ・ソー", "クリス・ヘムズワース",
                "ブラック・ウィドウ", " ナターシャ・ロマノフ", "スカーレット・ヨハンソン",
                "スパイダーマン", "トム・ホランド",
                "アントマン", "ワスプ",
                "ハルク",
                "ガーディアンズ・オブ・ギャラクシー", "クイル",
                "ドクター・ストレンジ",
                "ブラックパンサー", "ブラック・パンサー",
                "キャプテン・マーベル", "キャロル・ダンバース",
                "ワンダ・マキシモフ", "スカーレット・ウィッチ", "エリザベス・オルセン",
                "クリント・バートン",
                "サノス"]

# Incoming WebhookのURL
SLACK_URL = 'https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX'
