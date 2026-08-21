from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.responses.create(
    model="gpt-5.6",
    input="Write a short sentence about artificial intelligence."
)

print(response.output_text)
