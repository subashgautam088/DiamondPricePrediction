from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]  # Isse requirements me jo packages hain uske pich 1 blank hota hain usko remove kar rahe hain

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements
    
    

setup(
    name= 'DiamondPricePrediction',
    version='0.0.1',
    author='Subash',
    author_email='subashgautam088@gmail.com',
    #install_requires=['pandas','numpy','seaborn'], OR
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages() # It find submodule in module
)