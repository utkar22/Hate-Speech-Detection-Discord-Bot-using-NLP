import discord

import csv_handler
import check_score

client=discord.Client()

def get_from_file(file_name):
    '''
    This function will get data from the filename given
    The extension has to be provided with the file_name
    Parameters: a string that is the file name
    Returns: a string that contains the data
    '''
    f=open(file_name,"r")
    data = f.read()
    f.close()

    return (data)



def get_token():
    '''
    Store the discord bot token in token.txt
    This function will pull it out of the file
    The token is the password for the bot, so keep it safe.
    Parameters: None
    Returns: a string which is the token
    '''
    token = get_from_file("token.txt")

    return (token)



async def get_username(user_id):
    user = await fetch_user(user_id)
    return user.name

@client.event
async def on_ready():
    print ("Bot is running")

@client.event
async def on_message(message):

    if message.content == "p!score":
        user_score = csv_handler.get_score(message.author.id)
        if user_score == 0:
            string = "Your hate speech is 0 :) Do not become hateful :)"
        elif user_score<10:
            string = f"Your hate speech is {user_score} :)"
        elif user_score<50:
            string = f"Your hate speech is {user_score} :|"
        elif user_score<100:
            string = f"Your hate speech is {user_score} :("
        elif user_score<500:
            string = f"Your hate speech is {user_score}. You are a menace to society"
        else:
            string = f"Your hate speech is {user_score}. You need to be banned from discord"
        await message.channel.send(string)
    else:
        string = message.content

        score = check_score.get_score(string)

        if score>0:
            await message.channel.send("Hey! That message was offensive!")
            csv_handler.update_score(message.author.id, score)

    
        

@client.event
async def on_reaction(reaction, user):
    pass

token=get_token()
client.run(token)
