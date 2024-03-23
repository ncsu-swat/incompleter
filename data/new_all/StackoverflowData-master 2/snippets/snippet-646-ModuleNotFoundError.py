#Source: https://stackoverflow.com/questions/74389747/attributeerror-what-am-i-doing-wrong-here
from spellCheck import SpellCheck
#from spellCheck import bcolors

def main():
    choice = input("Enter the word to look for:\n> ")
    initial = SpellCheck()
    initial.__init__()
    initial.linearSearch(choice)
    
    
main()