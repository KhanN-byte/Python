import openai
openai.api_key = "your-own-api-key-here"

prompt = "Hello, my name is John and I am a software engineer."
model = "gpt-3.5-turbo"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

generated_text = response.choices[0].text
print(generated_text)
