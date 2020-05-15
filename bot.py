import discord
from discord.ext import commands
import random











#----------------------------------------------------------------------------------------------------
#===================BUROKKU TOCHI SETTINGS===================
#----------------------------------------------------------------------------------------------------










#--------------------------------------------------------------------------------
#============ BOT PREFIX SETTINGS ============
#--------------------------------------------------------------------------------


client = commands.Bot(command_prefix = "b!")
client.remove_command("help")


#--------------------------------------------------------------------------------






#--------------------------------------------------------------------------------
#============ BOT ON READY EVENT ============
#--------------------------------------------------------------------------------


@client.event
async def on_ready():
    print("Bot is ready!")



#@client.event
#async def on_message(message: discord.Message) -> None:
    #if 'Anime' in message.content:
        #await message.channel.send("Is life")









#----------------------------------------------------------------------------------------------------
#================= BUROKKU TOCHI FUN COMMANDS =================
#----------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------
#============ MY TRUE NAME COMMAND ============
#--------------------------------------------------------------------------------


@client.command()
async def my_true_name(ctx, fruit = None, animal = None, birth_stone = None):
    user = ctx.author.mention
    if fruit != None and animal != None and birth_stone != None:
        fruit_list = list(fruit)
        animal_list = list(animal)
        birth_stone_list = list(birth_stone)
        if len(fruit) < 3 or len(animal) < 3 or len(birth_stone) < 3:
            await ctx.send(f'{user}, all inputs must be 3 letters or more!')
        else:
            fruit_letter1 = random.choice(fruit_list)
            fruit_letter2 = random.choice(fruit_list)
            while fruit_letter2 == fruit_letter1:
                fruit_letter2 = random.choice(fruit_list)
            animal_letter1 = random.choice(animal_list)
            animal_letter2 = random.choice(animal_list)
            while animal_letter1 == fruit_letter1 or animal_letter1 == fruit_letter2:
                animal_letter1 = random.choice(animal_list)
            while animal_letter2 == fruit_letter1 or animal_letter2 == fruit_letter2 or animal_letter2 == animal_letter1:
                animal_letter2 = random.choice(animal_list)
            birth_stone_letter1 = random.choice(birth_stone_list)
            birth_stone_letter2 = random.choice(birth_stone_list)
            while birth_stone_letter1 == animal_letter1 or birth_stone_letter1 == animal_letter2:
                birth_stone_letter1 = random.choice(birth_stone_list)
            while birth_stone_letter2 == birth_stone_letter1:
                birth_stone_letter2 = random.choice(birth_stone_list)
            true_name = str(fruit_letter1) + str(fruit_letter2) + str(animal_letter1) + str(animal_letter2) + str(birth_stone_letter1) + str(birth_stone_letter2)
            await ctx.send(f'{user}, your true name is {true_name}!')
    else:
        embed = discord.Embed(title="My True Name",description=f'Do b!my_true_name <Fruit> <Animal> <Birth Stone>\nand you will be given your true name!',colour=discord.Colour.green())
        await ctx.send(embed=embed)




#--------------------------------------------------------------------------------
#============ LOVE CALCULATION COMMAND============
#--------------------------------------------------------------------------------


@client.command()
async def lovecalc(ctx, member1 : discord.Member = None, member2 : discord.Member = None):
    user = ctx.author
    calculation = random.randint(1,100)
    selected_user1 = member1.mention
    selected_user2 = member2.mention
    if member1 == None and member2 == None:
        embed1 = discord.Embed(title="Love Calculation",description=f'Do b!lovecalc <member> <member> to see their compatability!',colour=discord.Colour.red())
        await ctx.send(embed=embed1)
    elif member1 == None and member2 != None or member1 != None and member2 == None:
        await ctx.send(f'{user}, you must specify two members!')
    elif member1.mention and member2.mention == user.mention:
        embed2 = discord.Embed(title="Love Calculation",description=f'{user.mention} and {user.mention} are 0% compatible!\n\n:neutral_face: This is awkward :neutral_face:',colour=discord.Colour.red())
        await ctx.send(embed=embed2)
    elif member1.mention == member2.mention:
        embed2 = discord.Embed(title="Love Calculation",description=f'{user.mention} and {user.mention} are 0% compatible!\n\n:neutral_face: This is awkward :neutral_face:',colour=discord.Colour.red())
        await ctx.send(embed=embed2)
    else:
        if calculation >= 0 and calculation <= 10:
            embed3 = discord.Embed(title="Love Calculation",description=f'{member1.mention} and {member2.mention} are {calculation}% compatible!\n\n:face_vomiting: This is not a good match :face_vomiting:',colour=discord.Colour.red())
            await ctx.send(embed=embed3)
        elif calculation >= 10 and calculation <= 15:
            embed4 = discord.Embed(title="Love Calculation",description=f'{member1.mention} and {member2.mention} are {calculation}% compatible!\n\n:joy: Haha, are you kidding? :joy:',colour=discord.Colour.red())
            await ctx.send(embed=embed4)
        elif calculation >= 15 and calculation <= 25:
            embed5 = discord.Embed(title="Love Calculation",description=f'{member1.mention} and {member2.mention} are {calculation}% compatible!\n\n:grimacing: This could work but you are not anyones first choice, oof :grimacing:',colour=discord.Colour.red())
            await ctx.send(embed=embed5)
        elif calculation >= 25 and calculation <= 35:
            embed6 = discord.Embed(title="Love Calculation",description=f'{member1.mention} and {member2.mention} are {calculation}% compatible!\n\n:slight_smile: It is a nice though, consider it carefully.. :slight_smile:',colour=discord.Colour.red())
            await ctx.send(embed=embed6)
        elif calculation >= 35 and calculation <= 40:
            embed7 = discord.Embed(title="Love Calculation",description=f'{member1.mention} and {member2.mention} are {calculation}% compatible!\n\n:smile: This might be something good for the both of you! :smile:',colour=discord.Colour.red())
            await ctx.send(embed=embed7)
        elif calculation >= 40 and calculation <= 50:
            embed8 = discord.Embed(title="Love Calculation",description=f'{member1.mention} and {member2.mention} are {calculation}% compatible!\n\n:wink: This is probably not the first time you thought about this! :wink:',colour=discord.Colour.red())
            await ctx.send(embed=embed8)
        elif calculation >= 50 and calculation <= 60:
            embed9 = discord.Embed(title="Love Calculation",description=f'{member1.mention} and {member2.mention} are {calculation}% compatible!\n\n:smirk: What are you waiting for? This might be it! :smirk:',colour=discord.Colour.red())
            await ctx.send(embed=embed9)
        elif calculation >= 60 and calculation <= 70:
            embed10 = discord.Embed(title="Love Calculation",description=f'{member1.mention} and {member2.mention} are {calculation}% compatible!\n\n:flushed: Woah! Is this an error or reality?? Awesome match! :flushed:',colour=discord.Colour.red())
            await ctx.send(embed=embed10)
        elif calculation >= 70 and calculation <= 85:
            embed11 = discord.Embed(title="Love Calculation",description=f'{member1.mention} and {member2.mention} are {calculation}% compatible!\n\n:star_struck: A match made from heaven, take it and fly to the stars! :star_struck:',colour=discord.Colour.red())
            await ctx.send(embed=embed11)
        elif calculation >= 85 and calculation <= 90:
            embed12 = discord.Embed(title="Love Calculation",description=f'{member1.mention} and {member2.mention} are {calculation}% compatible!\n\n:smiling_face_with_3_hearts: Love is in the air! :smiling_face_with_3_hearts:',colour=discord.Colour.red())
            await ctx.send(embed=embed12)
        elif calculation >= 90 and calculation <= 100:
            embed13 = discord.Embed(title="Love Calculation",description=f'{member1.mention} and {member2.mention} are {calculation}% compatible!\n\n:heart_eyes: No words can describe the feelings between this partnership! :heart_eyes:',colour=discord.Colour.red())
            await ctx.send(embed=embed13)



#==================BUROKKU TOCHI RUN TOKEN=======================

client.run("")

#==========================================================
