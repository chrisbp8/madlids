from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_word(word_type):
    words = {
        'noun': ['dog', 'car', 'banana', 'mountain', 'cookie'],
        'verb': ['run', 'jump', 'eat', 'sleep', 'drive'],
        'adjective': ['big', 'yellow', 'quick', 'lazy', 'funny'],
        'adverb': ['quickly', 'lazily', 'happily', 'sadly'],
        'place': ['park', 'restaurant', 'school', 'zoo', 'museum'],
<<<<<<< HEAD
        'exclamation': ['Wow', 'Oh no', 'Hoorays', 'Yikes', 'Oops'],
=======
        'exclamation': ['Wow', 'Oh no', 'Hooray', 'Yikes', 'Oops'],
>>>>>>> refs/remotes/origin/main
    }
    return random.choice(words[word_type])

def create_story():
    story_template = (
        "{exclamation}! Today I went to the {place} and I saw a very {adjective} {noun}. "
        "It was {adverb} {verb}ing around! I couldn't believe my eyes, so I decided to "
      "{verb} along with it. What a day!"
    )

def create_story():
    story_template = (
        "{exclamation}! Today I went to the {place} and I saw a very {adjective} {noun}. "
        "It was {adverb} {verb}ing around! I couldn't believe my eyes, so I decided to "
      "{verb} along with it. What a day!"
    )
    
    story = story_template.format(
        exclamation=get_word('exclamation'),
        place=get_word('place'),
        adjective=get_word('adjective'),
        noun=get_word('noun'),
        adverb=get_word('adverb'),
        verb=get_word('verb')
    )

    return story

@app.route('/')
def home():
    return create_story()

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=8000)
=======
    app.run(host="0.0.0.0", port=8000)
>>>>>>> refs/remotes/origin/main
