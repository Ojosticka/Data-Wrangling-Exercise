# Date Created

This project was created on the 12th of August 2021

## Project Title

Data Wrangling Challenge, Junior Software Engineer - Datopian

## Description

This is a project used to scrape data from a website. The goal is to get a table from the site that explains the rate at which road accident deaths occur in European Union Countries, clean the data, and add visualizations to help with understanding the data.

## Setting up for the project

To help with choices, I created a `.py` script and also a `.ipynb` script, this helps the user go with his favourite platform for running python/data wrangling codes.

To use this project locally,

- [python](https://www.python.org/downloads/) for `.py` or
- [anaconda](https://www.anaconda.com/products/individual) for `.ipynb` or
- better still a code editor such as [Vscode](https://code.visualstudio.com/download) which is my personal best as it can run both files seamlessly. It should be installed alongside an interpreter, i suggest [python pack](https://code.visualstudio.com/docs/python/coding-pack-python).
- [Power bi desktop](https://powerbi.microsoft.com/en-us/downloads/) will be needed to view the visualized file, chart summary.

### 1. Clone the repository

    `git clone https://github.com/Ojosticka/Data-Wrangling-Exercise.git`

### 2. Start the virtual environment: Run the following commands in the project root folder

    `virtualenv env
     source env/Scripts/activate # for windows
     source env/bin/activate # for MacOs`

### 3. Install Extensions

    `pip install pandas`

### 4. Running the script: In the project root directory, run any of

    `python Road_safety_project/Script/script.py
     conda Road_safety_project/Script/script.ipynb`

## How the Script works

`get_data` function is used for solving this challenge.
The get_data function takes the wikipedia url and scrapes it for the data necessary by indexing the list of tables gotten for the specific table. This data is then arranged and filtered according to the requiremnets of the task.
The resulting data is then populated to a CSV file located in the [data folder](Road_safety_project/data)
