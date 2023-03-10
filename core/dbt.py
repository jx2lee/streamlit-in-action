from collections import defaultdict
from typing import Union, Type, Dict, Any
import os
import yaml


class DbtYamlParser:
    """"""

    def __init__(self, root_path: str):
        self.file_loader = DbtUtils(root_path=root_path)

        self.model_type = self.file_loader.get_model_type()
        self.models = None  # todo:
        self.ref_models = None  # todo:


class DbtUtils:
    MODEL_ROOT = 'models'
    EXCLUDE_MODEL = ['metric']

    def __init__(self, root_path: str):
        self.root_path = root_path

        self.model_type = None
        self.models = None

    def load_yaml_file(self, model_type: str):
        """"""
        with open(os.path.join(self.root_path, DbtUtils.MODEL_ROOT, model_type) + '/schema.yml') as f:
            yaml_dict = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_dict

    def _get_model_type(self) -> None:
        """"""
        self.model_type = list()
        model_dirs = os.path.join(self.root_path, DbtUtils.MODEL_ROOT)
        for folder in os.listdir(model_dirs):
            if folder not in DbtUtils.EXCLUDE_MODEL and os.path.join(model_dirs, folder):
                self.model_type.append(folder)

    def get_all_model(self, ):
        """"""
        self.models = defaultdict(lambda: defaultdict(list))
        self._get_model_type()

        for model in self.model_type:
            model_from_yaml = dbt_utils.load_yaml_file(model_type=model)
            self.models['models'][model] = model_from_yaml['models']
        print(self.models['models']['staging'])
        return self.models


if __name__ == '__main__':
    dbt_utils = DbtUtils(root_path='/Users/jj.lee/workspace/data-cell/dbt-metric')
    dbt_utils.get_all_model()