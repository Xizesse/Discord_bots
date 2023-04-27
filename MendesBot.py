import discord
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
import random
import os
import youtube_dl
import shutil

#listas

jogos = ["League of Legends", "Counter-Strike: Global Offensive", "Hentai Hero", "Amoung Us", "Roblox",
         "Tony Hawk's Pro Skater 5", "Rocket League", "Dota 2", "Warframe"]


TOKEN = 

bot = commands.Bot(command_prefix="")


#
# event
#



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(random.choice(jogos)), status=discord.Status.idle)
    print("MendesBot in the house.")
    print(f'{round((bot.latency) * 1000)} ms')
    print(f'{bot.user} \n')
    # Por ordem : Gdp.geral, Bouas.geral, Bouas.private,
    canais = [bot.get_channel(566924461522026506), bot.get_channel(748176717490946061),
              bot.get_channel(748983244028117212)]
    for canal in canais:
        if False:
            await canal.send("Bouas")


@bot.event
async def on_member_join(member):
    print("Bouas " f'{member}')


@bot.event
async def on_member_remove(member):
    print("Xau " f'{member}')


@bot.event
async def on_message(ctx):
    author = str(ctx.author)
    author = author[:-5]
    if ctx.author == bot.user:
        return
    if "pum" in ctx.content.lower() or "PUM" in ctx.content.lower():
        await ctx.channel.send(f'AH fodasse, levei um tiro do {author}, agora morri')
    if "boas" in ctx.content.lower() or "bouas" in ctx.content.lower():
        await ctx.channel.send(f'Bouas {author}')

    if "mendes" in ctx.content.lower() or "mendocas" in ctx.content.lower():
        await ctx.channel.send(f'Diz {author} ?')

    if "topau" in ctx.content.lower():
        await ctx.channel.send("Esse topau n passa do primeiro período!")
    if "xau" in ctx.content.lower() or "adeus" in ctx.content.lower():
        await ctx.channel.send("Onde vais ?")
    if "almoça" in ctx.content.lower():
        await ctx.channel.send("onde vais almoçar ?")
    if "haha" in ctx.content.lower():
        await ctx.channel.send("Qual é a piada ?")
    if "obrigado" in ctx.content.lower() or "thanks" in ctx.content.lower() or "tnx" in ctx.content.lower():
        await ctx.channel.send("De nada")
    if "abraço" in ctx.content.lower():
        await ctx.channel.send("Abraço mpt")

    await bot.process_commands(ctx)



#
# comands
#


@bot.command(aliases=["Ping", "PING"])
async def ping(ctx):
    await ctx.send(f'Bouas, o meu ping é {round(bot.latency * 1000)} ms')


# depois do asterico tudo o que ta no ctx entra no parametro de question
@bot.command(aliases=["Achas", "ACHAS"])
async def achas(ctx, *, question):
    respostas = ["Ns bro",
                 "Talvez",
                 "hahaha sim",
                 "nop",
                 "ya, acho que sim",
                 "ya mpt"]
    await ctx.send(f'"achas {question}"\n{random.choice(respostas)}')


# defino o amount e esse fica standart, mas ao definir um cotna como esse

@bot.command()
@commands.has_permissions(manage_messages=True)
async def apaga(ctx, amount=1):
    amount += 1
    await ctx.channel.purge(limit=amount)

#
#
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
                print(f"Songs still in queue: {still_q}")

                song_there = os.path.isfile("song.mp3")

                if song_there:
                    os.remove("song.mp3")

                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')

                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                queues.clear()
                return

        else:
            queues.clear()
            print("No songs were queued before the ending of the last song\n")

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there is True:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")


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
        print("No old Queue folder")

    await ctx.send("A tratar disso")

    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
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
    voice.source.volume = 0.07
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


queues = {}


@bot.command(pass_context=True, aliases=["Queue", "QUEUE"])
async def queue(ctx, *, url: str):
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

bot.run(TOKEN)



