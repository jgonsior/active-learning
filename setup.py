from distutils.core import setup

setup(name='Playground',
      version='1.0',
      description='Google Active Learning Playground',
      author='Yilei Yang',
      url='https://github.com/google/active-learning',
      packages=['playground','playground.utils','playground.sampling_methods'],
      package_dir={'playground':".",
                   'playground.utils':"./utils",
                   'playground.sampling_methods':"./sampling_methods"}
     )
