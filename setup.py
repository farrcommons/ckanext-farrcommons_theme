from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-farrcommons_theme',
    version=version,
    description="Farrcommons theme",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Matthew Gamble',
    author_email='matthew.gamble@gmail.com',
    url='http://www.farrcommons.org',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.farrcommons_theme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
    	farrcommons_theme=ckanext.farrcommons_theme.plugin:FarrCommonsThemePlugin
	''',
)
