from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
description = 'Fork of: The official Python3 Domo API SDK - Domo, Inc.'
long_description = 'See https://github.com/domoinc/domo-python-sdk for more details.'

setup(
    name='pydomo jfv1',
    version='1.0.0',
    #description=description,
    #long_description=long_description,
    #author='Joe Reynolds',
    #author_email='j7f7r7@gmail.com',
    #url='https://github.com/jf-grpo/domo-python-sdk',
    #download_url='https://github.com/jf-grpo/domo-python-sdk',
    #keywords='domo api sdk',
    #license='MIT',
    packages=find_packages(exclude=['examples']),
    install_requires=[
        'pandas',
        'requests',
        'requests_toolbelt',
    ],
    python_requires='>=3',
)
