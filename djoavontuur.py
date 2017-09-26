import time
import os
import platform
# local imports
import loader

artpath = 'art.json'
artdata = loader.load(artpath)
storypath = 'story.json'
storydata = loader.load(storypath)

if platform.system() == "Windows":
	osclear = "cls"
	os.system("title Het DJO Avontuur")
else:
	osclear = "clear"

def printArt(id):
	linelist = artdata[id]['lines']
	for line in linelist:
		time.sleep(.1)
		print(line)

def printStory(id):
	prompt = storydata[id]['text']
	if isinstance(prompt, str):
		answer = input(prompt+': ').lower()
		processAnswer(answer, id)
	elif isinstance(prompt, list):
		for item in prompt[:-1]:
			print(item)
			time.sleep(1)
		answer = input(prompt[-1]+': ').lower()
		processAnswer(answer, id)

def processAnswer(answer, id):
	answers = storydata[id]['answers']
	replies = storydata[id]['replies']
	try:
		goto = answers[answer]
		print(replies[goto])
		time.sleep(1)
		try:
			printStory(goto)
		except:
			print('niks gevonden met dit id')
	except:
		print(answer+' is geen goede optie, probeer het opnieuw')
		printStory(id)

def mainSequence():
	os.system(osclear)
	printArt('title')
	time.sleep(1)
	printStory('start')
	printArt('gameover')
	raise Exception("kek")

mainSequence()
