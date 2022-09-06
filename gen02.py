import random
prompt = open('prompttext2.txt').read().splitlines()
vocab = len(prompt)
generated = []
num_word = 13
while len(sorted(set(generated), key=lambda d: generated.index(d))) < num_word:
	rand = random.randint(0, vocab)
	generated.append(prompt[rand])
print(' '.join(sorted(set(generated), key=lambda d: generated.index(d))))