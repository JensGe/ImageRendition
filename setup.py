try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ImageRendition',
    'author': 'JensGe',
    'url': 'URL to get it at.',
    'download_url': 'https://www.github.com/JensGe/ImageRendition/',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ImageRendition'],
    'scripts': [],
    'name': 'ImageRendition'
}

setup(**config)