# Libro Tracker

## Introduction
Libro Tracker is a CLI (command line interface) app where you can manage books in your library by genre, all stored locally on your computer. Libro Tracker also tracks books by reading status, can see how many books you've read in each genre and what's next on your reading list.

## Features
As a CLI app, Libro Tracker presents several menus that have their own options to manage your genres and books. You can select menu options by entering in the number of the option displayed; you can go back to the previous menu by entering '0' in most menus. The app will print informative messages to help you navigate each menu.

### Genres and Books
Genres have a name and a description which are provided by you. Genres can be updated over time, and deleted. Note, if there are books in a genre that you are deleting, you will be asked to reassign those books to a different genre.

Books have a title, author name, page count, reading status, and can have only one genre. Reading statuses include "Reading", "Finished", "To Read", and "Did Not Finish". You can edit a book's details and delete books entirely. When you update the reading status to "Finished", you will see the count of books and pages read update in the book's genre menu.

## Getting Started

1. Fork and clone this repository.
2. In the project directory, type `pipenv install ; pipenv shell` in the terminal to install dependencies and start a virtual environment.
3. Type `python lib/cli.py` to start Libro Tracker. 

Some sample genres and books are provided. Enter `python lib/seed.py` to seed the database with sample data, or start fresh with your own genres and books!

## Contributing
Contributions are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## MIT License
Copyright (c) 2025 Riko Fluchel

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.