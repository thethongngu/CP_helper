from codeforces import Codeforces
import argparse
import sys

parser = argparse.ArgumentParser(description='Competitve programming helper.')
parser.add_argument('-n', action='store', type=str, dest='contestUrl', help='Create new contest')
parser.add_argument('-p', action='store', type=str, dest='problemUrl', help='Create new problem')
parser.add_argument('-t', action='store', type=str, dest='problemTest', help='Test problem')
parser.add_argument('-c', action='store', type=str, dest='problemCompile', help='Compile problem')
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
	if site == "atcoder":
		pass
	if site == "csacademy":
		pass


# MAIN HERE
# ===============================================================================================

if sys.argv[1] == '-t':
	print "Testing problem ..."

if sys.argv[1] == '-c':
	print "Compiling problem ..."


if sys.argv[1] == '-n':
	print "Creating new contest ..."
	site = parseLink(sys.argv[2])
	createContest(site)

if sys.argv[1] == '-p':
	print "Creating new problem ..."
	site = parseLink(sys.argv[2])
	createProblem(site)	

