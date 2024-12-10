# Zootopia With API

This project generates a webpage showcasing different animals. The information is fetched dynamically from an external API (API Ninja) based on the user's input. The user enters the name of an animal, and the program generates a website displaying details of the animal fetched from the API.

## Features
- Fetches animal information from the API based on user input.
- Displays animal characteristics, diet, location, and type in a card-style layout on a webpage.
- Handles cases where the animal does not exist in the API's database.

## Installation

### Requirements:
- Python 3.x
- Pip (Python's package manager)

### Install Dependencies:
To get started, clone the repository and install the required libraries:

```bash
git clone https://github.com/your_username/zootopia_with_api.git
cd zootopia_with_api
pip3 install -r requirements.txt
requests: A library for making HTTP requests to the API.
python-dotenv: A library to manage environment variables.
Set up API Key:
Create a .env file in the root directory of the project.
Add your API key to the .env file:
plaintext
Copy code
API_KEY='your_api_key_here'
You can get the API key from API Ninja.

Run the Program:
Once the dependencies are installed and the API key is set up, run the program:

bash
Copy code
python3 animals_web_generator.py
Example:
The program will ask for an animal name, such as "Fox".
It will fetch the animal data and generate an HTML file (animals.html).
Open animals.html in your browser to view the generated webpage.
Project Structure:
animals_data.json: Static data for the animals (if used).
animals_template.html: The template HTML structure used to generate the webpage.
animals_web_generator.py: Main script that generates the HTML file.
data_fetcher.py: Script responsible for fetching data from the API.
.env: Stores sensitive information like the API key.
Contributions
Feel free to fork the repository and make contributions. If you have any suggestions or bug fixes, create a pull request!