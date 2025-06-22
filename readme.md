# QRコード生成Webアプリ

このアプリは、入力した文字列からQRコードを生成してブラウザに表示する簡単なWebアプリです。Flask（Python）と Tailwind CSS を使用して構築されています。

---

## ✨ 使用技術

* Python 3.x
* Flask
* qrcode
* Pillow
* Tailwind CSS（CDN）

---

## ὎6 セットアップ方法

### 1. リポジトリをクローン

```bash
git clone https://github.com/yut0takagi/qr-code-gen
cd qr-code-app
```

### 2. 仮想環境を作成（任意）

```bash
python -m venv venv
source venv/bin/activate  # Windowsなら venv\Scripts\activate
```

### 3. 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

### 4. Flaskアプリを実行

```bash
python app.py
```

### 5. ブラウザでアクセス

```
http://127.0.0.1:5000/
```

---

## ★ 使い方

1. テキストボックスに入力
2. 「QRコードを生成」ボタンをクリック
3. QRコードが表示

---

## 📁 ディレクトリ構成

```
qr-code-app/
├── app.py                 # Flask本体
├── requirements.txt       # 必要パッケージ
└── templates/
    └── index.html         # Tailwind適用HTML
```

---

## 📌 改良アイデア（任意）

* QR画像をページ内にBase64で埋め込み表示
* 色・サイズのカスタマイズ
* 履歴機能（セッション or DB）
* 画像ダウンロードボタン

---
