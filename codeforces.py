from contest import Contest
from problemCodeforces import ProblemCodeforces
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
			self.url = url

			html = super(Codeforces, self).getRequest(url)
			self.name = self.parseName(html)
			self.numProbs = self.parseNumProbs(html)
			self.problems = self.parseProblem(html)

			# Will add startTime and endTime later
			"""
			self.startTime = self.parseStart(html)
			self.endTime = self.parseEnd(html)
			"""

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

	def parseNumProbs(self, html):
		raw = html.find_all("td", class_="id")
		return len(raw)

	def parseStart(self, html):
		pass

	def parseEnd(self, html):
		pass

	def parseProblem(self, html):
		raw = html.find_all("td", class_="id")
		pros = []
		for item in raw:
			sub = item.a['href']
			link = "http://codeforces.com" + sub

			p = ProblemCodeforces(link)
			pros.append(p)

		return pros


#a = Codeforces("http://codeforces.com/contest/819")
