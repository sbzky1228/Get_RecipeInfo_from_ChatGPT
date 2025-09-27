from pathlib import Path

def write_recipe_to_file(folder_path: str, content: str):
    """
    各レシピフォルダに recipe.txt を保存
    ただしフォルダ内に .txt ファイルが既に存在する場合はスキップ
    """
    folder = Path(folder_path)

    # フォルダ内に .txt ファイルが存在するか確認
    txt_files = list(folder.glob("*.txt"))
    if txt_files:
        print(f"✅ {folder.name} フォルダには既に .txt ファイルがあるためスキップしました")
        return

    file_path = folder / "recipe.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content + "\n")
        print(f"📝 {file_path} を作成しました")
