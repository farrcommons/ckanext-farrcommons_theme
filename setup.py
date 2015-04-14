from setuptools import setup, find_packages
import sys, os

version = '0.1'

def get_data_files(directory):
    dir = os.path.dirname(__file__)
    abs_dir = os.path.join(dir,'ckanext/farrcommons_theme/', directory)
    paths = []
    for root, dirs, files in os.walk(abs_dir):
        root = os.path.relpath(root,abs_dir)
        paths += [os.path.join(directory,root,file) for file in files]
    return paths

template_data = get_data_files('templates/')
public_data = get_data_files('public/')

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
    package_data={'ckanext.farrcommons_theme': public_data + template_data },
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
    	farrcommons_theme=ckanext.farrcommons_theme.plugin:FarrCommonsThemePlugin
	''',
)
