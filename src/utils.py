import json
from pathlib import Path

from settings import OPERATIONS_PATH


def load_operations(path: Path) -> list[dict]:
    """
    Загружает операции из файла json
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


