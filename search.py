import re 
from re import Match
def printSolution(sol: Match[str]| None):
    for group in sol.groups():
        print(group)


text = 'My number is 415-555-4242.'
text1 = 'The Adventures of Batman'
text2 = 'The Adventures of Batwoman'

regex0 = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
regex1 = re.compile(r"Bat(wo)?man")
regex2 = re.compile(r"ha(\d)*ha")

sol = regex2.search("ha123412ha")


# sol = regex0.search(text)


# sol = regex1.search(text2)

print(sol.group(1))