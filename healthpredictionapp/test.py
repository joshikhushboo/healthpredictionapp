from google import genai

client = genai.Client(api_key="AQ.xxx")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello"
)

print(response.text)