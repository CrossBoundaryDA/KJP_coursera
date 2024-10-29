import yaml
import os
import sys
import pandas as pd

def get_onedrive_root(config_path: str = "user_config.yml") -> str:
    """Gets the onedrive root folder in an OS- and user-independent way
    Args:
        config_path (str, optional): A full or relative path to the user_config
        containing (among other things) the onedrive folder location on the local
        system. Defaults to "user_config.yml".
    Returns:
        str: The full path to the onedrive root folder, formatted correctly for OS
    """
    if not os.path.isabs(config_path):
        config_path = os.path.join(os.path.dirname(__file__), config_path)
    with open(config_path, "r") as stream:
        data = yaml.safe_load(stream)
    return data["onedrive_root"]


def function_to_square_numbers(x):
    return x**2