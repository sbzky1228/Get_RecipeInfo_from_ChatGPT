# 📘 ChatGPT レシピ自動生成プログラム

このプロジェクトは、**フォルダ名をレシピ名として解釈し、OpenAI API を使ってレシピ情報を自動生成**し、
各レシピフォルダに "recipe.txt" を作成するツールです。既に ".txt" があるフォルダは**スキップ**されます。

---

## 📂 構成

"""
├─ main.py               # 全体のオーケストレーション
├─ config.py             # .env 読み込み & 設定値の取得（APIキー/フォルダパス）
├─ folder_handler.py     # RECIPE_FOLDER 配下のサブフォルダ名を列挙（= レシピ名）
├─ gpt_handler.py        # OpenAI API でレシピ本文を生成
├─ file_writer.py        # 各フォルダに recipe.txt を作成（既存 .txt があればスキップ）
├─ .env                  # OPENAI_API_KEY / RECIPE_FOLDER を定義
"""

---

## 🔧 必要要件

- Python 3.10 以上
- 主要ライブラリ
  """bash
  pip install openai python-dotenv
  """

---

## 🧾 .env（例）

".env" をプロジェクト直下に作成してください。

"""
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
RECIPE_FOLDER=C:\path\to\投稿素材
"""

> ※ "config.py" は ".env" から上記2つの値を読み込みます。  
> ※ もし "config.py" に**直書きの定数**が残っている場合は削除・無効化し、".env" を利用してください。

---

## ▶️ 使い方

1) 依存関係をインストール  
   """bash
   pip install openai python-dotenv
   """

2) ".env" を用意（"OPENAI_API_KEY", "RECIPE_FOLDER" を設定）

3) "RECIPE_FOLDER" 直下に、レシピ名のフォルダを配置（例: "唐揚げ", "豚汁" など）

4) 実行  
   """bash
   python main.py
   """

5) 出力  
   - 各レシピフォルダに "recipe.txt" が作成されます  
   - 既に ".txt" がある場合はスキップします（安全に再実行可）

---

## 🔁 処理フロー

1. **フォルダ列挙**: "folder_handler.get_recipe_folders()" が "RECIPE_FOLDER" 配下のサブフォルダ名を取得  
2. **レシピ生成**: "gpt_handler.get_recipe_info(recipe_name)" が OpenAI API で本文を生成  
3. **保存**: "file_writer.write_recipe_to_file(folder_path, content)" が "recipe.txt" を作成（既存 ".txt" があればスキップ）  
4. **完了**: "main.py" が対象すべてを順に処理

---

## 🧱 "recipe.txt" の出力フォーマット（想定）

"""
■レシピタイトル（25文字以内）
…（タイトル）

■調理時間
…（例: 約15分）

■費用
…（例: 500円前後）

■レシピコメント（80文字以内）
…

■材料（2人分）
…

■作り方
1. …
2. …

■きっかけ（120文字以内）
…

■おいしくなるコツ（120文字以内）
…

■カテゴリ
…（例: 夕食・時短料理）
"""

---

## 🧰 コードのポイント

- "file_writer.py" は**フォルダ内にすでに ".txt" がある場合は作成せずスキップ**します。
- "gpt_handler.py" は OpenAI の Chat Completions API（"gpt-4o-mini"）を利用します。
- "config.py" は ".env" を読み込んで "OPENAI_API_KEY" と "RECIPE_FOLDER" を参照します。

> セキュリティ: APIキーは**必ず ".env"** に置き、".gitignore" でリポジトリから除外してください。

---

## 📦 実行ファイル化（任意 / 上級者向け）

PyInstaller を使って単一実行ファイルにまとめることができます。  
"Get_Recipe_from_ChatGPT.spec" を調整の上、以下のように実行します。

"""bash
pip install pyinstaller
pyinstaller Get_Recipe_from_ChatGPT.spec
"""

生成物は "dist/" 配下に出力されます。

---

## ❗トラブルシュート

- **APIエラー**: APIキーが無効/権限不足の場合、生成に失敗します。".env" を再確認してください。  
- **フォルダが見つからない**: "RECIPE_FOLDER" の絶対パスが正しいか、存在権限があるか確認してください。  
- **再実行で内容が増えない**: 既存 ".txt" があるフォルダはスキップされます。上書きしたい場合は ".txt" を削除してから実行してください。

---

## ライセンス

本プロジェクトは個人利用を想定しています。API利用規約や各種著作権にご留意ください。
