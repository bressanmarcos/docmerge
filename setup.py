from setuptools import setup, find_packages
from os.path import join, dirname

with open(join(dirname(__file__), 'docmerge', '__version__.py')) as v:
    __version__ = None
    exec(v.read().strip())

with open('README.rst') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

with open('requirements-dev.txt') as f:
    requirements_dev = [line.strip() for line in f.readlines()]


setup(
    name="docmerge",
    packages=find_packages(include=['docmerge*']),
    version=__version__,
    author="Marcos Bressan",
    author_email="bressan@dee.ufc.br",
    description="A simple tool to merge docstrings from parent classes to child classes.",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url="https://github.com/bigdatabr/docmerge",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=True,
    install_requires=requirements,
    extras_require={
        'dev': requirements_dev
    }
)
