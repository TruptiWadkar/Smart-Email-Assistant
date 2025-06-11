# orchestrator.py

import joblib
from Agents.response_generator import generate_response
from Agents.escalation_agent import escalate_email
import os
import sys

# Load classifier model and vectorizer
MODEL_PATH = "models/email_classifier.pkl"
VECTORIZER_PATH = "models/vectorizer.pkl"

# Confidence threshold
CONFIDENCE_THRESHOLD = 0.6

# Load the ML model and vectorizer
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
except FileNotFoundError:
    print("Error: Model files not found. Train your model first using email_classifier.py")
    sys.exit()

# Main pipeline function
def process_email(email_text):
    # Step 1: Transform email to vector
    X = vectorizer.transform([email_text])

    # Step 2: Predict category + confidence
    predicted_category = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]
    confidence = max(probabilities)

    print(f"Predicted: {predicted_category} | Confidence: {confidence:.2f}")

    # Step 3: Route to correct agent
    if confidence >= CONFIDENCE_THRESHOLD and predicted_category != "Other":
        # Generate AI response
        response_data = generate_response(email_text, predicted_category)
        return {
            "stage": "response_generated",
            "response": response_data.get("response"),
            "category": predicted_category,
            "confidence": round(confidence, 2)
        }
    else:
        # Escalate email
        escalation_data = escalate_email(email_text, predicted_category, confidence)
        return {
            "stage": "escalated",
            **escalation_data,
            "category": predicted_category,
            "confidence": round(confidence, 2)
        }

# Manual test
if __name__ == "__main__":
    test_email = input("Enter email text: ")
    result = process_email(test_email)
    print("\n Final Output:")
    print(result)
