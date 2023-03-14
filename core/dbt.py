import os
import re
from collections import defaultdict

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

        self.docs = None
        self.model_type = None
        self.models = None

        self._load_docs_file()

    def load_yaml_file(self, model_type: str):
        """"""
        with open(os.path.join(self.root_path, DbtUtils.MODEL_ROOT, model_type) + '/schema.yml') as f:
            yaml_dict = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_dict

    def _load_docs_file(self) -> None:
        """"""
        contents = list()
        for md in os.listdir(self.root_path + '/docs'):
            with open(self.root_path + '/docs/' + md, 'r') as f:
                contents.append(f.read())

        pattern = re.compile(r'{%\s*docs\s*(?P<key>\w+)\s*%}(?P<value>.*?)'
                             r'{%\s*enddocs\s*%}', re.DOTALL)

        self.docs = {}
        for content in contents:
            for match in pattern.finditer(content):
                key = match.group('key')
                value = match.group('value').strip()
                self.docs[key] = value

    def _get_model_type(self) -> None:
        """"""
        self.model_type = list()
        model_dirs = os.path.join(self.root_path, DbtUtils.MODEL_ROOT)
        for folder in os.listdir(model_dirs):
            if folder not in DbtUtils.EXCLUDE_MODEL and os.path.join(model_dirs, folder):
                self.model_type.append(folder)

    def get_all_model(self, ):
        """"""
        self.models = defaultdict(lambda: defaultdict(defaultdict))
        self._get_model_type()

        for model_type in self.model_type:
            model_from_yaml = self.load_yaml_file(model_type=model_type)
            for model in model_from_yaml['models']:
                self.models['models'][model_type][model['name']] = {k: v for k, v in model.items() if k != 'name'}
                self.models['models']['all'][model['name']] = {k: v for k, v in model.items() if k != 'name'}

        return self.models

    def get_description(self, model: str) -> str:
        """"""
        description = self.models['models']['all'][model]['description']
        pattern = r'{{ doc\("(.+)"\) }}'
        if '{{' in description:
            doc_string = re.search(pattern, description).group(1)
            return self.docs[doc_string]
        return description


if __name__ == '__main__':
    dbt_utils = DbtUtils(root_path='/Users/jj.lee/workspace/data-cell/dbt-metric')
    models = dbt_utils.get_all_model()

    print(models['models']['common']['prep_referral'].get('description'))
    print(dbt_utils.get_description(model='prep_referral'))
