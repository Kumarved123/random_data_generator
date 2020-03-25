# Random Data Generator
Generates random customized datas in different file formates
## Introduction to the problem
The task is to create a Random Data Generator to download large amounts of randomly generated test data. The user can define the schema of the data and generate several rows of realistic test data in various formats. 

## Solution
I have used python Django and made a web application that generates the customized and OnDemand test data in several formats in any number.
To generate the random data I have used Faker and some list with the random function of python to generate data and then I have stored in lists of the list data structure. I have used the panda’s data frame as the staged data to convert it further to different formats of data like csv, json, xml, tsv elc  .
![Untitled presentation](https://user-images.githubusercontent.com/46513056/77521114-30c50200-6ea8-11ea-9c18-0606124dd014.jpg)

All the generated file is downloaded in the download folder of the project
## Technology Used
- Python Django - Backend
- HTML 
- CSS
- Javascript
- Jquery
- Knockout.js
## Installation
Before using this install panda, NumPy, Faker

```bash
pip install Faker

```
```bash
pip install pandas
```
```bash
pip install numpy
```
## How to Use
Command:in manage.py directory
```bash
Python manage.py runserver
```
Run the local server and use the web application
