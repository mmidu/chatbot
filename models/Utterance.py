import re

class Utterance:
	regex = None
	slots = []
	data = None

	def __init__(self, regex):
		self.regex, self.slots = self.build_utterance(regex)


	def build_utterance(self, text):
		slots = re.findall(r'\[(?P<slot>\b[A-Za-z]+[_[A-Za-z]+]*\b)\]', text)
		for i in range(len(slots)):
			slot = slots[i]
			reslot = '(?P<'+slot+'>\\w+)'
			text = re.sub(r'\['+slot+'\\]', '(?P<'+slot+'>\\\\w+)', text)
			text = re.sub(r'\s', '[\\\\W\\\\d]*', text)

			if i == 0:
				if text[0:len(reslot)] == reslot:
					text = '^[\\W\\d]*' + text
				else:
					text = '.*' + text

			if i == len(slots) - 1:
				if text[-len(reslot):len(text)] == reslot:
					text += '[\\W\\d]*$'
				else:
					text += '.*'

		return r'{}'.format(text), slots


	def check(self, text):
		match = re.match(self.regex, text, re.IGNORECASE)
		if match:
			self.data = {}
			for slot in self.slots:
				self.data[slot] = match.group(slot)
		return self.data