from problem import Problem
from bs4 import BeautifulSoup
import os
import requests
import sys

class Contest(object):

	# For check exception of request
	def getRequest(self, url):
		try:
			r = requests.get(url);
			html = BeautifulSoup(r.text, 'html.parser')
		except: 
			print "Fuck your network! Cannot connect to server"
			sys.exit()
		return html

	def __init__(self, name = "", site = "", numProbs = 0, startTime = 0, endTime = 0, problems = None):
		self.name = name
		self.site = site
		self.numProbs = numProbs
		self.startTime = startTime
		self.endTime = endTime
		self.problems = problems

	# create folder and input ouput files
	def writeFile(self, path, header):

		
		location = path + '/' + self.name

		if not os.path.exists(location):
   			os.makedirs(location)
   		else:
   			print "[Careful !!!] Contest existed! Do you want to override all data? (y/n): "
   			ans = raw_input()
   			if (ans == 'y'):
   				 pass
   			else:
   				sys.exit()

   		for pro in self.problems:
   			pro.writeSolutions(location, header)
   			pro.writeSamples(location)

	@property
	def name(self):
		return self._name

	@property
	def site(self):
		return self._site

	@property
	def numProbs(self):
		return self._numProbs

	@property
	def startTime(self):
		return self._startTime

	@property
	def endTime(self):
		return self._endTime

	@property
	def problems(self):
		return self._problems

	@name.setter
	def name(self, newName):
		self._name = newName

	@site.setter
	def site(self, newSite):
		self._site = newSite

	@numProbs.setter
	def numProbs(self, newNumProbs):
		self._numProbs = newNumProbs

	@startTime.setter
	def startTime(self, newStartTime):
		self._startTime = newStartTime

	@endTime.setter
	def endTime(self, newEndTime):
		self._endTime = newEndTime

	@problems.setter
	def problems(self, newProblems):
		self._problems = newProblems
