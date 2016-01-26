#!/usr/bin/env python
# -*- conding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='ipython-sparkline',
    version='0.0.1',
    description='sparkline in ipython-notebook (jupyter)',
    long_description=long_description,
    author='Ryoji Ishii',
    author_email='airtoxin@icloud.com',
    license='MIT',
    url='https://github.com/airtoxin/ipython-sparkline',
    packages=find_packages(exclude=['build', 'doc', 'template']),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: IPython',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    keywords='ipython jupyter animation array',
    install_requires=[
        'ipython',
        'Jinja2'
    ],
    tests_require=['pytest', 'tox']
)
