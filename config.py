from dotenv import load_dotenv
import os

# .env を読み込む
load_dotenv()

# APIキーや設定値を環境変数から取得
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
RECIPE_FOLDER = os.getenv("RECIPE_FOLDER")