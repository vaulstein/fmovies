# FMOVIES


Let's you download movies/episodes from [Bmovies](https://bmovies.is/).

Don't wait for the stream to load.
Download latest TV Series in 720p resolution and watch them at your leisure.


# Installation

### Requirements

Make sure you have [Python](https://docs.npmjs.com/getting-started/installing-node) installed.

The script requires following dependencies and downloads them automatically.

1. Requests
2. Beautiful Soup
3. Youtube-dl

Install using pip globally (**Not available yet**):

```
$ sudo pip install fmovies

```

Or build from Source:

```
$ pip install virtualenv
```
```
$ virtualenv movies
```
```
$ source movies/bin/activate
```
```
$ git clone https://github.com/vaulstein/fmovies.git
```
```
$ cd fmovies
```
```
$ python setup.py install
```

## RUN

    fmovies <movie-name>

Select the movie you want to watch:

[![fmovies.png](https://s33.postimg.org/6kyypixzz/Screen_Shot_2017-11-23_at_10.04.04_AM.png)](https://postimg.org/image/b6v2xvjiz/)

## TODO

1. Fetch daily token dynamically
2. Code re-factoring
3. Deploy package on PyPi

## KNOWN ISSUES

Right now the code seems to download the wrong video. Working on fixing this.
Please stay tuned.