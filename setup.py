from setuptools import setup, find_packages


setup(
    name="dockerapp",
    packages=find_packages(),
    version='0.0.1',
    description='test package for deploying using docker',
    author='Peter de Zwart',
    license='',
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    install_requires=[],
    extras_require={
        'lint': [],
        'tests': ['pytest==5.4.2']
    },
)
