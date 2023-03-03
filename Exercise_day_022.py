# 30DaysOfPython Exercises 

print("...................(""Exercise (Q.1)"")............................")
''' Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/'). '''

import requests
from bs4 import BeautifulSoup
import json

url = "https://www.sanhablog.com/"

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object and parse the HTML content of the website
soup = BeautifulSoup(response.content, "html.parser")

# For example, to scrape the text of all <h1> elements:
data = [h1.text for h1 in soup.find_all("h1")]

# Create a dictionary with the scraped data
data_dict = {"data": data}

# Convert the dictionary into a JSON object
json_data = json.dumps(data_dict)

# Write the JSON object to a file
with open("scraped_data.json", "w") as f:
    f.write(json_data)


print("...................(""Exercise (Q.1)"")............................")
''' Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file '''

# Replace this URL with the website URL containing the table you want to extract
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Make a GET request to the URL and parse the HTML using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table element in the HTML and get its header row
table = soup.find('table')
header_row = table.find('tr')

# Extract the column names from the header row and initialize an empty list for the data
column_names = [header.text for header in header_row.find_all('th')]
table_data = []

# Loop through all rows in the table (excluding the header row) and extract the cell values
for row in table.find_all('tr')[1:]:
    row_data = {}
    for i, cell in enumerate(row.find_all('td')):
        row_data[column_names[i]] = cell.text
    table_data.append(row_data)

# Convert the table data to a JSON object
json_data = json.dumps(table_data)

# Write the JSON object to a file named 'table_data.json'
with open('table_data.json', 'w') as f:
    f.write(json_data)

print("...................(""Exercise (Q.3)"")............................")
''' Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time. '''

# URL of the Wikipedia page containing the "List of Presidents of the United States" table
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

# Make a GET request to the URL and parse the HTML using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table element containing the presidents data
table = soup.find('table', {'class': 'wikitable'})

# Initialize an empty list for the presidents data
presidents_data = []

# Loop through all rows in the table (excluding the header row) and extract the president data
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    
    # Ignore rows with incomplete data or table headers
    if len(columns) < 4:
        continue
    
    # Extract the data for the current president
    number = columns[0].text.strip()
    name = columns[1].text.strip()
    start_date = columns[3].text.strip()
    end_date = columns[4].text.strip()
    party = columns[5].text.strip()
    
    # Create a dictionary object for the current president and add it to the list
    president_data = {
        'number': number,
        'name': name,
        'start_date': start_date,
        'end_date': end_date,
        'party': party
    }
    presidents_data.append(president_data)

# Convert the presidents data to a JSON object
json_data = json.dumps(presidents_data)

# Write the JSON object to a file named 'presidents.json'
with open('presidents.json', 'w') as f:
    f.write(json_data)
