from duckduckgo_search import DDGS

keywords = 'osint'
results = DDGS().text(keywords, region='us-en', safesearch='off', timelimit='y', max_results=10)
print(results)