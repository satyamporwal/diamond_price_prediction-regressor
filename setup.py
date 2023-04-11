from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = ('-e . ')

def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
    name="regressorproject",
    author='satyam porwal',
    version='10.1',
    author_email='satyamporwal8055@gmail.com',
    packages=find_packages()
)