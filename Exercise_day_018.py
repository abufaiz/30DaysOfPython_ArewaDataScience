# 30DaysOfPython Exercises 


print("...................(""Exercise Level 1 (Q.1)"")............................")
'''What is the most frequent word in the following paragraph?   
paragraph = 'I love teaching. If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the capabilities
to develop an application what else can you love.'''

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# remove punctuation and convert to lowercase
clean_paragraph = paragraph.lower().replace('.', '').replace(',', '')

# split paragraph into individual words
words = clean_paragraph.split()

# count the occurrences of each word
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# find the word with the highest count
most_frequent_word = max(word_counts, key=word_counts.get)

print("The most frequesnt word is:", most_frequent_word)

print("...................(""Exercise Level 1 (Q.2)"")............................")

'''The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 
in the negative direction, 0 at origin, 4 and 8 in the positive direction. 
Extract these numbers from this whole text and find the distance between the 
two furthest particles. points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) # 12.'''


text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

import re

# extract the numbers from the text
points = re.findall(r'-?\d+', text)

# convert the numbers to integers
points = [int(p) for p in points]

# sort the points in ascending order
sorted_points = sorted(points)

# calculate the distance between the furthest points
distance = abs(sorted_points[-1] - sorted_points[0])

print(distance)


print("...................(""Exercise Level 2 (Q.1)"")............................")

''' Write a pattern which identifies if a string is a valid python variable

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True '''

def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_]\w*$'
    return re.match(pattern, variable) is not None

print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname'))  # True


print("...................(""Exercise Level 3 (Q.1)"")............................")

''' Clean the following text. After cleaning, count three most frequent words in the string.
sentence = %I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing;
&as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching 
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a 
tea@cher!?

print(clean_text(sentence));
I am a teacher and I love teaching There is nothing as more rewarding as educating
and empowering people I found teaching more interesting than any other jobs Does 
this motivate you to be a teacher print(most_frequent_words(cleaned_text)) 
# [(3, 'I'), (2, 'teaching'), (2, 'teacher')] '''

from collections import Counter

def clean_text(text):
    pattern = r'[^a-zA-Z0-9\s]'
    text = re.sub(pattern, '', text)
    text = text.lower()
    return text

def most_frequent_words(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(3)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is 
nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;
I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s 
mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)
# Output: i am a teacher and i love teaching there is nothing as more rewarding as educating and empowering people i found teaching more interesting than any other jobs does this motivate you to be a teacher

print(most_frequent_words(cleaned_text))
# Output: [(3, 'i'), (2, 'teaching'), (2, 'teacher')]
