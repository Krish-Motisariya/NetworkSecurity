import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
import os
import numpy as np
import pandas as pd
# import dill
import pickle

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as yml_file:
            return yaml.safe_load(yml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    
def write_yaml(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as yml_file:
            yaml.dump(content, yml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e