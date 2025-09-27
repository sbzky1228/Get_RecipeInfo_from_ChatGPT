from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_recipe_info(recipe_name: str) -> str:
    """
    ChatGPTにレシピ情報を生成してもらう
    """
    prompt = f"""
    以下のレシピ情報を作成してください。
    レシピ名: {recipe_name}

    出力フォーマットは必ず以下の順番・ラベル付きでお願いします:

    ■レシピタイトル（25文字以内）
    ■調理時間
    ■費用
    ■レシピコメント（80文字以内）
    ■材料（2人分）
    ■作り方
    ■きっかけ（120文字以内）
    ■おいしくなるコツ（120文字以内）
    ■カテゴリ
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "あなたは料理研究家です。"},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content.strip()
