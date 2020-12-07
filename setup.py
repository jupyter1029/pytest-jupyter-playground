
import pathlib
from setuptools import setup, find_packages
from jupyter_packaging import get_version

NAME = "pytest-jupyter"
PACKAGE_NAME = NAME.replace("-", "_")
DESCRIPTION = "A pytest plugin for testing Jupyter libraries and extensions."
VERSION = get_version(f"{PACKAGE_NAME}/_version.py")

HERE = pathlib.Path('.')
readme_path = HERE.joinpath('README.md')
README = readme_path.read_text()

# Build the extra requirements for each plugin.
EXTRA_REQUIRES = {
    'docs': [
        'Sphinx',
        'myst_parser',
        'pydata_sphinx_theme',
    ],
    'core': [
        'jupyter_core'
    ],
    'server': [
        'nbformat',
        'jupyter_core',
        'jupyter_server',
        'pytest-tornasync'
    ]
}

setup_args = dict(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    packages=find_packages('.', exclude=['tests', 'tests.*']),
    author='Jupyter Development Team',
    author_email='jupyter@googlegroups.com',
    url='http://jupyter.org',
    license='BSD',
    platforms="Linux, Mac OS X, Windows",
    keywords=['Jupyter', 'pytest'],
    install_requires=['pytest'],
    extras_require=EXTRA_REQUIRES,
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)


if __name__ == '__main__':
    setup(**setup_args)

