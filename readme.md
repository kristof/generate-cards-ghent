# Generate cards from CSV
This script generates a pdf called `cards.pdf` containing pages with the source file `card.pdf` filled in with the data from `data.csv`.

## 1. CSV structure
The CSV file should be structured as pictured below.

`FirstName;LastName;BirthNate;ImageUrl`

## 2. Installing requirements
Requirements can be installed with `pip install`, recommended is to do this in a virtual environment to keep dependencies seperate from system dependencies.

## 3. Running the script
The script can be run like as  `./generate-cards.py data.csv`


## 4. Remarks
Don't generate too many cards at the same time since these cards are kept in memory until it's finished.


## 5. Questions
Contact [kristof.houben@citylife.be](kristof.houben@citylife.be)