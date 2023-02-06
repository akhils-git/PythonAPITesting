import openai

# set the API key
openai.api_key = "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"

# Define the prompt
prompt = "What about titanic explain"

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
