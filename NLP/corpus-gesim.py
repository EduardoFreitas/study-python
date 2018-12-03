# Import Dictionary
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

article = open('../data/article.txt', 'r').read()
# Tokenize the article: tokens
tokens = word_tokenize(article)
# Convert the tokens into lowercase: lower_tokens
lower_tokens = [t.lower() for t in tokens]
english_stops = set(stopwords.words('english'))
# Retain alphabetic words: alpha_only
alpha_only = [t for t in lower_tokens if t.isalpha()]
# Remove all stop words: no_stops
no_stops = [t for t in alpha_only if t not in english_stops]
# Instantiate the WordNetLemmatizer
articles = [1]
articles[0] = no_stops

# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)

# Select the id for "computer": computer_id
computer_id = dictionary.token2id.get("computer")

# Use computer_id with the dictionary to print the word
print(dictionary.get(computer_id))

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[4][:10])