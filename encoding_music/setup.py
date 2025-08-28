from setuptools import setup, find_packages

setup(
    name='encoding-music',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'urllib3>=1.26.0'
    ],
    python_requires='>=3.6'
)