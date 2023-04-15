# [![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Python Command Line Application

To learn Python and SQL, I built a command line application!

### Note Taker

Users sould be able to create notes with titles and contents. They should be
able to see a list of their notes and select and view a specific note.

## Instructions

1.  Clone this repository.
1.  (Optional) Set up the SQL database for this exercise (instructions below).
1.  Change into directory created from clone

## Setup

Before you get started, create a new database called `carmen` and load the
provided data in `world.sql`:

```sh
# Enter psql:
psql

# Create database:
CREATE DATABASE notes;

# Connect to notes:
\c notes

# Load note.sql:
\i path/to/notes.sql
# (replace /path/to/notes.sql with the actual path to the file)
```

## Bonus

Once you have the command line version working consider the following bonuses:

1. Get Update and Delete working
1. Build a user interface with [tkinter](https://docs.python.org/3/library/tk.html), [pygame](https://www.pygame.org/), or [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
1. Use web scraping to pull data from a webpage using [requests](https://2.python-requests.org/en/master/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## [License](LICENSE)

1.  All content is licensed under a CC­BY­NC­SA 4.0 license.
1.  All software code is licensed under GNU GPLv3. For commercial use or
    alternative licensing, please contact legal@ga.co.
