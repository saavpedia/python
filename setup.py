from setuptools import setup, find_packages

setup(
    name='SAAVpedia',

    version='0.6.6',

    description='SAAVpedia python library',

    author='Young-Mook Kang',

    author_email='ymkang@thylove.org',

    url='https://github.com/SAAVpedia/python',

    license='APACHE 2.0',

    packages=find_packages(exclude=['tests', 'resources', 'tmp', 'docs']),

    long_description=open('README.md').read(),

    zip_safe=False,

    #setup_requires=['nose>=1.0', 'datetime>=4.0', 'MySQL-python>=1.2', 'requests>=2.14'],

    install_requires=[
        'nose',
        'datetime',
        'requests',
    ],

    test_suite='nose.collector'
)