from setuptools import setup

setup(name='playground',
      version='1.0',
      description='Google Active Learning Playground',
      long_description=open("README.md", encoding="UTF-8").read(),
      long_description_content_type="text/markdown",
      author='Yilei Yang',
      url='https://github.com/google/active-learning',
      packages=['playground','playground.utils','playground.sampling_methods'],
      package_dir={'playground':".",
                   'playground.utils':"./utils",
                   'playground.sampling_methods':"./sampling_methods"}
     )
