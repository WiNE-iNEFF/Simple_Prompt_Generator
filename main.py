import argparse
import random

def prompts(prompts="pr1.txt", num=10, artists=2):
	if prompts == "pr1.txt":
		prompt = open('pr1.txt', encoding='utf-8').read().splitlines()
	elif prompts == "pr2.txt":
		prompt = open('pr2.txt', encoding='utf-8').read().splitlines()

	vocab = len(prompt)
	generated = []
	artists_num = 0
	num_word = num

	while len(sorted(set(generated), key=lambda d: generated.index(d))) < num_word:
		rand = random.randint(0, vocab)
		if prompt[rand-1].startswith('art by') and artists_num < artists:
			artists_num +=1 
			generated.append(prompt[rand-1])
		elif not prompt[rand-1].startswith('art by'):
			generated.append(prompt[rand-1])

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
		prompts(args.prompts, int(args.num), int(args.artists))

if __name__ == "__main__":
	main = MainArg()
	main.parse()