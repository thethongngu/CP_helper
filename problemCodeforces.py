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
			print self.name

	def parseName(self, html):
		title = html.find("div", class_="title").string
		title = title[3:]
		print title

a = ProblemCodeforces("http://codeforces.com/problemset/problem/821/E")