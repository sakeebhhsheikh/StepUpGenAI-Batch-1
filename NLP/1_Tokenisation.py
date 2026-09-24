import string
import re
import gc
import pandas as pd

string_data = '''
What is Python? Executive Summary

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective. '''

Stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
stop_symbols = """[];',./?><":}{|=-0987654321`~!@#$%^&*()_+}"""

# print(string.punctuation)
# print(string.digits)
# final_word_li = []
# word_list = string_data.lower().split()

# for word in word_list:
#     # print(word, end='-->')
#     for ch in stop_symbols:
#         word = word.replace(ch, " ")    
#     templi = [w for w in word.split() if w not in Stop_words]
#     # print(templi)
#     final_word_li.extend(templi)
# print(final_word_li)

input_data = '''sports	The team scored a dramatic goal in the final minute of the match to win the championship.
sports	The tennis star advanced to the quarter-finals after a grueling three-hour match.
technology	The new software update addresses critical security bugs and optimizes battery life.
technology	Engineers are developing a new quantum computer that operates at room temperature.
finance	The stock market experienced a sharp decline following the central bank's interest rate announcement.
finance	Quarterly corporate earnings exceeded expectations, driving a rally in tech stocks.'''

'''
def gen_tokens(line):
    word_li = []
    word_list = line.lower().split()

    for word in word_list:
        # print(word, end='-->')
        for ch in stop_symbols:
            word = word.replace(ch, " ")    
        templi = [w for w in word.split() if w not in Stop_words]
        # print(templi)
        word_li.extend(templi)
    #print(word_li)
    return word_li

all_unique_words = []
final_token_li = []
for line in input_data.strip().splitlines():
    wli = gen_tokens(line)
    all_unique_words.extend(wli)
    final_token_li.append(wli)
#print(*final_token_li, sep='\n')
unique_words = sorted(set(all_unique_words))
'''
#df = pd.get_dummies(unique_words)
#print(df)
'''
one_hot_encoding = dict.fromkeys(unique_words, list())
for row in final_token_li:
    for word in one_hot_encoding:
        li = (one_hot_encoding.get(word) if one_hot_encoding.get(word) else [])
        li.append((1 if word in row else 0))
        one_hot_encoding[word] = li
#print(one_hot_encoding)

df = pd.DataFrame(one_hot_encoding)
print(df)
'''

# df_li = []

# for row in final_token_li:
#     df = pd.get_dummies(row)
#     df = pd.DataFrame(df.sum(axis=0))
#     df_li.append(df)
# finaldf = pd.concat(df_li, axis=1)
# finaldf = finaldf.T.fillna(0).astype(int)
# print(finaldf)


from nltk.tokenize import word_tokenize, LineTokenizer, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re
import nltk
# nltk.download('punkt_tab')
# nltk.download('stopwords')
# nltk.download('wordnet')
"""
clean_text = input_data.lower()
#clean_text = re.sub(r'(\\d+)', '', clean_text)
clean_text = clean_text.translate(str.maketrans('','', string.punctuation))
#print(clean_text)#

tokenizer = LineTokenizer(blanklines="discard-eof")
linetokens = tokenizer.tokenize(clean_text)
# input(linetokens)

tokens = word_tokenize(clean_text)
# print(tokens)

stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w not in stop_words]
print(filtered_tokens)

#PorterStemmer
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(w) for w in filtered_tokens]
#print(stemmed_tokens)

#WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]
#print(lemmatized_tokens)
"""

# stemmer = PorterStemmer()
# lemmatizer = WordNetLemmatizer()
# w ='industry'
# w ='industries'
# w ='industrialization'
# print(stemmer.stem(w))
# print(lemmatizer.lemmatize(w))

import gensim
text = "Natural language processing enables computers to understand human language. Word2Vec creates dense vector representations."

# Preprocessing and tokenization
processed_story = [word_tokenize(i.lower()) for i in sent_tokenize(text)]

# input(processed_story)
# Train Word2Vec model (CBOW or Skip-gram via sg=0 or sg=1)
model = gensim.models.Word2Vec(sentences=processed_story, vector_size=100, window=5, min_count=1, workers=4)

# Get vector for a specific word
# vector = model.wv['word2vec']

# # Find similar words
# similar_words = model.wv.most_similar('language')
# print(similar_words)

#print(model.wv.most_similar("computers"))

print(model.wv.similarity(w1="computers", w2="computers"))

print(model.wv['computers'])