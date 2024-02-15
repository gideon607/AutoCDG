#!/usr/bin/python3
# codemain.py

import os
import subprocess
import requests
import nltk
from nltk.tokenize import sent_tokenize
import spacy

# This will download NLTK resources if not already downloaded
nltk.download('punkt')

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def generate_documentation(code):
    # Tokenize code into sentences
    sentences = sent_tokenize(code)

    # Perform NLP tasks on each sentence
    processed_sentences = []
    for sentence in sentences:
        doc = nlp(sentence)
        # Extract relevant information from NLP analysis
        processed_sentences.append(doc.text)  # For demonstration, just use the original sentence

    # Join processed sentences into documentation
    documentation = '\n'.join(processed_sentences)
    return documentation

def fetch_code_from_github(repo_url):
    # Extract username and repository name from the URL
    _, _, _, username, repo_name = repo_url.split('/')

    # Fetch code from GitHub API
    api_url = f"https://api.github.com/repos/{username}/{repo_name}/contents"
    response = requests.get(api_url)
    response.raise_for_status()

    # Extract and concatenate code from all files
    code = ""
    for item in response.json():
        if item['type'] == 'file' and item['name'].endswith('.py'):  # Consider Python files only
            file_url = item['download_url']
            file_content = requests.get(file_url).text
            code += file_content + '\n'

    return code

def main():
    # Get input from the user (GitHub URL or code snippet)
    user_input = input("Enter GitHub repository URL or code snippet:\n")

    if user_input.startswith("https://github.com/"):
        # Fetch code from GitHub repository
        code = fetch_code_from_github(user_input)
    else:
        # Use input as code snippet
        code = user_input

    # Generate documentation
    documentation = generate_documentation(code)

    # Write documentation to a file
    with open("documentation.txt", "w") as file:
        file.write(documentation)

    print("Documentation generated successfully!")

    # Open the generated documentation file
    subprocess.run(["xdg-open", "documentation.txt"])  # Linux-specific, change as needed for other platforms

if __name__ == "__main__":
    main()

