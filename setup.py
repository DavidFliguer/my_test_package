from setuptools import setup, find_packages

setup(
    name="my_test_package",
    version="0.0.1",
    author="X",
    description="Y",
    author_email='Z',
    url='some_url',
    include_package_data=True,
    package_data={'': ['*.txt', 'data/my_other_file.txt']},
    packages=find_packages(),
    install_requires=[
        'requests',
    ])
