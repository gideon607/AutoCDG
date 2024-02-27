# AutoCDG

AutoCDG is a web application and CLI tool designed to generate documentation for GitHub projects. It aims to streamline the process of documenting projects, saving time and energy for developers.
![Screenshot 2024-02-26 122021](https://github.com/gideon607/AutoCDG/assets/48885554/0d28810c-72b6-4b39-9712-27d077598c33)

## Installation

### Web Version

The web version of AutoCDG is built using Flask. Follow these steps to install and configure it:

1. Install Flask:

   ```
   pip install Flask
   ```

2. Edit `app.py` to customize Flask settings according to your needs.

### CLI Version

The CLI version allows for command-line usage to start the program and retrieve `documentation.txt` from the server. Install dependencies as follows:

1. Install spaCy for Python:

   ```
   pip install spacy
   python -m spacy download en_core_web_sm
   ```

2. Install NLTK Toolkit for natural language processing:

   ```
   pip install nltk
   ```

3. Install XDG-utils:

   ```
   sudo apt-get install xdg-utils
   ```

## Usage

### CLI Version

Navigate to the directory containing the CLI version and execute:

```
./codemain.py
```
or
```
python3 codemain.py
```

Then, enter the GitHub link (e.g., `https://github.com/username/project`).

### Web Version

To use the web version:

1. Install Flask (if not already installed).

2. Modify settings in `app.py` to specify the server address (`serveraddress:5000`).

3. Run the Flask app:

   ```
   ./app.py
   ```

## Documentation

Visit [AutoCDG Documentation](https://autocdg.webflow.io/) for detailed instructions on how to use AutoCDG.

## Contributions

Contributions to make AutoCDG more efficient and robust are welcome. Feel free to contribute by submitting pull requests or reporting issues.

Bugs bounty is also welcome. Please note any bugs found, especially those related to frontend-backend communication issues.

## License

AutoCDG is open-source software distributed under the MIT License. You are free to distribute and run it actively on any hosting platform.
