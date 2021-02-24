from setuptools import find_packages, setup

with open("requirements.txt") as reqfile:
	requirements = reqfile.read().split('\n')

setup(
    name='hello_world_python_package',
    url='https://github.com/AnnaVechkaeva/hello_world_python_package',
    author='Anna Vechkaeva',
    author_email='vechkaevaanna@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
    version='0.1',
    license='',
    description='My first python package',
)
