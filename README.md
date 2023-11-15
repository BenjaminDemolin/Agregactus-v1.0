# Agregactus V1.0

## Overview

Agregactus is your go-to tool for effortlessly staying informed and sharing summarized news on social media. It not only scrapes news websites, summarizes articles, and generates tweets but also poses insightful questions alongside. All of this is neatly stored in a PostgreSQL database and sent via email.

## Features
* Web Scraping: Extracts the latest news from specified websites.
* Summarization: Condenses articles while retaining key information.
* ChatGPT Integration: Crafts engaging tweets and questions using ChatGPT.
* Database Storage: Utilizes PostgreSQL to store tweet and question data.
* Email Notification: Sends tweets and questions via email.
* Configurability: Easily configurable through a .env file for email, OpenAI key, and database information.

## Getting Started

### Prerequisites
Python 3.x  
PostgreSQL (can use Docker image)  
Dependencies listed in requirements.txt  

### Installation
Clone the repository:

```bash
git clone https://github.com/BenjaminDemolin/Agregactus-v1.0.git
cd Agregactus-v1.0
pip install -r requirements.txt
```

### Env file configuration

Create a .env file in the root directory of the project and fill it with the following information:

```bash
DB_HOST|DB_NAME|DB_USER|DB_PASSWORD|DB_PORT = PostgreSQL database information.
OPENAI_API_KEY = OpenAI API key (https://platform.openai.com/api-keys).
EMAIL_SENDER_ADDRESS|EMAIL_SENDER_PASSWORD|EMAIL_RECEIVER_ADDRESS = Email information.
```

### Run Agregactus:

python main.py



