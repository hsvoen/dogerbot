import os
import discord
import asyncio
import re
import random
import thought
import time

client = discord.Client()

Thoughts = thought.ThoughtForTheDay()
time_last_thought = time.struct_time

murder_response = ["I too can appreciate a good killing", "Why stopp there? I think we can go further." , "Just do it." , "Did someone mention murder? Count me in!", "I'm gonna call the police!", "That's a whipping!", "Why am I never included when you do fun stuff?"]

DOGER_TOKEN =os.environ.get('DOGER_BOT_TOKEN')

def post_thought():
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    kill = re.search("murder|kill|killing|genocide|execute|assassinate|eliminate|dispatch|wreck|destroy|ruin|drep|drap|mord",message.content.lower())

    if(message.author.name =="doger_bot"):
        return

    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif (message.content.find("dodger") >=0):
        await client.send_message(message.channel, 'Dodger Dodger best i test')
    elif find_magnus(message): 
        for server in client.servers:
            for emoji in server.emojis:
                if (emoji.name == "magnus"):
                    await client.add_reaction(message,emoji)
    elif message.content.startswith('!dogerhelp'):
        await client.send_message(message.channel, 'Doger will respond to: !test, !sleep and any mention of space or murder')
    elif kill:
        await client.send_message(message.channel, random.choice(murder_response))
    elif message.content.startswith('!thought'):
        await client.send_message(message.channel, 'Thought for the day: ' + Thoughts.getThought())


def find_magnus(message):
    ''' Search a message for any trace of magnusyness. 
        Returns true if the message is confirmed of having been sent by magnus, false otherwise
    '''
    if re.search("sp.+?ce|elon musk|rocket|tesla|new space conspiracy|artificial intelligence|coffe|complexity|hard sci-fi|anti-authoritarian|anarchist|nanofabricator|mars|minion|puppet|democracy.+?failed|moonbase|hex based|capitalism.+?doesn't work|capitalism.+?failed|capitalist|cynicism|hero system|complex|",message.content.lower()): #Reacts to space
        return True
    else
        return False


if __name__ == '__main__':
    client.run(DOGER_TOKEN)

