#!/usr/bin/python3
# app.py

from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_documentation():
    github_link = request.json['githubLink']

    if not isinstance(github_link, str):
        return 'invaild github link format.'

    # Call the code generation script with the GitHub link
    result = subprocess.run(['python3', 'codemain.py'], input=github_link, text=True, capture_output=True)

    if result.returncode == 0:
        return result.stdout
    else:
        return 'Error occurred while generating documentation.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

