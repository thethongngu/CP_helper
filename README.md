# cp-helper

Parsing tool for competitive programmer

## Requirements
- Python 2
- ```pip install requests``` (or equivalent)
- ```pip install beautifulsoup4``` (or equivalent)

## Features
- Parse problem statement or contest by url
- Check sample inputs and outputs

## How to use
- Edit your path in ```cp-helper.txt```
- Run ```python main.py``` to view help
- Example: 
	- ```python main.py -n http://codeforces.com/contest/822```: New contest 
	- ```python main.py -p http://codeforces.com/contest/822/problem/B```: New problem
	- ```python main.py -m ../codeforces-round-420-div-2```: active this contest to compiling and testing
	- ```python main.py -c A```: compile A.cpp in actived contest	
	- ```python main.py -t A```: test A.cpp in actived contest
