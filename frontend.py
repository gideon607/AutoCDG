#!/usr/bin/python3
# frontend.py

import requests

def main():
    # Gets the input from the user (GitHub URL or code snippet)
    github_link = input("Enter GitHub repository URL: ")

    # Send GitHub link to Flask backend
    response = requests.post('http://localhost:5000/generate', json={'githubLink': github_link})
    print(response.text)

if __name__ == "__main__":
    main()

