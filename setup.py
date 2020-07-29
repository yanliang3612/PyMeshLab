from setuptools import setup
import platform
import sys
import os
import urllib.request
import zipfile

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

f = open("PYML_VERSION", "r")
pymeshlabversion = f.read()

osused = platform.system()
if osused == 'Darwin':
    osused = 'macOS'

if (osused != 'Linux' and osused != 'Windows' and osused != 'macOS'):
    raise Exception("Operative System not supported")

if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 5):
    raise Exception("Must be using Python >= 3.5")

pythonversion = str(sys.version_info[0]) + '.' + str(sys.version_info[1])

baseurl = 'https://github.com/cnr-isti-vclab/PyMeshLab/releases/download/v' + pymeshlabversion + '/'
filename = 'PyMeshLab_' + osused + '_python' + pythonversion + '.zip'
url = baseurl + filename

print('Downloading ' + filename)
urllib.request.urlretrieve(url, this_directory + '/' + filename)

with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall('pymeshlab/')

os.remove(this_directory + '/' + filename)

setup(
    name='pymeshlab',
    version=pymeshlabversion,
    description='A Python interface to MeshLab',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cnr-isti-vclab/PyMeshLab',
    author='Alessandro Muntoni, Paolo Cignoni',
    author_email='alessandro.muntoni@isti.cnr.it',
    license='GPL3',
    packages=['pymeshlab', 'pymeshlab.tests'],
    include_package_data=True,
    zip_safe=False
)