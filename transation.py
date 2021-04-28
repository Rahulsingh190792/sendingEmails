# from googlesearch import search
# query = 'what is machine learning?'
# for j in search(query, tld="co.in", num=1, stop=5, pause=2):  ## it will return a total of 5 links
#     print(j)

###############################################################################


import wikipedia
query = 'Narendra Modi'
results = wikipedia.summary(query, sentences=20) ## change the number of sentence to get a larger words summary
print(results)