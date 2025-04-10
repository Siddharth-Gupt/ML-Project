from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT='-e .'

def get_req(file_path:str)->List[str]:
    # this function will return list of req
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

    if HYPHEN_E_DOT in requirements :
        requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
    name="ML Project",
    author='SID',
    author_email='sidg972@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_req('requirments.txt')
)