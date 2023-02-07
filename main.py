# Import necessary libraries
import openai
import os

# Read API key from file
with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

# Authenticate with OpenAI API
openai.api_key = api_key

# Generate a quote using OpenAI
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt='What is a good quote about developer?',
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
quote = response['choices'][0]['text']

# Read the existing file into memory
with open("README.md", "r") as f:
    lines = f.readlines()

# Find the line to update
for i, line in enumerate(lines):
    if line.startswith("###### Today's Quote from GPT3:"):
        lines[i+1] = "> " + quote + "\n"
        break

# Write the updated file to disk
with open("README.md", "w") as f:
    f.writelines(lines)

# Commit and push the file to GitHub
os.system("git add README.md")
os.system("git commit -m 'Automated update of README.md'")
os.system("git push origin main")
