def plural(word):
	if(word.endswith('y')):
		return word[:-1] + 'ies'
	if word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
		return word + 'es'
	if word.endswith('an'):
		return word[:-2] + 'en'
	return word + 's'
print(plural('dutch'))