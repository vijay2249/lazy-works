import random

capitals = {
  'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock',
  'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford',
  'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
  'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
  'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
  'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
  'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
  'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
  'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
  'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
  'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
  'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
  'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}


for _ in range(1,36,1):
  #creating quiz file and answer file 
  qFile = open(f'Quiz{_}.txt','w')
  ansFile = open(f'Answers{_}.txt','w')

  #headers
  qFile.write(f"Name {_}\n Section: A \n Roll.no. 1971{_}\n\n")
  qFile.write(("States and Capitals Quiz") + (' '*10) + ("Each Question carries one mark"))
  qFile.write("\n\n\n")
  ansFile.write(f"Answer Key {_}")
  ansFile.write("\n\n")

  #shuffing the list of states
  states = list(capitals.keys())
  random.shuffle(states)

  for i in range(len(states)):
    correctAns = capitals[states[i]] #getting correct answer for each question
    wrongAns = list(capitals.values()) #all options possible
    del wrongAns[wrongAns.index(correctAns)] #removing the correct option
    wrongAns = random.sample(wrongAns,3) #selecting 3 random options
    options = wrongAns + [correctAns] #setting up 4 total options
    random.shuffle(options) #shuffling the options

    qFile.write(f"{i+1}. What is the capital of the state {states[i]} \n\n")
    qFile.write(f"(A) {options[0]}\t(B) {options[1]}\t(C) {options[2]}\t(D) {options[3]}")
    qFile.write("\n\n")
    ansFile.write(f"{i+1}. {'ABCD'[options.index(correctAns)]}\n")

  qFile.close()
  ansFile.close()
