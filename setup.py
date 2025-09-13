from setuptools import setup ,find_packages
from typing import List

# this function is return the all requirements
req_list:List[str] = []
def get_requirements():
    try:
        with open("requirements.txt",'r') as f:
            lines = f.readlines()
            for line in lines:
                req = line.strip()
                if req and req !='-e .':
                    req_list.append(req)
    except Exception as e:
        print("Exception : ",e)
    
    return req_list

setup(
    Name = "Duplicate_Question_Pair",
    version = "0.0.1",
    author="Onkar Shinde",
    author_email="shindeonkar704@gmail.com",
    packages= find_packages(),
    install_require = get_requirements()
)