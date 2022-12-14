import random
import csv

# CSV importing line adapted from https://stackoverflow.com/a/26179929
countries = list(csv.reader(open("countries.csv")))
score = 0
correctList = []
inGame = True

def checkCorrect(guess):
  if(guess.casefold() == country.casefold()):
    print("Correct!")
    correctList.append(city + ", " + country)
    return True
  else:
    print("Incorrect! The correct country was " + country + ". Your score was " + repr(score) + ".")
    correctList.append("Game ended on " + city + ", " + country)
    return False

print("Welcome to European City Guesser, a game created to help you get better at GeoGuessr. Simply guess the country that the given city is in, and you'll get a point!")

while inGame == True:
  countryNum = random.randint(0, 36)
  country = countries[countryNum][1]
  cityNum = random.randint(2, 21)
  city = countries[countryNum][cityNum]

  answer = input("\nIn what country is " + city + "? ")

  isCorrect = checkCorrect(answer)
  
  if isCorrect == False:
    again = input("\nWould you like to play again? (y/n) ")
    if again.casefold() == "y":
      score = 0
      inGame = True
    else:
      inGame = False
      
      summary = input("\nWould you like a summary of all the countries you have guessed? (y/n) ")

      if summary.casefold() == "y":
        print("")
        for i in correctList:
          print(i)
  score += 1