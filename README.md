# AI Email Generator

An AI-powered web application that generates professional emails based on the recipient, email type, purpose, tone, length, and additional information provided by the user.

## Live Demo

[Try the AI Email Generator](https://ai-email-generator1.streamlit.app/)

## Features

* Generate professional emails using AI
* Multiple email types
* Different writing tones
* Short, medium, and detailed email lengths
* Custom additional information
* Automatically generates a suitable subject line
* Simple and user-friendly interface

## Technologies Used

* Python
* Streamlit
* Groq API
* GPT-OSS-20B via Groq
* Git & GitHub

## Project Structure

```text
ai-email-generator/
├── app.py
├── email_generator.py
├── requirements.txt
├── README.md
└── .gitignore
```

## API Key Setup

This project uses the Groq API.

For local development, create:

```text
.streamlit/secrets.toml
```

Add your Groq API key:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

**Never upload `secrets.toml` to GitHub.**

## Run Locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## How It Works

1. Enter the recipient and purpose of the email.
2. Select the email type, tone, and length.
3. Add any additional information.
4. The application sends the details to the Groq API.
5. The AI generates a professional email and subject line.
6. The generated email is displayed in the application.

## Security

The Groq API key is stored securely using Streamlit secrets and is not included in the source code or GitHub repository.

## Future Improvements

* Email copy button
* Download generated emails
* Email history
* More customization options
* User authentication
* Support for additional AI models

## Author

**Areeba Shafqat**

BS Computer Science Student
PAF-IAST
