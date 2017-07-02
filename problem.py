from bs4 import BeautifulSoup
from shutil import copyfile
import sys
import os
import requests


class Problem(object):

	# For check exception of request
	def getRequest(self, url):
		try:
			r = requests.get(url);
			html = BeautifulSoup(r.text, 'html.parser')
		except: 
			print "Fuck your network! Cannot connect to server"
			sys.exit()
		return html

	def writeSolutions(self, location, header):
		filename = location + '/' + self.level + '.cpp'
		copyfile(header, filename)

	def writeSamples(self, location):
		for i in range(self.numSample):
			item = self.inputs[i]
			filename = location + '/in-' + self.level.lower() + '-' + str(i + 1) + '.inp'
			
			f = open(filename, "w+")
			f.write(item)
			f.close()

			item = self.outputs[i]
			filename = location + '/out-' + self.level.lower() + '-' + str(i + 1) + '.out'

			f = open(filename, "w+")
			f.write(item)
			f.close()

	def writeFile(self, path, header, relatedContest):

		path = path[:-1]
		location = path + '/' + relatedContest.name
		
		if not os.path.exists(location):
   			relatedContest.writeFile(path, header)
   		else:
   			print "[Careful !!!] Problem existed! Do you want to override all data? (y/n): "
   			ans = raw_input()
   			if (ans == 'y'):
   				 self.writeSolutions(location, header)
   			else:
   				sys.exit()
		
	@property
	def name(self):
		return self._name

	@property
	def url(self):
		return self._url

	@property
	def level(self):
		return self._level

	@property
	def timeLimit(self):
		return self._timeLimit

	@property
	def memoryLimit(self):
		return self._memoryLimit

	@property
	def numSample(self):
		return self._numSample

	@property
	def inputs(self):
		return self._inputs

	@property
	def outputs(self):
		return self._outputs

	@url.setter
	def url(self, newUrl):
		self._url = newUrl

	@name.setter
	def name(self, newName):
		self._name = newName

	@level.setter
	def level(self, newLevel):
		self._level = newLevel

	@timeLimit.setter
	def timeLimit(self, newTimeLimit):
		self._timeLimit = newTimeLimit

	@memoryLimit.setter
	def memoryLimit(self, newMemoryLimit):
		self._memoryLimit = newMemoryLimit

	@numSample.setter
	def numSample(self, newNumSample):
		self._numSample = newNumSample

	@inputs.setter
	def inputs(self, newInputs):
		self._inputs = newInputs

	@outputs.setter
	def outputs(self, newOutputs):
		self._outputs = newOutputs
