import json
from pathlib import Path

from settings import OPERATIONS_PATH
from src.operations import Operation


def load_operations(path: Path) -> list[dict]:
    """
    Загружает операции из файла json
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def load_operation_instances(operations):
    """
    Создает экземпляры операций из списка операций
    """

    operation_list = []
    for operation in operations:
        if operation:
            operation_instance = Operation(
                date=operation["date"],
                state=operation["state"],
                amount=operation["operationAmount"]["amount"],
                currency_name=operation["operationAmount"]["currency"]["name"],
                description=operation["description"],
                from_=operation.get("from", ""),
                to=operation["to"]
            )


