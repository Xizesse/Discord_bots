import discord
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
import random
import os
import youtube_dl
import shutil
from random import randrange



#listas

jogos = ["League of Legends", "Counter-Strike: Global Offensive", "Hentai Hero", "Amoung Us", "Roblox",
         "Tony Hawk's Pro Skater 5", "Rocket League", "Dota 2", "Warframe", "CyberBonk 2069"]
queues = {}

TOKEN = "Nzg5ODI5MzMxNjgxMTQ4OTQw.X93v4g.Nttp0rRleM2GDGNvgS03e8I5GpM"

bot = commands.Bot(command_prefix="")
bot.remove_command('help')


# VARIÁVEIS DEFINIDADS

VOLUME = 10
#
# event
#



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(random.choice(jogos)), status=discord.Status.invisible)

    print("Juan in the house.")
    print(f'{round((bot.latency) * 1000)} ms')
    print(f'{bot.user} \n')
    # Por ordem : Gdp.geral, Bouas.geral, Bouas.private,
    queues.clear()

    song_there = os.path.isfile("song.mp3")

    if song_there:
        os.remove("song.mp3")


    canais = [bot.get_channel(566924461522026506), bot.get_channel(748176717490946061),
              bot.get_channel(748983244028117212),bot.get_channel(772282193363730477)]


@bot.event
async def on_member_join(member):
    print("Boas " f'{member}')


@bot.event
async def on_member_remove(member):
    print("Xau " f'{member}')


@bot.event
async def on_message(ctx):
    author = str(ctx.author)
    author = author[:-5]
    if ctx.author == bot.user:
        return
    if "boas" in ctx.content.lower() or "bouas" in ctx.content.lower():
        await ctx.channel.send(f'Bouas {author}')

    if "juan" in ctx.content.lower() or "juan" in ctx.content.lower():
        await ctx.channel.send(f'Diz {author} ?')

    if "esteban" in ctx.content.lower():
        await ctx.channel.send("Esteban é o rei")
    if "xau" in ctx.content.lower() or "adeus" in ctx.content.lower():
        await ctx.channel.send("Xau mpt")
    if "aha" in ctx.content.lower():
        await ctx.channel.send("Qual é a piada ?")
    if "obrigado" in ctx.content.lower() or "thanks" in ctx.content.lower() or "tnx" in ctx.content.lower() or "ty" in ctx.content.lower():
        await ctx.channel.send("De nada")
    if "abraço" in ctx.content.lower():
        await ctx.channel.send("Aquele abraço")


    if "meme" in ctx.content.lower():
        memes = os.path.abspath(os.path.realpath("memes"))
        quantosmemes = len(os.listdir(memes))
        memenum = randrange(quantosmemes)
        meme = os.listdir(memes)[memenum]
        await ctx.channel.send(file=discord.File(meme))




    await bot.process_commands(ctx)

#
# comands
#

@bot.command(aliases=["Ping", "PING"])
async def ping(ctx):
    await ctx.send(f'Tou com {round(bot.latency * 1000)} ms')


# depois do asterico tudo o que ta no ctx entra no parametro de question

@bot.command(aliases=["Achas", "ACHAS"])
async def achas(ctx, *, question):
    respostas = ["Nao sei bro",
                 "Talvez",
                 "hahaha sim",
                 "nop",
                 "ya, acho que sim",
                 "yha"]
    await ctx.send(f'"achas {question}"\n{random.choice(respostas)}')

# defino o amount e esse fica standart, mas ao definir um contaa como esse

@bot.command()
@commands.has_permissions(manage_messages=True)
async def apaga(ctx, amount=1):
    amount += 1
    await ctx.channel.purge(limit=amount)


@bot.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        title = "Ajuda",
        description = "Bouas,\n Yo soy Juan, dá tipo p por música e o crl\n Se quiseres mais info sobre os comandos escreve: \n help_comandos \n",
        colour = discord.Colour.orange(),
    )
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def help_comandos(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        title = "Ajuda",
        description = "Todos os comandos do JuanBot",
        colour = discord.Colour.orange(),
    )
    embed.add_field(name='Ping', value='Digo te o ping do meu client', inline=False)
    embed.add_field(name="Achas (questão)", value="Respondo-te a uma pergunta", inline=False)
    embed.add_field(name="Apaga (número de mensagens)", value="Apago as últimas mensagens (precisas de permissão)", inline=False)
    embed.add_field(name="Anda", value="Entro no teu voice chat", inline=False)
    embed.add_field(name="Sai", value="Saio do teu voice chat", inline=False)
    embed.add_field(name="Canta (nome da música)", value="Canto a música que pediste", inline=False)
    embed.add_field(name="Skip", value="Próxima Música", inline=False)
    embed.add_field(name="Stop", value="Para a música", inline=False)
    embed.add_field(name="Pausa", value="Põe a música em pausa", inline=False)
    embed.add_field(name="Resume", value="Dá resume na música", inline=False)
    embed.add_field(name="Volume (%)", value="Altera o volume da música (DISABLED PQ A MALTA SÓ PÕE EARRAPE)", inline=False)
    await ctx.send(embed=embed)

#
# Voice Commands
#


@bot.command(pass_context=True, aliases=["entra", "ENTRA", "Entra", "Anda", "ANDA"])
async def anda(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice is not None:
        return await voice.move_to(channel)
    await channel.connect()
    print(f'Entrei no {channel}\n')
    await ctx.send("ok")


@bot.command(pass_context=True, aliases=["baza", "BAZA", "Baza", "SAI", "Sai"])
async def sai(ctx):
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        print(f'Saí do voice chat : {channel}\n')
        await ctx.send("okok")
    else:
        print("Mandaram me sair do voice chat mas n estou em nenhum \n")
        await ctx.send("N estou em voice chat")



@bot.command(pass_context=True, aliases=['p', 'Play', "PLAY", "canta", "Canta", "CANTA", "puxa", "PUXA", "Puxa"])
async def play(ctx, *, url: str):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected:
        def check_queue():
            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is True:
                DIR = os.path.abspath(os.path.realpath("Queue"))
                length = len(os.listdir(DIR))
                still_q = length - 1
                try:
                    first_file = os.listdir(DIR)[0]
                except:
                    print("No more queued song(s)\n")
                    queues.clear()
                    return
                main_location = os.path.dirname(os.path.realpath(__file__))
                song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
                if length != 0:
                    print("Song done, playing next queued\n")
                    print(f"Songs still in queue: {still_q} \n")
                    song_there = os.path.isfile("song.mp3")

                    if song_there:
                        os.remove("song.mp3")

                    shutil.move(song_path, main_location)
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            os.rename(file, 'song.mp3')

                    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = VOLUME

                else:
                    queues.clear()
                    return

            else:
                queues.clear()
                print("Acabaram as músicas sem mais músicas na Q\n")

        song_there = os.path.isfile("song.mp3")
        try:
            if song_there is True:
                os.remove("song.mp3")
                print("Removido o ficheiro song \n")
        except PermissionError:
            print("Está a tocar uma música, por isso vou adicionar à queue")

            ###adicionar playqueue

            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is False:
                os.mkdir("Queue")
            DIR = os.path.abspath(os.path.realpath("Queue"))
            q_num = len(os.listdir(DIR))
            q_num += 1
            add_queue = True
            while add_queue:
                if q_num in queues:
                    q_num += 1
                else:
                    add_queue = False
                    queues[q_num] = q_num
            queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

            ydl_opts = {
                'format': "bestaudio/best",
                'quiet' : True,
                'outtmpl': queue_path,
                "postprocessors": [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Sacando o audio \n")
                ydl.download([f'ytsearch1:{url}'])
            await ctx.send("A adicionar " + str(q_num) + "ª música à queue")
            print("Song added to the queue \n")

            ##fim playqueue

            return
        Queue_infile = os.path.isdir("./Queue")
        try:
            Queue_folder = "./Queue"
            if Queue_infile is True:
                print("Removed old Queue Folder\n")
                shutil.rmtree(Queue_folder)
        except:
            print("No old Queue folder\n")

        await ctx.send("A tratar disso")

        voice = get(bot.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([f'ytsearch1:{url}'])
            await ctx.send(f'{url}')

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"Renamed File: {file}\n")
                os.rename(file, "song.mp3")

        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = VOLUME
        try:
            await ctx.send(f"A puxar: {name}")
            print("playing\n")
        except:
            await ctx.send("Música a tocar")
    else:
        channel = ctx.author.voice.channel
        await channel.connect()
        def check_queue():
            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is True:
                DIR = os.path.abspath(os.path.realpath("Queue"))
                length = len(os.listdir(DIR))
                still_q = length - 1
                try:
                    first_file = os.listdir(DIR)[0]
                except:
                    print("No more queued song(s)\n")
                    queues.clear()
                    return
                main_location = os.path.dirname(os.path.realpath(__file__))
                song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
                if length != 0:
                    print("Song done, playing next queued")
                    print(f"Songs still in queue: {still_q}\n")
                    song_there = os.path.isfile("song.mp3")

                    if song_there:
                        os.remove("song.mp3")

                    shutil.move(song_path, main_location)
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            os.rename(file, 'song.mp3')

                    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = VOLUME

                else:
                    queues.clear()
                    return

            else:
                queues.clear()
                print("No songs were queued before the ending of the last song\n\n")

        song_there = os.path.isfile("song.mp3")
        try:
            if song_there is True:
                os.remove("song.mp3")
                print("Removed old song file\n")
        except PermissionError:
            print("Está a tocar uma música, por isso vou adicionar à queue\n")

            ###adicionar playqueue

            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is False:
                os.mkdir("Queue")
            DIR = os.path.abspath(os.path.realpath("Queue"))
            q_num = len(os.listdir(DIR))
            q_num += 1
            add_queue = True
            while add_queue:
                if q_num in queues:
                    q_num += 1
                else:
                    add_queue = False
                    queues[q_num] = q_num
            queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

            ydl_opts = {
                'format': "bestaudio/best",
                'quiet' : True,
                'outtmpl': queue_path,
                "postprocessors": [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Sacando o audio \n")
                ydl.download([f'ytsearch1:{url}'])
            await ctx.send("A adicionar " + str(q_num) + "ª música à queue")
            print("Song added to the queue \n")

            ##fim playqueue

            return
        Queue_infile = os.path.isdir("./Queue")
        try:
            Queue_folder = "./Queue"
            if Queue_infile is True:
                print("Removed old Queue Folder")
                shutil.rmtree(Queue_folder)
        except:
            print("No old Queue folder\n")

        await ctx.send("A tratar disso")

        voice = get(bot.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([f'ytsearch1:{url}'])
            await ctx.send(f'{url}')

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"Renamed File: {file}\n")
                os.rename(file, "song.mp3")

        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = VOLUME
        try:

            await ctx.send(f"A puxar: {name}")
            print("playing\n")
        except:
            await ctx.send("Música a tocar")


@bot.command(pass_context=True, aliases=["pausa", "PAUSA", "Pausa"])
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Música em pausa")
        voice.pause()
        await ctx.send("Música em pausa")
    else:
        print("Não está a tocar música\n")
        await ctx.send("Não está a tocar música bro")


@bot.command(pass_context=True)
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Music resumed")
        voice.resume()
        await ctx.send("A puxar de novo")
    else:
        print("Erro Resume : No music playing\n")
        await ctx.send("Comando inválido bro: Não está a tocar música")


@bot.command(pass_context=True)
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    queues.clear()
    queue_infile = os.path.isdir("./Queue")
    if queue_infile is True:
        shutil.rmtree("./Queue")

    if voice and voice.is_playing():
        print("Music Stoped")
        voice.stop()
        await ctx.send("Música parada")
    else:
        print("Erro Stop : No music playing\n")
        await ctx.send("Comando inválido bro: Não está a tocar música")


@bot.command(pass_context=True, aliases=["skip", "Skip", "SKIP", "Next", "NEXT"])
async def next(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Próxima música \n")
        voice.stop()
        await ctx.send("Próxima música ")
    else:
        print("Erro Skip : No music playing\n")
        await ctx.send("Comando inválido bro: Não está a tocar música")


@bot.command(pass_context=True)
async def volume(ctx, volume : int):
    if False:
        if ctx.voice_client is None:
            return await ctx.send("Não estou num voice channel")
        print("Volume definido:" + str(volume/100))
        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f'A cantar com {volume}% do meu poder')

bot.run(TOKEN)


