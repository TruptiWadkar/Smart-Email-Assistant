import json
import os

# Escalation threshold 
CONFIDENCE_THRESHOLD = 0.6
ESCALATION_LOG_PATH = "escalation_log.txt"

def escalate_email(email_text, predicted_category, confidence):
    """
    Logs emails for manual review if:
    - Confidence is low
    - OR category is 'Other'
    """
    # Check if the email should be escalated
    if confidence < CONFIDENCE_THRESHOLD or predicted_category.lower() == "other":
        # Create a log entry
        entry = {
            "email_text": email_text,
            "predicted_category": predicted_category,
            "confidence": confidence
        }

        # Save to file
        with open(ESCALATION_LOG_PATH, "a") as file:
            file.write(json.dumps(entry) + "\n")

        return {
            "status": "escalated",
            "reason": "Low confidence or unknown category",
            "logged_to": ESCALATION_LOG_PATH
        }

    else:
        return {
            "status": "not_escalated",
            "reason": "Confidence OK and category known"
        }

# Test the escalation logic
if __name__ == "__main__":
    result = escalate_email(
        "Can I work from home tomorrow?",
        "Other",
        0.45
    )
    print(result)
