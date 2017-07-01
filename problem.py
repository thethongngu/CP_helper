from bs4 import BeautifulSoup
import sys
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
			
	@property
	def name(self):
		return self._name

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
