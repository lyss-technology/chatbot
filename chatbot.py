from chatterbot import ChatBot  #importing chatterbot library
from chatterbot.trainers import ListTrainer  #Allows a chat bot to be trained using a list of strings where the list represents a conversation.in addition, it Train the chat bot based on the provided list of statements that represents a single conversation
from chatterbot.trainers import ChatterBotCorpusTrainer #Allows the chat bot to be trained using data from the ChatterBot dialog corpus. A corpus is a large and structured set of machine-readable texts that have been produced in a natural communicative setting

# Creating ChatBot Instance
chatbot = ChatBot('ATPLCBot')

 # Training with Personal Questions & Answers for chatterbot.trainers to make use of
training_data_quesans = open('/home/adesoji/Documents/Internship/ATPLC/new_chat_bot/training_data/answers.txt').read().splitlines()
training_data_personal = open('/home/adesoji/Documents/Internship/ATPLC/new_chat_bot/training_data/questions.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal


trainer = ListTrainer(chatbot) #The base class of the class hierarchy.When called, it accepts no arguments and returns a new featureless instance that has no instance attributes and cannot be given any.
trainer.train(training_data) # As seen in line 2 above

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 
#End of Code, Thanks and smile while reading, trust you understood :-)