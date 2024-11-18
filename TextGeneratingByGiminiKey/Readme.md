# Gemini Text Generation Chatbot

This project uses Google’s Gemini API to create a chatbot that generates text responses based on user prompts. It integrates with Streamlit to provide a simple and interactive web interface for users to input questions or prompts, and get AI-generated responses in real-time.

## Features

- **Text Generation**: Generate responses using the Gemini model.
- **Streamlit Interface**: A simple web-based UI to interact with the chatbot.
- **API Integration**: Integrates with Google’s Gemini API for generating text responses.

## Project Structure
gemini-text-generation-chatbot/ │ ├── .env 
- Environment configuration file for API key ├── app.py 
- Main application to run the chatbot ├── requirements.txt 
- Python dependencies required for the project └── README.md 
- This file

### Files Description

- **`.env`**:
   - Stores sensitive environment variables, such as the `GEMINI_API_KEY`, to authenticate with the Gemini API.
   
- **`app.py`**:
   - The core Python script that loads the Gemini API, handles user input through Streamlit, and generates responses based on prompts.
   
- **`requirements.txt`**:
   - Contains a list of Python packages required to run the project. Install them with:
     ```bash
     pip install -r requirements.txt
     ```

## Prerequisites

Before running the project, ensure that you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation

Follow these steps to set up the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/gemini-text-generation-chatbot.git
cd gemini-text-generation-chatbot

### Step 2: Set Up Virtual Environment
python -m venv venv
.\venv\Scripts\activate

# Step 3: Install Dependencies
pip install -r requirements.txt

# Step 4: Configure API Key
1. Copy .env.example to .env:
  cp .env.example .env
2. Open the .env file and add your Gemini API key:
  GEMINI_API_KEY=your_api_key_here

# Step 5: Run the Application
streamlit run app.py

