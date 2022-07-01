"""
Created on Wed Jul 29 21:21:22 2020

@author: jhalls

"""


from spellchecker import SpellChecker

spell = SpellChecker()

#find the woeds that may be mispelled
misspell = spell.unknown(['let', 'us', 'walk', 'on', 'teh'])

for word in misspell:
#    get the one most likely answer
    print(spell.correction(word))
    
#    get the list of likely words
    print(spell.candidates(word))
    
