from folder_handler import get_recipe_folders
from gpt_handler import get_recipe_info
from file_writer import write_recipe_to_file
from config import RECIPE_FOLDER
from pathlib import Path

def main():
    # 1. フォルダ名をレシピ名として取得
    recipe_names = get_recipe_folders()

    # 2. 各レシピごとにChatGPTから情報取得 & 各フォルダに保存
    for recipe_name in recipe_names:
        folder_path = Path(RECIPE_FOLDER) / recipe_name
        print(f"処理中: {recipe_name}")

        content = get_recipe_info(recipe_name)
        write_recipe_to_file(folder_path, content)

    print("✅ 全レシピ処理が完了しました。")

if __name__ == "__main__":
    main()
