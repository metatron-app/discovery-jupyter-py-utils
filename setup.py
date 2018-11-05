from setuptools import setup, find_packages

setup(
    name='pymetis',
    version='0.0.3',
    packages=find_packages(exclude=['tests*']),
    license='Apache 2.0',
    description='metis python package',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/metatron-app/discovery-jupyter-py-utils',
    author='metatron',
    author_email='metatron@sk.com'
)
