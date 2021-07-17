from chatbot import chatbot #Before we do anything else, ChatterBot needs to be imported. The import for ChatterBot is seen before reading this comment.

from flask import Flask, render_template, request #Renders a template from the template folder with the given context,The requests library is for your app to make HTTP request to other sites, usually APIs. It makes an outgoing request and returns the response from the external site.

app = Flask(__name__) #Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
app.static_folder = 'static' #calling the instance or saving this file flask.py will confilct with flask application itself but it's better to save the application as app.py

@app.route("/") #This is a  decorator.A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate
def home():
    return render_template("index.html") #it generates the output in the content of index.html file to a url through the template_render

@app.route("/get") #A decorator that is used to register a view function for a given URL rule. This does the same thing as add_url_rule but is intended for decorator usage
def get_bot_response(): #this defines a function for user input 
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText)) #Return the bot's response based on the input from user.

if __name__ == "__main__": #the __name__ == "__main__" runs blocks of code only when our Python script is being executed directly from a user. This is powerful as it allows our code to have different behavior when it's being executed as a program instead of being imported as a module. Though python sets Whenever the Python interpreter reads a source file, it does two things:it sets a few special variables like __name__, and then it executes all of the code found in the file.
    app.run() #Runs the application on a local development server.

#Do not use run() in a production setting. It is not intended to meet security and performance requirements for a production server. Instead, see deployment for WSGI server recommendations.

#If the debug flag is set the server will automatically reload for code changes and show a debugger in case an exception happened.

#If you want to run the application in debug mode, but disable the code execution on the interactive debugger, you can pass use_evalex=False as parameter. This will keep the debugger's traceback screen active, but disable code execution.

#It is not recommended to use this function for development with automatic reloading as this is badly supported. Instead you should be using the flask command line script's run support.

#End of Code, Thanks and smile while reading, trust you understood :-)