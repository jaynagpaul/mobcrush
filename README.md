# mobcrush
Python Mobcrush API Wrapper

[![PyPI](https://img.shields.io/pypi/v/mobcrush.svg)](https://pypi.python.org/pypi/mobcrush/)
[![Documentation Status](https://readthedocs.org/projects/mobcrush/badge/?version=latest)](http://mobcrush.readthedocs.io/en/latest/?badge=latest)

Currently has minimal functionality, and should be considered as an **Alpha**.

## Usage
```python
>>> import mobcrush
>>> client = mobcrush.User('USERNAME', 'PASSWORD') # Login to the mobcrush API
>>> client.login()
>>> client.say('ChatroomID', 'This is my cool message!') #Limited functionality
>>> SpiesWithin = mobcrush.streamer('SpiesWithin') # Query a streamer
>>> SpiesWithin.name
SpiesWithin
>>> SpiesWithin.islive
False
>>> SpiesWithin.profilepic
'http://cdn.mobcrush.com/u/profile/556d0e16eab733432e6d6721/116060c5db'
>>> SpiesWithin.lastbroadcast.viewers
22
```
## Documentation
Documentation can be found at [documentation][doc].
[doc]: http://mobcrush.rtfd.org/en/latest

To build it yourself, do the following:
```
$ git clone https://github.com/jaynagpaul/mobcrush
$ cd mobcrush
$ cd docs
$ make html
```

## Installation

To install the library you can just run the following command:

```
python3 -m pip install -U mobcrush
```

To install the development version, do the following:

```
$ git clone https://github.com/jaynagpaul/mobcrush
$ cd mobcrush
$ python3 -m pip install -U setup.py
```

## TODO
See main.py
