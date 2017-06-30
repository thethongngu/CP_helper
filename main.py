from contest import Contest
import argparse
import sys

parser = argparse.ArgumentParser(description='Competitve programming helper.')
parser.add_argument('-n', action='store', type=str, dest='contestUrl', help='Create new contest')
parser.add_argument('-p', action='store', type=str, dest='problemUrl', help='Create new problem')
parser.add_argument('-t', action='store', type=str, dest='problemTest', help='Test problem')
parser.add_argument('-c', action='store', type=str, dest='problemCompile', help='Compile problem')
args = parser.parse_args()

# MAIN HERE
# ===============================================================================================

# 
if sys.argv[1] == '-n':
	print "Creating new contest ..."

if sys.argv[1] == '-p':
	print "Creating new problem ..."

if sys.argv[1] == '-t':
	print "Testing problem ..."

if sys.argv[1] == '-c':
	print "Compiling problem ..."
