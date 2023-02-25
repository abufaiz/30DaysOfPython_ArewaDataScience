# 30DaysOfPython Exercises 

print("...................(""Exercise Level 1 (Q.1)"")............................")
''' Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt' '''
import requests
from collections import Counter
import re

# Fetch the text from the URL
response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
text = response.text

# Remove the header and footer
start_index = text.find('*** START OF THIS PROJECT GUTENBERG EBOOK ROMEO AND JULIET ***')
end_index = text.find('*** END OF THIS PROJECT GUTENBERG EBOOK ROMEO AND JULIET ***')
text = text[start_index:end_index]

# Remove all punctuation and convert to lowercase
text = re.sub(r'[^\w\s]', '', text).lower()

# Count the frequency of each word and find the 10 most frequent
word_counts = Counter(text.split())
top_words = word_counts.most_common(10)

print(top_words)

print("...................(""Exercise Level 1 (Q.2)"")............................")
'''Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
the min, max, mean, median, standard deviation of cats' weight in metric units.
the min, max, mean, median, standard deviation of cats' lifespan in years.
Create a frequency table of country and breed of cats'''

import requests
import statistics

# make a request to the cats API
cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)

# load the response data into a Python object
data = response.json()

# extract the weight and lifespan data from the object
weights = []
lifespans = []
for cat in data:
    if cat['weight']['metric']:
        weight_min, weight_max = cat['weight']['metric'].split(' - ')
        weight_min = float(weight_min)
        weight_max = float(weight_max)
        weight_mean = (weight_min + weight_max) / 2
        weights.append(weight_mean)
    if cat['life_span']:
        lifespan_min, lifespan_max = cat['life_span'].split(' - ')
        lifespan_min = int(lifespan_min)
        lifespan_max = int(lifespan_max)
        lifespan_mean = (lifespan_min + lifespan_max) / 2
        lifespans.append(lifespan_mean)

# calculate the statistics for weight and lifespan
weight_min = min(weights)
weight_max = max(weights)
weight_mean = statistics.mean(weights)
weight_median = statistics.median(weights)
weight_stddev = statistics.stdev(weights)

lifespan_min = min(lifespans)
lifespan_max = max(lifespans)
lifespan_mean = statistics.mean(lifespans)
lifespan_median = statistics.median(lifespans)
lifespan_stddev = statistics.stdev(lifespans)

# create a frequency table of country and breed of cats
freq_table = {}
for cat in data:
    country = cat['origin']
    breed = cat['name']
    if country and breed:
        key = (country, breed)
        if key in freq_table:
            freq_table[key] += 1
        else:
            freq_table[key] = 1

# print the results
print(f"Weight statistics (in metric units):")
print(f"Minimum weight: {weight_min:.2f}")
print(f"Maximum weight: {weight_max:.2f}")
print(f"Mean weight: {weight_mean:.2f}")
print(f"Median weight: {weight_median:.2f}")
print(f"Standard deviation of weight: {weight_stddev:.2f}\n")

print(f"Lifespan statistics (in years):")
print(f"Minimum lifespan: {lifespan_min:.2f}")
print(f"Maximum lifespan: {lifespan_max:.2f}")
print(f"Mean lifespan: {lifespan_mean:.2f}")
print(f"Median lifespan: {lifespan_median:.2f}")
print(f"Standard deviation of lifespan: {lifespan_stddev:.2f}\n")

print("Frequency table of country and breed of cats:")
for key, value in freq_table.items():
    country, breed = key
    print(f"{country}: {breed} - {value} cats")

print("...................(""Exercise Level 1 (Q.3)"")............................")

''' Read the countries API and find
the 10 largest countries
the 10 most spoken languages
the total number of languages in the countries API '''

