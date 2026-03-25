# 🎬 YouTube Summarizer

An intelligent web application that automatically generates concise summaries of YouTube videos using Google's Gemini AI. Extract key points, insights, and practical applications from any video with a single click.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask 2.3](https://img.shields.io/badge/flask-2.3-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)

## ✨ Features

- **🤖 AI-Powered Summaries**: Uses Google Gemini 2.5 Flash for fast, accurate content summarization
- **📝 Structured Output**: Generates summaries with:
  - Concise overview
  - Key points
  - Actionable insights
  - Real-world applications
- **🎯 Custom Instructions**: Add specific prompts to tailor summaries to your needs
- **🔗 Multi-Format Support**: Accepts YouTube links in multiple formats
- **🌐 Web Interface**: Clean, intuitive UI built with Flask and Bootstrap
- **🐳 Docker Ready**: Pre-configured for containerized deployment
- **☁️ Cloud Deployment**: Ready for Google Cloud Run, Heroku, or any cloud platform

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## 📦 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- A Google Gemini API key ([Get it free here](https://ai.google.dev))
- A YouTube video link with captions/transcripts

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BHARGAVC1/youtube-summarizer.git
cd youtube-summarizer
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Configuration

### Set Up Your Google Gemini API Key

1. Visit [Google AI Studio](https://ai.google.dev) and get your free API key
2. Set the environment variable:

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY = "your-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your-api-key-here
```

**macOS/Linux:**
```bash
export GEMINI_API_KEY=your-api-key-here
```

**For development, create a `.env` file:**
```
GEMINI_API_KEY=your-api-key-here
```

Then load it in your application or use `python-dotenv`:
```bash
pip install python-dotenv
```

## 💻 Usage

### Running Locally

```bash
python app.py
```

The application will start at `http://localhost:8080`

### Using the Web Interface

1. Open `http://localhost:8080` in your browser
2. Paste a YouTube video link in the input field
3. *(Optional)* Add custom instructions to focus the summary
4. Click "Summarize"
5. View your structured summary with key points and insights

### Example

```
Input: https://www.youtube.com/watch?v=xxxxxxxxxxx
Custom Prompt: Focus on technical implementation details

Output:
- Summary: [AI-generated concise overview]
- Key Points: [Bullet points of main topics]
- Insights: [Deep-dive analysis]
- Applications: [Practical uses and implementations]
```

## 📁 Project Structure

```
youtube-summarizer/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── Procfile               # Heroku deployment config
├── README.md              # This file
├── templates/
│   ├── index.html         # Main input page
│   └── result.html        # Summary results page
├── static/
│   └── style.css          # Application styling
└── img/                   # Documentation images
```

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python 3.9+ |
| Web Framework | Flask 2.3.3 |
| AI Engine | Google Gemini 2.5 Flash |
| Transcript Extraction | youtube-transcript-api |
| Web Server | Gunicorn |
| Containerization | Docker |

## 📊 Dependencies

```
Flask==2.3.3              # Web framework
google-genai==1.2.0       # Google Gemini API
youtube-transcript-api==0.6.2  # YouTube transcript extraction
gunicorn==21.2.0          # Production WSGI server
```

## ☁️ Deployment

### Docker Deployment

```bash
# Build the Docker image
docker build -t youtube-summarizer .

# Run the container
docker run -p 8080:8080 -e GEMINI_API_KEY=your-key-here youtube-summarizer
```

### Google Cloud Run

```bash
# Deploy to Cloud Run
gcloud run deploy youtube-summarizer \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY=your-key-here
```

### Heroku

```bash
# Login to Heroku
heroku login

# Create a new app
heroku create your-app-name

# Set environment variable
heroku config:set GEMINI_API_KEY=your-key-here

# Deploy
git push heroku main
```

## 🐛 Troubleshooting

### "Repository not found" error
Ensure your YouTube video has accessible transcripts/captions.

### API quota exceeded
Check your Google Gemini API usage limits and rate limits.

### Transcript fetch fails
- Verify the YouTube URL is valid
- Some videos may have transcripts disabled
- Try a different video with captions enabled

## 🤝 Contributing

Contributions are welcome! Here's how to help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Support

For issues, questions, or suggestions, please open an [issue](https://github.com/BHARGAVC1/youtube-summarizer/issues) on GitHub.

---

**Made with ❤️ by [Your Name]**
