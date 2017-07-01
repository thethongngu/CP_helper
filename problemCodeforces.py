from bs4 import BeautifulSoup
from problem import Problem
import sys
import requests

class ProblemCodeforces(Problem):

	def __init__(self, url = "", name = "", level = "", timeLimit = 0, memoryLimit = 0, numSample = 0, inputs = [], outputs = []):
		if url == "":
			self.name = name
			self.level = level
			self.timeLimit = timeLimit
			self.memoryLimit = memoryLimit
			self.numSample = numSample
			self.inputs = inputs
			self.outputs = outputs
		else:
			html = super(ProblemCodeforces, self).getRequest(url)

			header = html.find("div", class_="header")
			self.name = self.parseName(header)
			self.level = self.parseLevel(header)
			self.timeLimit = self.parseTimeLimit(header)
			self.memoryLimit = self.parseMemoryLimit(header)

			header = html.find("div", class_="sample-tests")
			print header

			self.numSample, self.inputs, self.outputs = self.parseSample(header)

			print self.name
			print self.level
			print self.timeLimit
			print self.memoryLimit
			print self.numSample
			print self.inputs[1]
			print self.outputs[1]

	def parseName(self, html):
		title = html.find("div", class_="title").string
		title = title[3:]
		return title

	def parseLevel(self, html):
		level = html.find("div", class_="title").string
		level = level[0]
		return level

	def parseTimeLimit(self, html):
		raw = html.find("div", class_="time-limit")
		time = str(raw)
		first = time.find('</div>')
		second = time.find('</div>', first + 1)
		time = time[first + 6: second]
		time = time.replace(' seconds','')
		return int(time)

	def parseMemoryLimit(self, html):
		raw = html.find("div", class_="memory-limit")
		memory = str(raw)
		first = memory.find('</div>')
		second = memory.find('</div>', first + 1)
		memory = memory[first + 6: second]
		memory = memory.replace(' megabytes','')
		return int(memory)

	def parseSample(self, html):
		inps = [];  
		outs = [];

		raw = html.find_all("pre")
		for i in range(len(raw)):
			item = raw[i]

			if i % 2 == 0:
				inp = str(item)
				inp = inp[5:-11]
				inp = inp.replace('<br/>','\n')
				inps.append(inp)
			else:
				out = str(item)
				out = out[5:-11]
				out = out.replace('<br/>','\n')
				outs.append(out)

		return (len(raw) / 2, inps, outs)

#a = ProblemCodeforces("http://codeforces.com/problemset/problem/821/E")
#b = ProblemCodeforces("http://codeforces.com/contest/819/problem/A")