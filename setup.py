from setuptools import setup, find_packages

setup(
    name = 'pylogic',
    packages = find_packages(exclude=['.idea','.git','test']),
    version = '0.1.2',
    description = 'First description for the module',
    author = 'Francisco Bravo',
    author_email = 'fran_ase@hotmail.com',
    license='MIT',
    url = 'https://github.com/fran-bravo/pylogic-module',
    download_url = 'https://github.com/fran-bravo/pylogic-module/tarball/0.1.2',    
    keywords = ['testing', 'logic'],
    classifiers = ['Development Status :: 3 - Alpha',],
)
    
