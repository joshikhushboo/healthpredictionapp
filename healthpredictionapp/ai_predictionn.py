import google.generativeai as genai

# Replace with your Gemini API key
genai.configure(api_key="AQ.xxxxx")

model = genai.GenerativeModel("gemini-1.5-flash")

def predict_health(glucose, haemoglobin, cholesterol):

    prompt = f"""
    Analyze these blood test values and provide a short health remark.

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Give only a concise health assessment.
    """

    try:
        response = model.generate_content(prompt)

        if response.text:
            return response.text

        return "No prediction generated."

    except Exception as e:
        print("Gemini Error:", e)

        # Fallback logic
        if glucose > 180:
            return "High glucose level detected. Possible diabetes risk."

        elif cholesterol > 240:
            return "High cholesterol level detected. Possible cardiovascular risk."

        elif haemoglobin < 12:
            return "Low haemoglobin level detected. Possible anemia risk."

        else:
            return "Blood test values appear within normal range."