from setuptools import setup

setup(
    name='jPTDP',
    version='0.1.0',    
    description='Neural Network Models for Joint POS Tagging and Dependency Parsing',
    url='https://github.com/datquocnguyen/jPTDP',
    author='Dat Quoc Nguyen',
    author_email='dat.nguyen@students.mq.edu.au',
    license='GNU General Public License',
    packages=['jPTDP'],
    install_requires=['dynet==2.1.2'],
    package_data = {
        'jPTDP': ['model/model', 'model/model.params']
    }
)