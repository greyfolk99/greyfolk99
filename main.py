import openai
import os
import platform
# Updated


# Get the absolute path of the current file
current_file = os.path.abspath(__file__)


# Get the directory containing the current file
current_dir = os.path.dirname(current_file)


# Get the absolute path of the secrets file
secrets_file = os.path.join(current_dir, "secrets.txt")


# Get a quote from GPT3
def generate_quote():
    # Read the API key from the secrets file
    with open(secrets_file, "rt", encoding='UTF8') as f:
        api_key = f.readline().strip()

    # Authenticate to the OpenAI API
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Please generate a motivational quote in one line: ",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response["choices"][0]["text"]
    return message


# Get the absolute path of the readme file
readme_file = os.path.join(current_dir, "README.md")


def update_readme(quote):
    # Read the existing file into memory
    with open(readme_file, "rt", encoding='UTF8') as f:
        lines = f.readlines()

    # Find the line to update
    for i, line in enumerate(lines):
        if line.startswith("###### Today's Quote from GPT3:"):
            lines[i + 1] = "> " + quote.strip().replace("\n", " ") + "\n"
            break

    # Write the updated file to disk
    with open(readme_file, "w", encoding='UTF8') as f:
        f.writelines(lines)


# Commit and push the file to GitHub
quote = generate_quote()
update_readme(quote)
