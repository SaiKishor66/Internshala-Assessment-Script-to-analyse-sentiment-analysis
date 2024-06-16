import spacy
from textblob import TextBlob

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Sample interview responses 
responses = [
    "I am a software developer with 5 years of experience in web development. I have worked with various technologies including Python, JavaScript, and React.",
    "My biggest strength is my problem-solving ability. However, I sometimes struggle with time management, but I am working on improving it.",
    "I want to work at your company because of your commitment to innovation and the opportunities for growth that you offer.",
    "In my previous job, I faced a situation where we had to deliver a project under a tight deadline. I coordinated with my team, prioritized tasks, and we successfully delivered the project on time.",
    "In 5 years, I see myself leading a team of developers and contributing to innovative projects that make a difference."
]

def analyze_sentiment(response):
    analysis = TextBlob(response)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

def extract_key_phrases(response):
    doc = nlp(response)
    key_phrases = [chunk.text for chunk in doc.noun_chunks]
    return key_phrases

def assess_quality(sentiment, key_phrases):
    if sentiment == 'Positive' and key_phrases:
        return 'High'
    elif sentiment == 'Negative':
        return 'Low'
    else:
        return 'Medium'

# Analyze each response
for i, response in enumerate(responses):
    sentiment = analyze_sentiment(response)
    key_phrases = extract_key_phrases(response)
    quality = assess_quality(sentiment, key_phrases)
    
    print(f"Response {i+1}:")
    print(f"Sentiment: {sentiment}")
    print(f"Key Phrases: {', '.join(key_phrases)}")
    print(f"Overall Quality: {quality}\n")
