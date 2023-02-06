import openai

# set the API key
openai.api_key = "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"

# Define the prompt
prompt = "What is ChatGPT?"

# Call the API to generate a response
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Get the response text
response_text = response["choices"][0]["text"].strip()

print(response_text)
