from setuptools import setup
from setuptools import find_packages

setup(name='playground',
      version='1.0',
      description='Google Active Learning Playground',
      long_description=open("README.md", encoding="UTF-8").read(),
      long_description_content_type="text/markdown",
      author='Yilei Yang',
      url='https://github.com/google/active-learning',
      packages=find_packages()
     )
