from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    with open('requirements.txt') as f:
        # requirement_list = f.read().splitlines()
        requirement_list:List[str] = f.read().splitlines()
        # print(requirement_list)

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return requirement_list[:-1]

setup(
    name="sensor",
    version="0.0.2",
    author="vamsi",
    author_email="vkrishna238@outlook.com",
    packages = find_packages(),
    install_requires= get_requirements()
)