#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        # For example:
        # 'numpy>=1.18',
    ],
    entry_points={
        'console_scripts': [
            # If you want to create any executable scripts
            # 'script_name = my_project.module:function',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18',
        # other core dependencies
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'flake8',
            # other development dependencies
        ]
    },
)

