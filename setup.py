#! /usr/bin/env python
from setuptools import setup, find_packages
from os import path, listdir
import re

pkg_name = 'dj_gui_api_server'
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), 'r') as f:
    long_description = f.read()

with open(path.join(here, pkg_name, 'version.py')) as f:
    exec(f.read())

with open(path.join(here, 'requirements.txt')) as f:
    requirements = ['{pkg} @ {target}#egg={pkg}'.format(
        pkg=re.search(r'/([A-Za-z0-9\-]+)\.git', r).group(1),
        target=r) if '+' in r else r for r in f.read().splitlines() if '#' not in r]

setup(
    name=pkg_name,
    version=__version__,
    author='DataJoint Neuro',
    author_email='info@vathes.com',
    description='A generic REST API for DataJoint pipelines.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://datajoint.io',
    packages=find_packages(exclude=['test*', 'docs']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=requirements,
    entry_points={
        'console_scripts': ['djgui_api={}.DJGUIAPIServer:run'.format(pkg_name)],
    },
)
