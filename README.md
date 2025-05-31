Weather Checker Web App 🌤️
A simple and elegant weather app built with Flask and OpenWeatherMap API that shows current weather by city name or your location. Includes a stylish video background and loading spinner for a smooth user experience.

Features
Search weather by city name or use your current location

Displays temperature, weather description, and icon

Responsive UI with background video

Loading spinner while fetching data

Demo
[Insert link to your deployed app or demo video here]

Tech Stack
Python 3.x

Flask

OpenWeatherMap API

HTML, CSS, JavaScript

Setup & Installation
Clone this repo:

bash
Copy
Edit
git clone https://github.com/yourusername/weather-checker.git
cd weather-checker
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Get an OpenWeatherMap API key at https://openweathermap.org/api.

Create a .env file in the project root and add your API key:

ini
Copy
Edit
API_KEY=your_openweathermap_api_key_here
Run the Flask app:

bash
Copy
Edit
flask run
Open your browser at http://127.0.0.1:5000

Usage
Enter a city name or click Use My Location to fetch weather info.

The app displays current temperature, weather icon, and description.

Enjoy the background video and smooth loading spinner while fetching data.
