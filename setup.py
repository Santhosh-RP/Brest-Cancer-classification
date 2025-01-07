from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='Breast_Cancer classification',  # Project name
    version='1.0.0',  # Version
    description='The mode lclassifies which is milligant or brilligant .',  # Short description
    author='santhosh Ailneni',
    author_email='santhoshch16195@gmail.com',
    url='https://github.com/Santhosh-RP/Brest-Cancer-classification',  # Project's homepage
    license='MIT',  # License type
    packages=find_packages(),  # Automatically finds Python packages in your directory
    install_requires=get_requirements('requirements.txt')
)
