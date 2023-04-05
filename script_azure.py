import openai

with open('token.txt') as f:
    # converting out text file to a list of lines
    lines = f.read().split('\n')
    # openai api key
    openai.api_key = lines[0]
    # discord token
    discord_token = lines[1]
#close the file
f.close()


response = openai.Image.create(
    prompt = 'A beautiful London Spring day.',
    n = 1,
    size = '1024x1024'
)

image_url = response['data'][0]['url']
print(image_url)
