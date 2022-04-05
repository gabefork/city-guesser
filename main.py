import random
import csv

# CSV importing line from https://stackoverflow.com/a/26179929
countries = list(csv.reader(open("countries.csv")))

countryNum = random.randint(1,37)
country = countries[countryNum][1]
print(country)