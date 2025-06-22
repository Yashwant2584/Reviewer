# ReviewPulse

**ReviewPulse** is a web-based product sentiment analysis platform that aggregates and analyzes reviews from Reddit, Twitter (X), and YouTube for any searched product.

## Features
- Aggregates reviews from Reddit, Twitter, and YouTube
- Uses Hugging Face Transformers for sentiment analysis
- Visualizes insights, trends, and keyword clouds
- Stores processed results in MongoDB
- Interactive dashboard (Streamlit)

## Tech Stack
- Python, FastAPI, Streamlit, MongoDB, Hugging Face Transformers, Docker

## Project Structure
```
ReviewPulse/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── database/
│   └── utils/
├── dashboard/
├── data/
├── tests/
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

## Quick Start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up your `.env` file with API keys.
3. Run the FastAPI backend:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Run the Streamlit dashboard:
   ```bash
   streamlit run dashboard/app.py
   ```

## License
MIT
