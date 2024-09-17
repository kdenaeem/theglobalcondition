from math import sqrt, pow, exp


nlp = spacy.load('en_core_web_md')

def squared_sim(x):
  return round(sqrt(sum([a*a for a in x])),3)

def euclidean_distance(x, y):
  return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

sentences = ["The bottle is empty",
"There is nothing in the bottle"]
sentences = [sent.lower().split(" ") for sent in sentences]


embeddings = [nlp(sentence).vector for sentence in sentences]

