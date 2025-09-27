from pathlib import Path
from config import RECIPE_FOLDER

def get_recipe_folders():
    base = Path(RECIPE_FOLDER)
    if not base.exists():
        raise FileNotFoundError(f"{RECIPE_FOLDER} が存在しません")

    return [f.name for f in base.iterdir() if f.is_dir()]
