from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

string1 = 'hi Katie the self driving car will be late Best Sebastien'
string2 = 'Hi Sebastien the machine learning class will be great great great Best Katie'
string3 = 'Hi Katie the machine learning class will be most excellent'

print string3

email_list = [string1, string2, string3]

bag_of_words = vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list)
