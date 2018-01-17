import nltk
from nltk.corpus import stopwords

# download the english stopwords first if necessary
#nltk.download('stopwords')

stop_words = stopwords.words("english")
print len(stop_words)