from summa import keywords
import newspaper
from newspaper import Article
import pickle


url = 'https://apnews.com/article/shootings-gun-politics-barack-obama-houston-violence-62765e5b208e74c0b109678bb46d31ed'
article = Article(url)
article.download()

article.parse()

full_text = article.text

TR_keywords = keywords.keywords(full_text, scores=True)

top_ten = TR_keywords[0:10]

key_list = []
for word in top_ten:
    key_list.append(word[0])

print(key_list)

pickle_out = open('key_list', 'wb')
pickle.dump(key_list, pickle_out)
pickle_out.close()



