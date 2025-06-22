def summarize(text: str) -> str:
    # Dummy summarizer
    return text[:200] + ("..." if len(text) > 200 else "")
