# Instructions to parse football club data from Instagram without using Instagram's API

## Aim of the project
A friend needed to perform statistics on multiple months of Instagram posts of famous football clubs. I have therefore 
established a simple workflow to programmatically extract Instagram post metrics, such as the like and comment counts, 
for a set of accounts of interest for a given time frame. This code is a convenience tool that makes use of your active 
Instagram session to extract the posts without using Instagram's API. Please note that the code was written in June 2023 
and could at some point not work anymore.

## Disclaimer
Owing to the use of browser's cookies and your own Instagram account to access the posts programmatically, Instagram might 
notice an unusual activity on your account and temporarily block it. I therefore suggest you create a new Instagram account 
specifically for the extraction, to protect your own account. This script was made to provide publicly available data 
for a Master thesis, i.e. for an educational purpose, and I will not take any responsibility for any deviant use of my code.

## Dependencies
### First set-up
1. Download `virtualenv` if you do not alread have it
```bash
pip install virtualenv
```
2. Create virtual environment in your folder of interest
```bash
virtualenv insta-parsing
```
3. Activate the virtual environment
```bash
source insta-parsing/bin/activate
```
4. Install the libraries of interest in the virtual environment based on the `requirements.txt` file
```bash
pip install -r requirements.txt
```

### Re-activate virtual environment every time you need to extract data
```bash
source insta-parsing/bin/activate
```

## Account permission
### Connect to a secondary account on Firefox

### Store the cookies and session details to a local file
```bash
python3 615_import_firefox_session.py
```

## Define the Instagram account list and time frame to target
### Fill the list of accounts of interest
The list of Instagram accounts should be simply the account IDs formatted as shown in the file `clubs.txt`.

### Define the time frame for the post extraction
The time frame should be specified in the file `date.txt` and should follow the same format.


## Extraction
### Run the extraction script
```bash
python3 insta_parsing.py
```

### Manual curation
Verify the printed comments and repeat the download for the accounts which had an error.
