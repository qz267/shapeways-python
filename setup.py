from distutils.core import setup
import sys

if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    sys.exit(1)

setup(name='shapeways2',
      version='0.1.8',
      description='Unofficial Shapeways python bindings',
      author='Paul Walker',
      author_email='pwalker@fvml.ca',
      url='https://github.com/pauldw/shapeways-python',
      packages=['shapeways2'],
      install_requires=['rauth >= 0.6.2'],
)
