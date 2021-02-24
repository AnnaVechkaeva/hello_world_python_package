# Hello Wworld Python Package

Creating my first Python package

Can be installed using:
```
pip install git+https://github.com/AnnaVechkaeva/hello_world_python_package.git#egg=hello_world_python_package
```

To use the package:
```
>>> from hello_world_python_package.hello.SayHello import Hello
>>> h = Hello()
>>> h.sayhelloworld()
Hello World
>>> h.describe()
This is my first python package
```
