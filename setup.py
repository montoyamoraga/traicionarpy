import setuptools
from codecs import open
from os import path

# taken from https://tom-christie.github.io/articles/pypi/
here = path.abspath(path.dirname(__file__))

# taken from https://tom-christie.github.io/articles/pypi/
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='traicionar',
    version='0.0.3',
    author='montoyamoraga',
    author_email='montoyamoraga@gmail.com',
    description='library for electronic betrayal',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/montoyamoraga/traicionar.py',
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        'Development Status :: 3 - Alpha',
    ],
)
