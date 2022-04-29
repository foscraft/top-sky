from calendar import c
from setuptools import setup

setup(
    name='sky_app',
    version='1.1',
    license='MIT',
    author='foscraft',
    author_email='anyaribari@gmail.com',
    description='A sample Flask app',
    packages=['sky_app'],
    platforms='any',
    install_requires=[
        'flask',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)