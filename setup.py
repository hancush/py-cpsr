from setuptools import setup

setup(name='py-cpsr',
      version='0.1',
      description='''A Python library for retrieving data from Inter-university
      Consortium for Political and Social Research (ICPSR)''',
      url='http://github.com/hancush/py-cpsr',
      author='Hannah Cushman',
      author_email='hannah.cushman@gmail.com',
      license='MIT',
      install_requires=['requests'],
      packages=['py_cpsr'],
      zip_safe=False)