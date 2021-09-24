#! python3
'''
at each adjective and noun and verb and in some blanks we ask for the user input
and then user input is placed in the blank in the text
and finally after all the inputs are taken then we display the final text to the user based on the user input
also created a new file in the directory as text.txt file
'''

def out(word):
  return(str(input(f"Enter {word}: ")))

text = f'The {out("Adjective")} panda walked to the {out("Noun")} and then {out("Verb")}. A nearby {out("Noun")} was unaffected by these events.'

print(text)

f = open("text.txt","w")
f.write(text)
f.close()