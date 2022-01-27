import pathlib
from setuptools import setup, find_packages


here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='sofastorage',
    version='0.0.4',
    description='Easy to use password manager',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SlumberDemon/SofaStorage',
    author='SlumberDemon',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='storage, password-storage, password-manager, storage-service, web-storage',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=['deta'],
    project_urls={
        'Bug Reports': 'https://github.com/SlumberDemon/SofaStorage/issues',
        'Source': 'https://github.com/SlumberDemon/SofaStorage',
    },
)
