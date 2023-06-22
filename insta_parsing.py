# -*- coding: utf-8 -*-
"""
Instagram Club Post Extractor Script

This script extracts posts from a list of Instagram profiles (e.g. clubs) within a specified date range
and saves the results to a file. The script uses the Instaloader library to interact with Instagram
and requires user credentials for authentication.

Features:
- Reads a list of Instagram profile usernames from a file ('clubs.txt').
- Filters posts based on a date range specified in 'date.txt'.
- Writes the extracted post data, including likes, comments, video status, and URLs, to 'club_posts.txt'.

Prerequisites:
- A valid Instaloader session file must be available for the specified username.
- Required libraries: instaloader, python-dotenv, datetime, os, time.

Usage:
1. Prepare the required files:
   - `date.txt`: Specify the start and end dates (e.g., "2022.8.14\n2022.10.15").
   - `clubs.txt`: List the Instagram account IDs to process (one per line).

2. Run the script:
   python script_name.py

3. View the results in 'club_posts.txt'.

Author: Boris
Date: 2023 Jun 22
"""


# Importing Libraries
import os
import time
from datetime import datetime
from dotenv import load_dotenv
import instaloader

# Load user name
load_dotenv()
USER_NAME = os.getenv("USER_NAME")
# PWD = os.getenv("PWD")  # Load password

# Read dates from date.txt
with open("date.txt", "r") as date_file:
    lines = date_file.readlines()
    start_date = datetime.strptime(lines[0].strip(), "%Y.%m.%d")
    end_date = datetime.strptime(lines[1].strip(), "%Y.%m.%d")

# Get instance
L = instaloader.Instaloader()

# Optionally, login or load session
#L.login(USER_NAME, PWD)        # (login)
#L.interactive_login(USER_NAME)    # (ask password on terminal)
L.load_session_from_file(USER_NAME) # (load session created w/

# Create output file with its header
with open('club_posts.txt', 'w') as output:
    output.write("Club\tDate\tLikes\tComments\tisVideo\tLink\n")

# Read club list
with open('clubs.txt', 'r') as input:
    for line in input:
        club = line.rstrip()  # Remove newlines at the end of each line
        profile = instaloader.Profile.from_username(L.context, club)

        # Extract each post per club within the given dates
        print("Club: {}".format(club))
        with open('club_posts.txt', 'a') as output:
            try:
                for post in profile.get_posts():
                    # L.download_post(post, target=profile.username)
                    # print(post.date, post.likes, post.comments, post.get_is_videos)
                    if post.date > start and post.date < end:
                        output.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(club, str(post.date), str(post.likes), str(post.comments), ",".join([str(bool) for bool in post.get_is_videos()]), post.url))
            except instaloader.exceptions.ConnectionException as e:
                print(f"Connection error for {club}: {e}")
                time.sleep(60)  # Shorter delay for recoverable errors
            except instaloader.exceptions.LoginRequiredException as e:
                print(f"Login required for {club}: {e}")
            # Handle re-login or fail gracefully
            except Exception as e:
                print(f"Unexpected error for {club}: {e}")
                time.sleep(60 * 10)  # Longer delay for unknown issues
        time.sleep(60*2)  # Wait 2 minutes between each club just as an additional safety measure for the API request limit
