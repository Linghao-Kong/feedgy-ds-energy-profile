import yaml


def parse_config(file_path: str) -> dict:
    """parse_config _summary_.

    Args:
        file_path (str): _description_

    Returns:
        dict: _description_
    """
    with open(file_path, encoding="utf-8") as file:
        return yaml.safe_load(file)
