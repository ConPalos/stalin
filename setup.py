from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='stalin',
    version='0.0.1',
    author='conpalos',
    author_email='cohenethan5@gmail.com',
    description="Annoyed that your code won't run? Send it to the gulag!",
    long_description=(Path(__file__).parent/'README.md').read_text(),
    long_description_content_type='text/markdown',
    license=(Path(__file__).parent/'LICENSE').read_text(),
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: BSD-3',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.10.12'
)