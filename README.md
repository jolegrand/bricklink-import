BrickLink Wanted List Import
============================

The [BrickLink website](http://www.bricklink.com/), where you can buy and sell 
LEGO parts, sets and minifigures, lacks the ability to import easily multiple
wanted lists. 

This application allows to import wanted list from a BrickStock `.bsx` file in
a given bricklink wanted list easily.

bricklink-import is written in [Python](http://www.python.org/).

*This application and its author are in no way affiliated with BrickLink 
Limited.*


Requirements
------------

* Python
* Selenium


Installation
------------

On most UNIX-like systems, you can clone the repository and execute
the python file.

``` sh
git clone  git@github.com:jolegrand/bricklink-import.git
cd bricklink-import
```

You will need the geckodriver to run firefox through Selenium

```
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver-v0.24.0-linux64.tar.gz
export PATH=$PATH:$PWD

```

You can now run bricklink-import

```
python3 bricklink-import.py -h
```

Usage
-----

```
usage: bricklink-import [-h] [--version] [-v] [-u USERNAME] [-p PASSWORD] [-l] 
                   [-c] [-e ID]

Export a BrickLink wanted list.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  #v, --verbose         be verbose
  -u USERNAME, --username USERNAME
                        username on BrickLink
  -p PASSWORD, --password PASSWORD
                        password on BrickLink (omit for prompt)
  -f FILE		path to the .bsx file to import
  -n NAME 		Name of the bricklink list. If NAME doesn't exist, it will be created.
```


Example
--------

python3 bricklink-import.py -u USERNAME -p PASSWORD -f toto.bsx -n toto