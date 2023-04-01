import argparse
import random

def prompts(prompts, num_word, artists):
	if prompts == "pr1.txt":
		prompt = open('pr1.txt', encoding='utf-8').read().splitlines()
	elif prompts == "pr2.txt":
		prompt = open('pr2.txt', encoding='utf-8').read().splitlines()

	if num_word == None:
		num_word = 10
	if artists == None:
		artists = 2

	generated = []
	artists_num = 0

	while len(sorted(set(generated), key=lambda d: generated.index(d))) < int(num_word):
		rand = random.choice(prompt)
		if rand.startswith('art by') and int(artists_num) < int(artists):
			artists_num +=1 
			generated.append(rand)
		elif not rand.startswith('art by'):
			generated.append(rand)

	print(', '.join(set(generated)))

class MainArg():
	def __init__(self):
		pass

	def parse(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('-p', '--prompts', help='Prompt version', required=True)
		parser.add_argument('-n', '--num', help='Num of prompts (Standart: 10, MAX: 20)', required=False)
		parser.add_argument('-a', '--artists', help='How many artists use in prompt (Standart: 2)', required=False)

		args = parser.parse_args()
		prompts(args.prompts, args.num, args.artists)

if __name__ == "__main__":
	main = MainArg()
	main.parse()