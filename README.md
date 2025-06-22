# ReviewPulse

ReviewPulse is an intelligent sentiment analysis dashboard that aggregates user opinions about any product from multiple sources (Twitter, Reddit, and YouTube). It uses advanced NLP models to analyze sentiment, emerging trends, and feature-specific opinions (e.g., battery life, price, camera).

## Features
- 🔍 **Multi-Source Aggregation:** Collects reviews and comments from Twitter, Reddit, and YouTube.
- 🤖 **AI-Powered Sentiment Analysis:** Uses state-of-the-art NLP models to classify sentiment (positive, negative, neutral).
- 📊 **Interactive Dashboard:** Visualizes sentiment distribution, trends, and keyword clouds.
- 🏷️ **Top Insights:** Highlights the most positive and negative reviews.
- 🔒 **Secure:** Keeps API keys and secrets safe using a `.env` file (not tracked by git).

## Real-World Problem It Solves
Consumers face information overload when researching products. ReviewPulse offers condensed, trustworthy insights pulled from multiple platforms to support better purchase decisions. Businesses can also monitor brand sentiment or competitor reviews.

## Project Structure
```
Reviewer/
│   .env                # Environment variables (not tracked by git)
│   requirements.txt    # Python dependencies
│   Dockerfile          # For containerized deployment
│   README.md           # Project documentation
│
├───app/
│   ├───database/       # MongoDB client setup
│   ├───models/         # Sentiment model loader
│   ├───routes/         # FastAPI route handlers
│   ├───services/       # Preprocessing, scraping, sentiment logic
│   └───utils/          # Summarizer and helpers
│
├───dashboard/          # Streamlit dashboard app
├───data/               # Sample outputs and data
└───tests/              # Unit tests
```

## Getting Started

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd Reviewer
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory with your API keys:
```env
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=your_agent
TWITTER_BEARER_TOKEN=your_token
YOUTUBE_API_KEY=your_key
MONGO_URI=mongodb://localhost:27017/reviewpulse
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the FastAPI Backend
```sh
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.

### 5. Run the Streamlit Dashboard
```sh
streamlit run dashboard/app.py
```
The dashboard will open in your browser and connect to the backend.

## Usage
- Enter a product name in the dashboard to fetch and analyze reviews.
- View sentiment distribution, keyword clouds, and top reviews.
- Expand the raw data section for detailed API output.

## Security
- **Never commit your `.env` file.** It is included in `.gitignore` by default.
- Store all API keys and secrets in `.env` only.

## License
MIT License

---

**ReviewPulse** — Make smarter decisions with AI-powered review insights!
