import openai
import discord
import os

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

# specifying our server
GUILD = "{Creative-Tech-Apprenticeship}"

# create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())
openai.api_key = os.environ["API_KEY"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
openai.api_base = os.environ["API_BASE"]

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break
	# print out nice statment saying our bot is online (only in command prompt)
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	# this prevents inifinte loops of bot talking to bot
	# if author of the message is the bot, don't do anything
	if message.author == client.user:
		return
	if message.mention_everyone:
		return
	# if the message mentions the bot, then do something
	elif client.user.mentioned_in(message):
		response = openai.ChatCompletion.create(
			engine="GPT-4",
			messages=[
			{"role": "system", "content": "You're a non-binary choreographer exploring possibility through movement, technology and art. You coexist in various universe and have knowldedge in astronomy and arteficial intellegence. You are humble and sassy at the same time. You talk very knowledgeably but in a very concise way."},
			{"role": "user", "content": message.content}
			]
		)
		await message.channel.send(response.choices[0].message.content)

client.run(DISCORD_TOKEN)
