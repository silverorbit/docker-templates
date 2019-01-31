import os
from flask import Flask, jsonify

app = Flask(__name__)

books =  [
    {
      "isbn": "9781593275846",
      "title": "Eloquent JavaScript, Second Edition",
      "subtitle": "A Modern Introduction to Programming",
      "author": "Marijn Haverbeke",
      "published": "2014-12-14T00:00:00.000Z",
      "publisher": "No Starch Press",
      "pages": 472,
      "description": "JavaScript lies at the heart of almost every modern web application, from social apps to the newest browser-based games. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.",
      "website": "http://eloquentjavascript.net/"
    },
    {
      "isbn": "9781449325862",
      "title": "Git Pocket Guide",
      "subtitle": "A Working Introduction",
      "author": "Richard E. Silverman",
      "published": "2013-08-02T00:00:00.000Z",
      "publisher": "O'Reilly Media",
      "pages": 234,
      "description": "This pocket guide is the perfect on-the-job companion to Git, the distributed version control system. It provides a compact, readable introduction to Git for new users, as well as a reference to common commands and procedures for those of you with Git experience.",
      "website": "http://chimera.labs.oreilly.com/books/1230000000561/index.html"
    },
{
      "isbn": "9781593277574",
      "title": "Understanding ECMAScript 6",
      "subtitle": "The Definitive Guide for JavaScript Developers",
      "author": "Nicholas C. Zakas",
      "published": "2016-09-03T00:00:00.000Z",
      "publisher": "No Starch Press",
      "pages": 352,
      "description": "ECMAScript 6 represents the biggest update to the core of JavaScript in the history of the language. In Understanding ECMAScript 6, expert developer Nicholas C. Zakas provides a complete guide to the object types, syntax, and other exciting changes that ECMAScript 6 brings to JavaScript.",
      "website": "https://leanpub.com/understandinges6/read"
    }

  ]


@app.route('/library/api/v1.0/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})


from flask import abort

@app.route('/library/api/v1.0/books/<string:isbn>', methods=['GET'])
def get_book(isbn):
    print (isbn)
    book = [book for book in books if book['isbn'] == isbn]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book[0]})

from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

