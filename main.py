import discord
import asyncio
import os
import time
import random
import aiohttp
import requests
import safygiphy
import io

g = safygiphy.Giphy()
client = discord.Client()
version = "0.1"

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto
    token = secreto.token

def toint(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

@client.event
async def on_ready():
    print("=================================")
    print("Bot iniciado com sucesso!")
    print (client.user.name)
    print(f"Bot Version: {version}")
    print("=================================")
    await client.change_presence(game=discord.Game(name='RankUP e Gravando! | !comandos'), status=discord.Status.dnd)

@client.event
async def on_message(message):
##DOAÇÃO
    #avisofa
    if message.content.startswith('/doar FA'):
        role = discord.utils.get(message.server.roles, name='🕵️‍♂️ Doador')
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Você precisa ter o cargo `Doador` para executar este comando!")
        await client.delete_message(message)
        try:
            user = message.author

            embed = discord.Embed(
                title=" 📢 AVISO",
                description="Será feito uma doação de contas de **Minecraft Full Acesso Unmigrated**, dentro de 1 minuto!",
                color=0x0d488a
            )
            embed.set_footer(
                text="Enviado pelo doador: " + user.name,
                icon_url=user.avatar_url
            )

            await client.send_message(discord.Object(id='458719859312820264'), "@everyone")
            await client.send_message(discord.Object(id='458719859312820264'), embed=embed)
        finally:
            pass
    #avisoalt
    if message.content.startswith('/doar ALT'):
        role = discord.utils.get(message.server.roles, name='🕵️‍♂️ Doador')
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Você precisa ter o cargo `Doador` para executar este comando!")
        await client.delete_message(message)
        try:
            user = message.author

            embed = discord.Embed(
                title=" 📢 AVISO",
                description="Será feito uma doação de contas de **Minecraft ALTS**, dentro de 1 minuto!",
                color=0x0d488a
            )
            embed.set_footer(
                text="Enviado pelo doador: " + user.name,
                icon_url=user.avatar_url
            )

            await client.send_message(discord.Object(id='4587198593128202641'), "@everyone")
            await client.send_message(discord.Object(id='458719859312820264'), embed=embed)
        finally:
            pass
    #avisocapa
    if message.content.startswith('/doar CAPA'):
        role = discord.utils.get(message.server.roles, name='🕵️‍♂️ Doador')
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Você precisa ter o cargo `Doador` para executar este comando!")
        await client.delete_message(message)
        try:
            user = message.author

            embed = discord.Embed(
                title=" 📢 AVISO",
                description="Será feito uma doação de contas de **Minecraft ALTS**, dentro de 1 minuto!",
                color=0x0d488a
            )
            embed.set_footer(
                text="Enviado pelo doador: " + user.name,
                icon_url=user.avatar_url
            )
            await client.send_message(discord.Object(id='458719859312820264'), "@everyone")
            await client.send_message(discord.Object(id='458719859312820264'), embed=embed)
        finally:
            pass
    #avisosemi
    if message.content.startswith('/doar SEMI'):
        role = discord.utils.get(message.server.roles, name='🕵️‍♂️ Doador')
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Você precisa ter o cargo `Doador` para executar este comando!")
        await client.delete_message(message)
        try:
            user = message.author

            embed = discord.Embed(
                title=" 📢 AVISO",
                description="Será feito uma doação de contas de **Minecraft Semi-Full**, dentro de 1 minuto!",
                color=0x0d488a
            )
            embed.set_footer(
                text="Enviado pelo doador: " + user.name,
                icon_url=user.avatar_url
            )
            await client.send_message(discord.Object(id='458719859312820264'), "@everyone")
            await client.send_message(discord.Object(id='458719859312820264'), embed=embed)
        finally:
            pass
    #doar
    if message.content.startswith('/doar'):
        role = discord.utils.get(message.server.roles, name='🕵️‍♂️ Doador')
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Você precisa ter o cargo `Doador` para executar este comando!")
        await client.delete_message(message)
        try:
            user = message.author
            msg = message.content[6:]

            embed = discord.Embed(
                title="⚠ Doação!",
                description="{}".format(msg),
                color=0x003aff
            )
            embed.set_footer(
                text="Enviada pelo doador: " + user.name,
                icon_url=user.avatar_url
            )

            await client.send_message(discord.Object(id='458719859312820264'), "@everyone")
            await client.send_message(discord.Object(id='458719859312820264'), embed=embed)
        finally:
            pass

##DEFAULT_COMMANDS
    #comandos
    if message.content.lower().startswith('!comandos'):
        embed = discord.Embed(
            title="Comandos do bot:",
            color=0x0d488a,
            description="!serverinfo » Veja as informações do servidor\n"
                        "!user <usuário> » Veja as informações de um usuário\n"
                        "!dado » Role um dado de um número de 1 á 6\n"
                        "!moeda » Brinque de cara ou coroa\n"
                        "!avatar <usuário> » Veja o avatar seu ou de um membro\n"
                        "!convite » Gere um convite e use o mesmo para convidar todos para nossa comunidade\n"
                        "!ping » Veja o tempo de resposta do bot\n"
                        "!staff » Veja os comandos para o cargo `👤 Staff (apenas para quem tem o cargo).\n"
                        "!admin » Veja os comandos para a permissão `administrador` (apenas para quem tem a permissão).\n"
                        "!gif <título> » Gere um gif.\n"
                        "!cat » Gere uma foto ou um vídeo/gif de um gato.\n"
                        "!dog » Gere uma foto ou um vídeo/gif de um cão.\n\n"
                        "**Desenvolvido pelo Bruno. Mais informações aqui:** [Clique](https://twitter.com/brunoqq_)"
        )
        embed.set_author(
            name="Swift Bot",
            icon_url=client.user.avatar_url
        )
        embed.set_footer(
            text="Copyright © 2018 @brunoqq_",
            icon_url="https://cdn.discordapp.com/emojis/412576344120229888.png?v=1"
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/423159064533532672/424213167317712946/dsg.png"
        )

        await client.send_message(message.channel, "Olá {}, foi enviado a lista de comandos no seu privado!".format(
            message.author.mention))
        await client.send_message(message.author, embed=embed)

    #GERA UM GIF/VÍDEO ALEATÓRIO DE GATO
    if message.content.lower().startswith('!cat'):
     async with aiohttp.get('http://aws.random.cat/meow') as r:
         if r.status == 200:
             js = await r.json()
             canal = message.channel
             await client.delete_message(message)
             await client.send_message(canal, js['file'])
    #CAO
    if message.content.lower().startswith('!dog'):
     async with aiohttp.get('https://random.dog/woof.json') as r:
         if r.status == 200:
             js = await r.json()
             canal = message.channel
             await client.delete_message(message)
             await client.send_message(canal, js['url'])
#GERA UM GIF
    if message.content.startswith('!gif'):
        gif_tag = message.content[5:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

#GERA UM GIF DIVERTIDO
    if message.content.startswith('!fun'):
        gif_tag = "fun"
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')
    #avatar
    elif message.content.lower().startswith('!avatar'):
        try:
            membro = message.mentions[0]
            avatarembed = discord.Embed(
                title="",
                color=0x0d488a,
                description="**[Clique aqui](" + membro.avatar_url + ") para acessar o link do avatar!**"
            )
            avatarembed.set_author(name=membro.name)
            avatarembed.set_image(url=membro.avatar_url)
            await client.send_message(message.channel, embed=avatarembed)
        except:
            avatarembed2 = discord.Embed(
                title="",
                color=0x0d488a,
                description="**[Clique aqui](" + message.author.avatar_url + ") para acessar o link do avatar!**"
            )
            avatarembed2.set_author(name=message.author.name)
            avatarembed2.set_image(url=message.author.avatar_url)
            await client.send_message(message.channel, embed=avatarembed2)
    #ping
    if message.content.lower().startswith('!ping'):
        timep = time.time()
        emb = discord.Embed(title='Aguarde', color=0x0d488a)
        pingm0 = await client.send_message(message.channel, embed=emb)
        ping = time.time() - timep
        pingm1 = discord.Embed(title='Pong!', description=':ping_pong: Ping - %.01f segundos' % ping, color=0x0d488a)
        await client.edit_message(pingm0, embed=pingm1)
    #dado
    if message.content.lower().startswith('!dado'):
        choice = random.randint(1, 6)
        embeddad = discord.Embed(title='Dado', description='🎲 Joguei o dado, o resultado é :  {}'.format(choice),colour=0x0d488a)
        await client.send_message(message.channel, embed=embeddad)
    #serverinfo
    if message.content.lower().startswith('!serverinfo'):
        server = message.server
        embedserver = discord.Embed(
            title='Informaçoes do Servidor',
            color=0x0d488a,
            descripition='Essas são as informaçoes\n')
        embedserver = discord.Embed(name="{} Server ".format(message.server.name), color=0x0d488a)
        embedserver.add_field(name="Nome", value=message.server.name, inline=True)
        embedserver.add_field(name="Dono", value=message.server.owner.mention)
        embedserver.add_field(name="ID", value=message.server.id, inline=True)
        embedserver.add_field(name="Cargos", value=len(message.server.roles), inline=True)
        embedserver.add_field(name="Membros", value=len(message.server.members), inline=True)
        embedserver.add_field(name="Criado em", value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        embedserver.add_field(name="Emojis", value=f"{len(message.server.emojis)}/100")
        embedserver.add_field(name="Região", value=str(message.server.region).title())
        embedserver.set_thumbnail(url=message.server.icon_url)
        embedserver.set_footer(text="By: @brunoqq_")
        await client.send_message(message.channel, embed=embedserver)
    #user
    if message.content.startswith('!user'):
        try:
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]

            userembed = discord.Embed(
                title="Nome",
                description=user.name,
                color=0x0d488a
            )
            userembed.set_author(
                name="Informações do usuário"
            )
            userembed.set_thumbnail(url=user.avatar_url)
            userembed.add_field(
                name="Entrou no servidor em",
                value=userjoinedat
            )
            userembed.add_field(
                name="Criou seu Discord em",
                value=usercreatedat
            )
            userembed.add_field(
                name="TAG",
                value=user.discriminator
            )
            userembed.add_field(
                name="ID",
                value=user.id
            )

            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, "Usuário não encontrado!")
        except:
            await client.send_message(message.channel, "Erro, desculpe. ")
        finally:
            pass
    #moeda
    if message.content.lower().startswith('!moeda'):
        choice = random.randint(1, 2)
        if choice == 1:
         await client.add_reaction(message, '🌝')
        if choice == 2:
         await client.add_reaction(message, '👑')
    #convite
    if message.content.lower().startswith('!convite'):
     invite = await client.create_invite(message.channel, max_uses=1, xkcd=True)
     await client.send_message(message.author, "Seu convite para o discord do BielSwift é: discord.gg/bielswift")
     await client.send_message(message.channel, "Olá {}, um convite foi enviado no seu privado!".format(message.author.mention))

##admin
    #admin
    if message.content.lower().startswith('!admin'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, "Você precisa ter a permissão `administrador` para executar este comando!")
        embed = discord.Embed(
            title="Comandos para o cargo `🌕 STAFF+` :",
            color=0x0d488a,
            description="!ban <usuário> » Banimento permanentemente do discord.\n"
                        "!kick <usuário> » Expulsão do discord.\n"
                        "!mute <usuário> » Mute permanentemente do discord\n"
                        "!unmute <usuário> » Unmute do discord\n"
                        "!faq » Comando para ver as informaçoes básicas do servidor\n"
                        "!say » Bot repete a mensagem\n"
                        "!aviso » Avisa em EMBED\n"
                        "!votar » Inicia uma votação com like e deslike\n"
                        "!apagar <1 à 100> » Apague de 1 à 100 mensagens\n"
                        "\n"
                        "**STATUS:**"
                        "\n"
                        "!jogando <frase> » Altere o status de jogando\n"
                        "!transmitindo <frase> » Altere o status de transmitindo\n"
                        "!ouvindo <frase> » Altere o status de ouvindo\n"
                        "!assistindo <frase> » Altere o status de assistindo\n"
                        "\n"
                        "**Desenvolvido pelo Bruno. Mais informações aqui:** [Clique](https://discord.gg/TuDXw)"
        )
        embed.set_author(
            name="Swift Discord",
            icon_url=client.user.avatar_url
        )
        embed.set_footer(
            text="Copyright © 2018 @brunoqq_",
            icon_url="https://cdn.discordapp.com/emojis/412576344120229888.png?v=1"
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/423159064533532672/424213167317712946/dsg.png"
        )

        await client.send_message(message.channel, "Olá {}, foi enviado todos os comandos para a permissão `administrador` no seu privado!".format(message.author.mention))
        await client.send_message(message.author, embed=embed)
    #jogando
    if message.content.startswith('!jogando'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, "Você precisa ter a permissão `administrador` para executar este comando!")
        game = message.content[9:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Status `jogando` alterado para: " + game + " ")
    #transmitindo
    if message.content.startswith('!transmitindo'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, "Você precisa ter a permissão `administrador` para executar este comando!")
        game = message.content[14:]
        await client.change_presence(game=discord.Game(name=game, type=1, url='https://www.twitch.tv/TheDiretor'),status='streaming')
        await client.send_message(message.channel, "Status `transmitindo` alterado para: " + game + " ")
    #ouvindo
    if message.content.startswith('!ouvindo'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, "Você precisa ter a permissão `administrador` para executar este comando!")
        game = message.content[10:]
        await client.change_presence(game=discord.Game(name=game, type=2))
        await client.send_message(message.channel, "Status `ouvindo` alterado para: " + game + " ")
    #assistindo
    if message.content.startswith('!assistindo'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, "Você precisa ter a permissão `administrador` para executar este comando!")
        game = message.content[12:]
        await client.change_presence(game=discord.Game(name=game, type=3))
        await client.send_message(message.channel, "Status `assistindo` alterado para: " + game + " ")
    #say
    if message.content.lower().startswith("!say"):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, "Você precisa ter a permissão `administrador` para executar este comando!")
        msg = message.content[5:2000]
        await client.send_message(message.channel, msg)
        await client.delete_message(message)
    #aviso
    if message.content.startswith('!aviso'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, "Você precisa ter a permissão `administrador` para executar este comando!")
        await client.delete_message(message)
        try:
            user = message.author
            msg = message.content[7:]

            embed = discord.Embed(
                title=" 📢 AVISO 📢",
                description="{}".format(msg),
                color=0x0d488a
            )
            embed.set_footer(
                text="Enviado por: " + user.name,
                icon_url=user.avatar_url
            )

            await client.send_message(message.channel, "@everyone")
            await client.send_message(message.channel, embed=embed)
        finally:
            pass
    #apagar
    if message.content.lower().startswith('!apagar'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, "Você precisa ter a permissão `administrador` para executar este comando!")
        qntdd = message.content.strip('!apagar ')
        qntdd = toint(qntdd)
        if qntdd <= 100:
            msg_author = message.author.mention
            await client.delete_message(message)
            await asyncio.sleep(1)
            deleted = await client.purge_from(message.channel, limit=qntdd)
            botmsgdelete = await client.send_message(message.channel, 'Deletei {} mensagens de um pedido de {} para {}'.format(len(deleted), qntdd, msg_author))
            await asyncio.sleep(5)
            await client.delete_message(botmsgdelete)
        else:
            botmsgdelete = await client.send_message(message.channel, 'Utilize o comando digitando /apagar <numero de 1 a 100>')
            await asyncio.sleep(5)
            await client.delete_message(message)
            await client.delete_message(botmsgdelete)
    #votar
    elif message.content.lower().startswith('!votar'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, "Você precisa ter a permissão `administrador` para executar este comando!")
        msg = message.content[7:2000]
        botmsg = await client.send_message(message.channel, msg)
        await client.add_reaction(botmsg, '👍')
        await client.add_reaction(botmsg, '👎')
        await client.delete_message(message)
##STAFF
    #staff
    if message.content.lower().startswith('!staff'):
        role = discord.utils.get(message.server.roles, name='👤 Staff')
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Você precisa ter o cargo `👤 Staff` para executar este comando!")
        embed = discord.Embed(
            title="Comandos para o cargo `👤 Staff` :",
            color=0x0d488a,
            description="!ban <usuário> » Banimento permanentemente do discord.\n"
                        "!kick <usuário> » Expulsão do discord.\n"
                        "!mute <usuário> » Mute permanentemente do discord\n"
                        "!unmute <usuário> » Unmute do discord\n"
                        "\n"
                        "**Desenvolvido pelo Bruno. Mais informações aqui:** [Clique](https://twitter.com/brunoqq_)"
        )
        embed.set_author(
            name="Swift Discord",
            icon_url=client.user.avatar_url
        )
        embed.set_footer(
            text="Copyright © 2018 @brunoqq_",
            icon_url="https://cdn.discordapp.com/emojis/412576344120229888.png?v=1"
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/423159064533532672/424213167317712946/dsg.png"
        )

        await client.send_message(message.channel, "Olá {}, foi enviado todos os comandos para o cargo `👤 Staff` no seu privado!".format(message.author.mention))
        await client.send_message(message.author, embed=embed)
    #ban
    elif message.content.lower().startswith('!ban'):
        role = discord.utils.get(message.server.roles, name='👤 Staff')
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Você precisa ter o cargo `👤 Staff` para executar este comando!")
        membro = message.mentions[0]
        embedmsg = discord.Embed(
            title="⚠ Punição!"
                  "",
            description="O membro {} foi punido do servidor!".format(membro.name),
            color=0x0d488a,
        )
        embedmsg.set_thumbnail(url=membro.avatar_url)

        await client.send_message(message.channel, embed=embedmsg)
        await client.ban(membro)
    #mute
    elif message.content.lower().startswith('!mute'):
        role = discord.utils.get(message.server.roles, name='👤 Staff')
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Você precisa ter o cargo `👤 Staff` para executar este comando!")
        membro = message.mentions[0]
        embedmsg = discord.Embed(
            title="⚠ Punição!"
                  "",
            description="O membro {} foi mutado!".format(membro.name),
            color=0x0d488a,
        )
        embedmsg.set_thumbnail(url=membro.avatar_url)

        await client.send_message(message.channel, embed=embedmsg)
        cargo = discord.utils.get(message.author.server.roles, name='Mutado')
        await client.add_roles(membro, cargo)
    #unmute
    elif message.content.lower().startswith('!unmute'):
        role = discord.utils.get(message.server.roles, name='👤 Staff')
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Você precisa ter o cargo `👤 Staff` para executar este comando!")
        membro = message.mentions[0]
        embedmsg = discord.Embed(
            title="✔ Impunição!"
                  "",
            description="O membro {} foi desmutado!".format(membro.name),
            color=0x0d488a,
        )
        embedmsg.set_thumbnail(url=membro.avatar_url)

        await client.send_message(message.channel, embed=embedmsg)
        cargo = discord.utils.get(message.author.server.roles, name='Mutado')
        await client.remove_roles(membro, cargo)
    #kick
    elif message.content.lower().startswith('!kick'):
        role = discord.utils.get(message.server.roles, name='👤 Staff ')
        if not role in message.author.roles:
            return await client.send_message(message.channel, "Você precisa ter o cargo `👤 Staff ` para executar este comando!")
        membro = message.mentions[0]
        embedmsg = discord.Embed(
            title="⚠ Punição!"
                  "",
            description="O membro {} foi expulso do servidor!".format(membro.name),
            color=0x0d488a,
        )
        embedmsg.set_thumbnail(url=membro.avatar_url)
        await client.kick(membro)
        await client.send_message(message.channel, embed=embedmsg)

@client.event
async def on_member_join(member):

      grupo = discord.utils.find(lambda g: g.name == "🍔 Boladão", member.server.roles)
      await client.add_roles(member, grupo)

      channel = client.get_channel('457325553922473984')
      serverchannel = member.server.default_channel
      embedmsg = discord.Embed(
          title="Olá {}!".format(member.name),
          description="🍔 Bem vindo ao **BielSwift Discord**, divirta-se com a turma dos boladões!",
          color=0x0d488a,
      )
      embedmsg.set_thumbnail(url=member.avatar_url)

      await client.send_message(channel, embed=embedmsg)

client.run(token)
