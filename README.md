# cp-helper

Parsing tool for competitive programmer

## Requirements
- Python 2
- ```requests``` module of Python
- ```beautifulsoup4``` module of Python

## Features
- Parse problem statement or contest by url (only for Codeforces now)
- Check sample inputs and outputs

## How to use
- Edit your path in ```cp-helper.ini```
- Run ```python main.py``` to view help
- Example: 
	- ```python main.py -n [contest url]```: New contest 
	- ```python main.py -p [problem url]```: New problem
	- ```python main.py -m [path]```: active this contest to compiling and testing
	- ```python main.py -c [A, B, C, D, E]```: compile A.cpp in actived contest	
	- ```python main.py -t [A, B, C, D, E]```: test A.cpp in actived contest
	- ```python main.py -o [A, B, C, D, E, inp]```: open .cpp, in or out files
