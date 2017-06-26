from contest import Contest
import argparse

parser = argparse.ArgumentParser(description='Competitve programming helper.')
parser.add_argument('-n', action='store', type=str, dest='contestUrl', help='Create new contest')
parser.add_argument('-t', action='store', type=str, dest='problemTest', help='Test problem')
parser.add_argument('-c', action='store', type=str, dest='problemCompile', help='Compile problem')
args = parser.parse_args()