import random
import csv

# CSV importing line adapted from https://stackoverflow.com/a/26179929
countries = list(csv.reader(open("countries.csv")))

countryNum = random.randint(0,36)
country = countries[countryNum][1]
print(country)
cityNum = random.randint(2,21)
city = countries[countryNum][cityNum]
print(city)