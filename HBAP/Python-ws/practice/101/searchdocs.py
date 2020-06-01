import string

doc_list = ['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'a Casinoville?', 'i have a red car.']


def word_search(documents, keyword):
    # list to hold the indices of matching documents
    indices = []
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


def multi_word_search(doc_list, keywords):
    matchdict = {}
    for keyword in keywords:
        matchdict[keyword] = word_search(doc_list, keyword)
    return matchdict


# print(word_search(doc_list, 'car'))
print(multi_word_search(doc_list, ['car', 'a']))

print(multi_word_search(doc_list, ['car', 'ab']))
