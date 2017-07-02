from codeforces import Codeforces
from problemCodeforces import ProblemCodeforces
import argparse
import ConfigParser
import sys
import os

parser = argparse.ArgumentParser(description='Competitve programming helper.')
parser.add_argument('-n', action='store', type=str, dest='contestUrl', help='Create new contest')
parser.add_argument('-p', action='store', type=str, dest='problemUrl', help='Create new problem')
parser.add_argument('-o', action='store', type=str, dest='filename', help='Open solution with sublime text')
parser.add_argument('-t', action='store', type=str, dest='filename', help='Test problem (FILENAME = [A, B, C, ...])')
parser.add_argument('-c', action='store', type=str, dest='filename', help='Compile problem (FILENAME = [A, B, C, ...])')
parser.add_argument('-m', action='store', type=str, dest='currentContest', help='Move to another contest directory')
args = parser.parse_args()

def parseLink(url):
	if url.find("codeforces.com") != -1:
		return "codeforces"
	if url.find("atcoder.jp") != -1:
		return "atcoder.jp"
	if url.find("csacademy.com") != -1:
		return "csacademy"

# Responsible for create and maintain folder of contest
def createContest(site):
	if site == "codeforces":
		newContest = Codeforces(sys.argv[2])
		newContest.writeFile(curPath, header)
		activeContest(curPath + '/' + newContest.name)
	if site == "atcoder":
		pass
	if site == "csacademy":
		pass

def createProblem(site):
	if site == "codeforces":
		newProblem = ProblemCodeforces(sys.argv[2])
		linkContest = newProblem.linkOfContest()

		relatedContest = Codeforces(linkContest)
		newProblem.writeFile(curPath, header, relatedContest)
		activeContest(curPath + '/' + relatedContest.name)

	if site == "atcoder":
		pass
	if site == "csacademy":
		pass

def readInfo():
	iniFile = ConfigParser.ConfigParser()
	iniFile.read('cp-helper.ini')
	curPath = iniFile.get('Data', 'path')
	header = iniFile.get('Data', 'header')
	compileCom = iniFile.get('Data', 'compileCom')
	exeCom = iniFile.get('Data', 'exeCom')
	currentContest = iniFile.get('Data', 'currentContest')

	return (curPath, header, compileCom, exeCom, currentContest)

def activeContest(location):
	iniFile = ConfigParser.ConfigParser()
	cfgFile = open("cp-helper.ini",'w')

	iniFile.add_section('Data')
	iniFile.set('Data', 'path', curPath)
	iniFile.set('Data', 'header', header)
	iniFile.set('Data', 'compileCom', compileCom)
	iniFile.set('Data', 'exeCom', exeCom)
	iniFile.set('Data', 'currentContest', location)
	iniFile.write(cfgFile)

	cfgFile.close()

	print "Contest activated!"

# MAIN HERE
# ===============================================================================================

curPath, header, compileCom, exeCom, currentContest = readInfo()

if sys.argv[1] == '-o':
	if os.path.exists(currentContest + '/'):
		command = "sublime " + currentContest + '/' + sys.argv[2] + '.cpp'
		print command
		os.system(command)
	else:
		print "Contest have not created yet"

if sys.argv[1] == '-m':
	activeContest(sys.argv[2])

if sys.argv[1] == '-t':
	print "Current contest: " + currentContest
	print ""
	print "Testing problem ..."
	
	location = currentContest + '/' + sys.argv[2] + ".cpp"
	command = exeCom.replace("<filename>", location)

	num = 0
	while (1):
		num += 1
		inpPath = currentContest + '/in-' + sys.argv[2].lower() + '-' + str(num) + '.inp'
		if os.path.exists(inpPath):
			command = command + ' < ' + inpPath
			print "==============================="
			print "TEST " + str(num) + ":"
			print ""

			print "YOUR OUTPUT:"
			os.system(command)

			print ""
			print "CORRECT ANSWER:"
			outPath = currentContest + '/out-' + sys.argv[2].lower() + '-' + str(num) + '.out'
			f = open(outPath, "r")
			out = f.readlines()
			for item in out:
				sys.stdout.write(item)
			print ""

   		else:
   			break		

	print "==============================="
   	print "Done!"

if sys.argv[1] == '-c':
	print "Compiling problem ..."
	print "Current contest: " + currentContest + '/' + sys.argv[2] + ".cpp"
	command = compileCom.replace("<filename>",currentContest + '/' + sys.argv[2] + ".cpp")
	os.system(command)
	print "Compiled completed!"

if sys.argv[1] == '-n':
	print "Creating new contest ..."
	site = parseLink(sys.argv[2])
	createContest(site)

if sys.argv[1] == '-p':
	print "Creating new problem ..."
	site = parseLink(sys.argv[2])
	createProblem(site)	

