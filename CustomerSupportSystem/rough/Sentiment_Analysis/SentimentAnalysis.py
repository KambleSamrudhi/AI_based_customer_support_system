import google.generativeai as genai

genai.configure(api_key="AIzaSyA3Q7nsLPniUdzsl95en6QJHF1dme_WAkM")
model = genai.GenerativeModel("gemini-pro")

# Function to get sentiment analysis
def get_sentiment(title, chat_history):
    prompt = f"Analyze the sentiment of the following text:\nTitle: {title}\nBody: {chat_history}\nPlease classify the sentiment as positive, negative, or neutral."
    response = model.generate_content(prompt)
    sentiment = response.text.strip()
    return sentiment
