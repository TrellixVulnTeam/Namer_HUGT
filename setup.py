from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'NamerCLI',
    version = '1.0.0',
    author = 'dmw94',
    license = 'GPLv3',
    description = 'Lightweight CLI to predict demographics of a name and enumerate search queries for it.',
    url = 'https://github.com/dmw94/Namer',
    py_modules = ['NamerCLI'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        namercli=NamerCLI:cli
    '''
)