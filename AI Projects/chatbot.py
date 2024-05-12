import openai
openai.api_key = "sk-proj-txCCJcED5sknmETayYuLT3BlbkFJG59jP08K3OS5w3kuB1h3"

prompt = "Hello, my name is John and I am a software engineer."
model = "gpt-3.5-turbo"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

generated_text = response.choices[0].text
print(generated_text)