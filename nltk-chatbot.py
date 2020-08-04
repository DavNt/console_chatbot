# importing natural language toolkit python library
from nltk.chat.util import Chat, reflections

# A dictionary containing input and output values.
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# set values for conversing
chat_pairs = [

    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name ?",
        ["My name is DBot and I'm a chatbot ?", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good. What is your name?", ]
    ],
    [
        r"my name is (.*)(.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"(.*) (good|great|fine)",
        ["Nice to hear!", ]
    ],
    [
        r"i'm|l'm (.*) doing good",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"What is your age?",
        ["I'm a computer program dude\nSeriously you are asking me this?", ]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*) created ?",
        ["David created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Bulawayo, Zimbabwe', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",
         "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it.", "Never even heard about %1"]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (cooking|cook|kitchen)",
        ["IYes! I love cooking. My favorite food is exotic dishes, haha if programs ate.", ]
    ],
    [
        r"(.*) fact",
        ["Be yourself; everyone else is already taken.",
         "You've gotta dance like there's nobody watching",
         "Be the change that you wish to see in the world",
         "No one can make you feel inferior without your consent",
         "Live as if you were to die tomorrow",
         "Darkness cannot drive out darkness: only light can do that", ]
    ],
    [
        r"(.*) (language) (.*) ?",
        ["I am written in python but I speak English.", ]
    ],
    [
        r"(.*) (friend|best friend) ?",
        ["David is my best friend. I love to being part of his programming projects", ]
    ],
    [
        r"(.*) (love|like) (.*)?",
        ["I love to chat and meet new peoples.", ]
    ],
    [
        r"(.*) (created) ?",
        ["David created me so that I can talk with beautiful people like you", ]
    ],
    [
        r"(.*) (DavNt|davnt programmer) ?",
        ["Well DavNt is a programmer. Who likes working on Programs, Freelancing projects and many other things.", ]
    ],
    [
        r"(.*) (fruit|eat|food) ?",
        ["HaHa nice question. I am a robot I don't eat.", ]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],

]


# define a function to work the chatbot
def dbot():
    # default message at the start
    print('''Hi, I'm DBot and am here if you're looking for a chat ;)
            Please type lowercase English language to start a conversation. 
            Type quit to leave ''')

    chat = Chat(chat_pairs, reflections)
    chat.converse()


# call the function
dbot()
