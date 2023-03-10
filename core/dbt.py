from typing import Union, Type
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

    def load_yaml_file(self, model_type: str):
        """"""
        with open(os.path.join(self.root_path, DbtUtils.MODEL_ROOT, model_type)) as f:
            yaml_dict = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_dict

    def get_model_type(self):
        """"""
        model_type = list()
        model_dirs = os.path.join(self.root_path, DbtUtils.MODEL_ROOT)
        for folder in os.listdir(model_dirs):
            if folder not in DbtUtils.EXCLUDE_MODEL and os.path.join(model_dirs, folder):
                model_type.append(folder)

        return model_type


def get_all_model(given_model_type: Union[list, str], dbt_util: Type[DbtUtils]) -> None:
    """"""
    models = dict()
    for model in given_model_type:
        model_from_yaml = dbt_util.load_yaml_file(model_type=model)
        if not models:
            models['models'] = model_from_yaml['models']

    return


print(get_model_type(given_path='/Users/jj.lee/workspace/data-cell/dbt-metric'))
