import random
import csv

# CSV importing line adapted from https://stackoverflow.com/a/26179929
countries = list(csv.reader(open("countries.csv")))
score = 0
correctList = []
inGame = True

print("Welcome to European City Guesser, a game created to help you get better at GeoGuessr. SImply guess the country that the given city is in, and you'll get a point!")

while inGame == True:
  countryNum = random.randint(0, 36)
  country = countries[countryNum][1]
  cityNum = random.randint(2, 21)
  city = countries[countryNum][cityNum]

  answer = input("\nIn what country is " + city + "? ")

  if(answer.casefold() == country.casefold()):
    print("Correct!")
    score += 1
    correctList.append(city + ", " + country)
  else:
    print("Incorrect! The correct country was " + country + ". Your score was " + repr(score) + ".")
    correctList.append("Ending on " + city + ", " + country)
    summary = input("\nWould you like a summary? (y/n) ")

    if summary.casefold() == "y":
      for i in correctList:
        print(i)
    
      again = input("Would you like to play again? (y/n) ")
    
      if again.casefold() == "y":
        score = 0
        inGame = True
      else:
        inGame = False
    
    else:
      again = input("Would you like to play again? (y/n) ")
    
      if again.casefold() == "y":
        score = 0
        inGame = True
      else:
        inGame = False