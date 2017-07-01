from contest import Contest
from bs4 import BeautifulSoup
import sys
import requests


class Codeforces(Contest):

	def __init__(self, url = "", name = "Codeforces", site = "", numProbs = 0, startTime = 0, endTime = 0, problems = None):
		if url == "":
			self.name = name
			self.site = startTime
			self.numProbs = numProbs
			self.startTime = startTime
			self.endTime = endTime
			self.problems = problems
		else:
			html = super(Codeforces, self).getRequest(url)
			self.name = self.parseName(html)
			

			# Will add startTime and endTime later
			"""
			self.startTime = self.parseStart(html)
			self.endTime = self.parseEnd(html)
			"""

			#self.numProbs
			#self.problems = self.parseProblem(hmtl)

	def parseName(self, html): 
		title = html.title.string
		title = title[12:-13]
		title = title.replace('(','')
		title = title.replace(')','')
		title = title.replace('#','')
		title = title.replace('.','')
		title = title.replace(' ','-')
		title = title.lower()
		return title

	def parseStart(self, html):
		pass

	def parseEnd(self, html):
		pass

	def parseProblem(self, html):
		pass


a = Codeforces("http://codeforces.com/contest/819")
print a.name

