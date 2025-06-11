#AIzaSyCeVGaSAsBTor7tMIRDYrUpKA6hsMoo4u4
#Import Gemini SDK
import google.generativeai as genai

# Configure  Gemini API key
genai.configure(api_key="AIzaSyCeVGaSAsBTor7tMIRDYrUpKA6hsMoo4u4") 

# Define the response generation function
def generate_response(email_text, predicted_category):
    # Create the prompt for Gemini
    prompt = f"""
You are a helpful assistant working in a company.
Your task is to reply to internal company emails politely and professionally.

Email category: {predicted_category}
Email content: {email_text}

Write a short, clear, and professional email reply based on the category.
"""

    try:
        # Use Gemini model 
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        # Generate response (input must be a list)
        response = model.generate_content([prompt])

        # Return only the text part
        return {"response": response.text.strip()}

    except Exception as e:
        # Handle errors safely
        return {"error": str(e)}


# Manual test
if __name__ == "__main__":
    test_email = "Hi, I can't access the company VPN. Please help."
    test_category = "IT"
    result = generate_response(test_email, test_category)
    print(result)

