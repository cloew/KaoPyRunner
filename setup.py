from distutils.core import setup

setup(name='kao_pyrunner',
      version='0.1',
      description='Kao Tessur Python Runner Utility to run and inspect Python code',
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['kao_pyrunner', 'kao_pyrunner/FunctionFinder', 'kao_pyrunner/Runner'],
     )