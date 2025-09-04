#setup.py

from setuptools import find_packages, setup # type: ignore
from typing import List

def get_requiremet():
    
    requirements_list: List[str] =[]
    
    try:
        with open('requirements.txt', "r") as file:
            lines = file.readlines()
            
            for line in lines:
                requirement = line.strip()
                
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
                    
    except FileNotFoundError:
        print(" File not found.")
        
    return requirements_list


setup(
    name= "network-security",
    author="Prasanth",
    version="0.0.1",
    packages=find_packages(),
    install_requires = get_requiremet()
    
)