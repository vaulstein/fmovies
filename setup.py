
from setuptools import setup

setup(name="fmovies",
      version="0.1",
      description="Download movies/T.V. series from fmovies/bmovies",
      url="http://vaulstein.github.com",
      author="Vaulstein Rodrigues",
      author_email="vaulstein@gmail.com",
      license='MIT',
      packages=["fmovies"],
      scripts=["bin/fmovies"],
      install_requires=[
            'BeautifulSoup4',
            'requests',
            'requests[security]',
            'youtube-dl'
      ],
      zip_safe=False)