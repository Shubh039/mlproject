#build my entire machine learning model as a package
from setuptools import find_packages, setup 
from typing import List

HYPEN_E_DOT = "-e ." #this was in setup.py file to show the end of the file

def get_requirements(file_path:str)->List[str]:
    '''
        this function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author= 'Shubhank',
    author_email='shubhanks039@gmail.com',
    packages=find_packages(),
    intall_requires=get_requirements('requirements.txt')
)