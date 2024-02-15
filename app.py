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

    # Call the code generation script with the GitHub link
    result = subprocess.run(['python', 'codegen.py'], input=github_link.encode(), text=True, capture_output=True)
    
    if result.returncode == 0:
        return result.stdout
    else:
        return 'Error occurred while generating documentation.'

if __name__ == '__main__':
    app.run(debug=True)

