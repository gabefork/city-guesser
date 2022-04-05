import random
import csv

# CSV importing line from https://stackoverflow.com/a/26179929
countries = list(csv.reader(open("countries.csv")))

countryNum = random.randint(0,0)
country = countries[countryNum][1]
print(country)
cityNum = random.randint(2,20)
city = countries[countryNum][cityNum]
print(city)