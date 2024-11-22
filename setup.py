from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='stalin',
    version='0.0.1',
    author='conpalos',
    author_email='cohenethan5@gmail.com',
    description="Annoyed that your code won't run? Send it to the gulag!",
    long_description=(Path(__file__).parent/'readme.md').read_text(),
    long_description_content_type='text/markdown',
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: Something something',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.10.12'
)