import random


birdsList = ['kingfisher','ostrich', 'owl', 'pigeon', 'eagle' , 'parrot']

hangmanList = [
    '''-----------------
|
|
|
|
|
|
|
|
    ''',
    '''-----------------
|      |
|      o
|      |
|
|
|
|
|
    ''',
        '''-----------------
|      |
|      o
|     /|\
|      |
|
|
|
|
    ''',
    '''-----------------
|      |
|      o
|     /|\
|      |
|     /
|
|
|
    ''',
        '''-----------------
|      |
|      o
|     /|\
|      |
|     / \
|
|
|
    ''']

def printLettersInaWord(selection, randomWord):
    finalWord = list()
    letterList = list(randomWord.upper())
    finalSelection = list()
    
    for selectedLetter in selection:
        finalSelection.append(selectedLetter)
        
    for letterInWord in letterList :
        if (letterInWord in finalSelection):
            finalWord.append(letterInWord)
            finalSelection.remove(letterInWord)
        else:
            finalWord.append('_')
            
    print(finalWord)



from typing import List
def hangman():
  randomWord = random.choice(birdsList)
  lettersSet = list(randomWord.upper())
  selection = list()
  guesses = list()

  hang = 0

  #print(hangmanList[hang])

  while ((hang < len(hangmanList)) & (len(lettersSet) > 0)):
      inputValue = input('Please enter the letter for the word: ').upper()
      if (inputValue in lettersSet):
          selection.append(inputValue)
          guesses.append(inputValue)
          lettersSet.remove(inputValue)
          print('LettersSet: ', lettersSet)

      elif (inputValue in guesses):
          print('You have already used this word')
          print(hangmanList[hang])

      else:
          print('You have entered a wrong letter \n')
          print(hangmanList[hang])
          guesses.append(inputValue)
          hang += 1

      printLettersInaWord(selection, randomWord)


  if len(lettersSet) == 0:
      print('Congrats, you win!!')

  if (hang == (len(hangmanList))):
      print('Sorry! you lose!!')


hangman()

