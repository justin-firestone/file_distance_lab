# file_distance lab

# a few text files are in the repository

# This function removes punctuation, and extra spaces from the input argument,
# then forces it into lowercase and tokenizes it into an array of words.

def tokenize(text):
	text = text.replace('[.,;@"”’“?‘\/#!$%\^&\*;:{}=\-_`~()]', "")
	text = text.replace('--', " ")
	text = text.replace('\s{2,}', " ")
	text = text.replace('[\n\t]', " ")
	text = text.lower()
	text = text.split()
	return text



# This function returns the shortest distance (in terms of number of words) between
	# the searchWords in the text. The searchWords can be found in the text in either order


def min_distance(text, search_words):
	words = tokenize(text);
	# TODO
	return None


def display_results(m):
	print(f"The shortest distance between the search words in the text is {m} words.")


text = "The itsy bitsy spider climbed up the waterspout. " \
		"Down came the rain and washed the spider out. " \
		"Out came the sun and dried up all the rain" \
		"and the itsy bitsy spider climbed up the spout again." \

search_words = ["spider", "rain"]

# try reading in files
# f = open("dracula.txt", "r")
# text = f.read()
# search_words = ["drink", "blood"]

# f = open("peterpan.txt", "r")
# text = f.read()
# search_words = ["fairy", "hook"]

# f = open("prideandprejudice.txt", "r")
# text = f.read()
# search_words = ["visit", "happiness"]



m = min_distance(text, search_words)
display_results(m)
