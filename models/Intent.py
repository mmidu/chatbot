import re

class Intent:
	utterances = []
	question = None

	def __init__(self, utterances, question):
		self.utterances = utterances
		self.question = question

	def execute(self):
		text = input(self.question).strip()
		for utterance in self.utterances:
			matches = utterance.check(text)
			if matches:
				return matches
				break