import google.generativeai as genai

genai.configure(api_key="AIzaSyA3Q7nsLPniUdzsl95en6QJHF1dme_WAkM")

# Function to generate automated response
def generate_automated_response(issue):
    tags_combined = " ".join(issue["tags"])
    prompt = f"""
    Generate a helpful automated response based on the following issue details:
    Priority: {issue['priority']}
    Tags: {tags_combined}
    Please provide a human-readable response in the format: "Subject" and "Body"
    """

    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    return response.text.strip()
