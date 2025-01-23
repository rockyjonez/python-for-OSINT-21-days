from duckduckgo_search import DDGS
import csv

csv_file = open('search_results.csv', 'w')
writer = csv.writer(csv_file, delimiter =';')


keywords = 'osint'
results = DDGS().text(keywords, region='us-en', safesearch='off', timelimit='y', max_results=10)

for x in range(len(results)):
    row = [results[x]["title"],results[x]["body"],results[x]["href"]]
    writer.writerow(row)

csv_file.close()
