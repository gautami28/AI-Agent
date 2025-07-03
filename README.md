# AI-Agent

# 📘 SimplifyIt – AI Concept Explainer

An AI-powered assistant that simplifies academic concepts using Wikipedia summaries and real-world examples generated with the Cohere AI API.

---

## Features

- Takes any academic concept input from the user
- Fetches a simplified Wikipedia summary
- Generates a clear, complete example using Cohere AI
- Provides a YouTube search link for further exploration

---

## Project Structure

```bash
.
├── app.py              # Flask backend server
├── templates/
│   └── index.html      # Frontend interface
├── static/             # Optional for CSS/JS files
├── .env.example        # Template for environment variables
├── requirements.txt    # Python dependencies
└── README.md           # You're here!

⚙️ Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/simplifyit-ai-concept-explainer.git
cd simplifyit-ai-concept-explainer

2. Install Required Packages

Flask
Wikipedia API (python)
Cohere AI
dotenv

3. Create Your .env File

Create a file named .env in the root directory and add your Cohere API key:
COHERE_API_KEY=your-cohere-api-key-here

4. Run the app

python app.py
OR
"file_path" app.py

5. Visit the localhost site mentioned as per the port

ScreenShots:

![image2](https://github.com/user-attachments/assets/b70e0183-e992-4ebf-96dc-21f30becae71)

![image3](https://github.com/user-attachments/assets/04d67911-dabd-4a97-9335-2a607c33d94c)


