import time
import random
import math
from difflib import SequenceMatcher


class TypingTest():
    
    def __init__(self):
        pass

  
    def format_file(self, filename, max_len, min_len):
        '''
        Given a file of words separated by a line, return a list of all 
        the words that have lengths between min_len and max_len inclusive.
        
        Args:
            filename: name of the file to be read
            max_len: maximum length of a word to be included in the returned list
            min_len: minimum length of a word to be included in the returned list
                
        Returns: list
        '''  
        lst = []
        f = open(filename)
        word = f.readline()
        while word:
            if len(word)-1 <= max_len and len(word)-1 >= min_len:
                word = ''.join(e for e in word if e.isalnum()).lower()
                lst.append(word)
            word = f.readline()
        return lst
    

    def accuracy(self, orig, user):
        '''
        This method measures the accuracy of string user with respect to string 
        orig. Accuracy is measured by with the SequenceMatcher class from the 
        difflib library
    
        Args:
            orig: actual word
            user: word to be compared to orig
    
        Returns: float
        '''
        return SequenceMatcher(None, orig, user).ratio()

    

    def __main__(self):
        '''
        This main method takes in user input of how long the maximum length of a word
        should be, how long the minimum length of a word should be, and how long the
        user wants to take the typing test for in seconds. Then, this main method
        outputs words randomly selected from the word list returned by method
        format_file as well as prints the total number of words typed and the average
        accuracy of the user's typing (computed through taking the average of all the
        accuracy values for each typed word)
        '''
        #user input
        print("Ready to test your typing skills?")
        duration = input("How long do you want to take this test for? \
                        Type a numeric value in seconds: ")
        duration = int(duration)
        max_len = input("How long do you want the max length of a word to be? \
                        Type a numeric value: ")
        max_len = int(max_len)
        while max_len < 0:
            max_len = input("Please input a positive number: ")
            max_len = int(max_len)
        
        min_len = input("How long do you want the min length of a word to be? \
                        Type a numeric value: ")
        min_len = int(min_len)
        while min_len > max_len:
            min_len = input("Please input a number less than the max length: ")
            min_len = int(min_len)
        
        #edge cases
        if min_len < 0: #user enters a negative value
            min_len = 0
        min_len = math.ceil(min_len) #user enters non-integer value
        max_len = math.floor(max_len) #uesr enters non-integer value
        
        
        #instructions for user
        print("Press enter after each word you type. Do not capitalize, punctuate, or type spaces.")

        #file obtained and modified from https://github.com/dwyl/english-words/blob/master/words.txt
        wordlist = self.format_file("words.txt", max_len, min_len)
        lenlist = len(wordlist)
        
        start = time.time() 
        end = start + duration
        counter = 0
        sum_accuracy = 0
        while time.time() < end:
            word = wordlist[random.randrange(lenlist)]
            user = input(word + '\n')
            print(len(word))
            print(len(user))
            print(self.accuracy(word, user))
            print(user)
            sum_accuracy += self.accuracy(word, user)
            counter += 1
        
        print("Number of words: " + str(counter))
        print("Average accuracy per word: " + str(sum_accuracy/counter))            




