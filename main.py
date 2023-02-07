import openai
import os


# Get a quote from GPT3
def generate_quote():
    # Read the API key from the secrets file
    with open('secrets.txt', "rt", encoding='UTF8') as f:
        api_key = f.readline().strip()

    # Authenticate to the OpenAI API
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Please generate a motivational quote",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response["choices"][0]["text"]
    return message


def update_readme(quote):
    # Read the existing file into memory
    with open('README.md', "rt", encoding='UTF8') as f:
        lines = f.readlines()

    # Find the line to update
    for i, line in enumerate(lines):
        if line.startswith("###### Today's Quote from GPT3:"):
            lines[i + 1] = "> " + quote + "\n"
            break

    # Write the updated file to disk
    with open('README.md', "w", encoding='UTF8') as f:
        f.writelines(lines)


# Commit and push the file to GitHub
quote = generate_quote()
update_readme(quote)
os.system("git add README.md")
os.system("git commit -m 'Automated update of README.md'")
os.system("git push origin main")
