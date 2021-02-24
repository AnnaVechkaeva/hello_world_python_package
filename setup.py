from setuptools import find_packages, setup

setup(
    name='hello_world_python_package',
    url='https://github.com/AnnaVechkaeva/hello_world_python_package',
    author='Anna Vechkaeva',
    author_email='vechkaevaanna@gmail.com',
    packages=find_packages(),
    install_requires=['numpy'],
    version='0.1',
    license='',
    description='My first python package',
)
