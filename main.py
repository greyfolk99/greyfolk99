import openai
import os

# Get the absolute path of the current file
current_file = os.path.abspath(__file__)
# Get the directory containing the current file
current_dir = os.path.dirname(current_file)
# Get the absolute path of the secrets file
secrets_file = os.path.join(current_dir, "secrets.txt")
# Get the absolute path of the readme file
readme_file = os.path.join(current_dir, "README.md")


# Get a quote from GPT3
def update_quote():
    # Read the existing file into memory
    with open(readme_file, "rt", encoding='UTF8') as f:
        lines = f.readlines()

    # Find the line to update
    i = 0
    line_to_update = None
    for i, line in enumerate(lines):
        if line.startswith("###### Today's Quote from GPT3:"):
            i += 1
            line_to_update = lines[i]
            print("before: " + line_to_update)
            break

    # Read the API key from the secrets file
    with open(secrets_file, "rt", encoding='UTF8') as f:
        api_key = f.readline().strip()

    # Authenticate to the OpenAI API
    openai.api_key = api_key

    # Get the quote from GPT3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Please generate a motivational quote in one line, except " + line_to_update,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response["choices"][0]["text"]

    lines[i] = "> " + message.strip().replace("\n", " ") + "\n"

    # Write the updated file to disk
    with open(readme_file, "w", encoding='UTF8') as f:
        f.writelines(lines)

    return message


# Commit and push the file to GitHub
quote = update_quote()
print("after: " + quote)
