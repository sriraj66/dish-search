# Django Restaurant Dish Search Application

This Django application allows users to search for dishes by name and receive recommendations based on several criteria including highest rating, nearest location, user ratings, votes, and price. The application leverages Bootstrap for a responsive design and the Geolocation API to get the user's current location.

## Features

- Search for dishes by name.
- Recommendations are based on:
  - Highest rating.
  - Nearest location to the user.
  - User ratings.
  - Number of votes.
  - Price.
- Display search results in a structured card format.
- Fetch current user location for proximity-based recommendations.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/sriraj66/dish-search.git
   cd dish-search
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the project root to set environment variables:**
   ```sh
   SECRET_KEY=your_secret_key
   DEBUG=True
   ```

5. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

## Running the Application

1. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

2. **Open your web browser and go to:**
   ```
   http://127.0.0.1:8000/
   ```

## Usage

1. **Navigate to the main page:**
   - You will see a form where you can enter the name of a dish and optionally get your current location.

2. **Enter the dish name and click "Search":**
   - If results are found, they will be displayed in a structured card format.
   - If no results are found, 5 random items will be displayed.

3. **Get Location:**
   - Click the "Get Location" button to automatically fill in the location input with your current latitude and longitude.

For more details, visit the [GitHub repository](https://github.com/sriraj66/dish-search).
