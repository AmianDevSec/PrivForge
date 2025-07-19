from setuptools import setup, find_packages

setup(
    name='privforge',
    version='1.2.2',
    description='Linux Privilege Escalation Toolkit',
    author='AmianDevSec',
    author_email='amiandevsec@gmail.com',
    license='GPL-3.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'rich>=13.0.0',
        'pyfiglet',
        'psutil',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'pf=privforge.privforge:main',
        ],
    },
    package_data={
        'privforge.utils.data': ['binaries.json'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
    ],
)
