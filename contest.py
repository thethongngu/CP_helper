from problem import Problem

class Contest:

	def __init__(self, name = "", site = "", numProbs = 0, startTime = 0, endTime = 0, problems = None):
		self.name = name
		self.site = site
		self.numProbs = numProbs
		self.startTime = startTime
		self.endTime = endTime
		self.problems = problems
