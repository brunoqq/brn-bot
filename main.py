import discord
import asyncio
import io
import requests
import safygiphy
import random
import aiohttp
import time
import os

client = discord.Client()

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto
    token = secreto.token

g = safygiphy.Giphy()
brunoid = "359129090285895680"

msg_id = None
msg_user = None
msg_author = None
qntdd = int
reaction_msg_stuff = {"role_msg_id": None, "role_msg_user_id": None, "r_role_msg_id": None, "r_role_msg_user_id": None}
BOTCOLOR = 0x547e34
version = "Not found!"
user = discord.Member

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
    print (client.user.id)
    print(f"Bot Version: {version}")
    print("=================================")
    await client.change_presence(game=discord.Game(name="!AJUDA", url='https://twitch.tv/TheDiretor', type=1))

@client.event
async def on_message(message):
#VEJA O MS DE CONEXÃO DO BOT
    if message.content.lower().startswith('!ping'):
      timep = time.time()
      emb = discord.Embed(title='Aguarde', color=0x565656)
      pingm0 = await client.send_message(message.channel, embed=emb)
      ping = time.time() - timep
      pingm1 = discord.Embed(title='Pong!', description=':ping_pong: Ping - %.01f segundos' % ping, color=0x15ff00)
      await client.edit_message(pingm0, embed=pingm1)

#ROLA UM DADO
    if message.content.lower().startswith('!dado'):
        choice = random.randint(1, 6)
        embeddad = discord.Embed(title='Dado', description=' Joguei o dado, o resultado é :  {} 🎲'.format(choice),
                             colour=0x1abc9c)
        await client.send_message(message.channel, embed=embeddad)

#INFO DO SERVIDOR
    if message.content.lower().startswith('!serverinfo'):
        server = message.server
        embedserver = discord.Embed(
            title='Informaçoes do Servidor',
            color=0x551A8B,
            descripition='Essas são as informaçoes\n')
        embedserver = discord.Embed(name="{} Server ".format(message.server.name), color=0x551A8B)
        embedserver.add_field(name="Nome:", value=message.server.name, inline=True)
        embedserver.add_field(name="Dono:", value=message.server.owner.mention)
        embedserver.add_field(name="ID:", value=message.server.id, inline=True)
        embedserver.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        embedserver.add_field(name="Membros:", value=len(message.server.members), inline=True)
        embedserver.add_field(name="Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        embedserver.add_field(name="Emojis:", value=f"{len(message.server.emojis)}/100")
        embedserver.add_field(name="Região:", value=str(message.server.region).title())
        embedserver.set_thumbnail(url=message.server.icon_url)
        embedserver.set_footer(text="By: brunoqq")
        await client.send_message(message.channel, embed=embedserver)

#GERA UM CONVITE E ENVIA NO PRIVADO DE QUEM EXECUTOU O COMANDO
    if message.content.lower().startswith('!convite'):
        invite = await client.create_invite(message.channel, max_uses=1, xkcd=True)
        await client.send_message(message.author, "Seu convite é {}".format(invite.url))
        await client.send_message(message.channel, "Olá {}, acabei de enviar um convite na sua direct.".format(message.author.mention))

#BANE UM MEMBRO
    elif message.content.lower().startswith('!ban'):
        membro = message.mentions[0]
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, "❌ {} Você nao possui permissão para executar este comando!".format(message.author.mention))

        await client.send_message(message.channel, "✔ O staff {} Baniu o membro {}!".format(message.author.mention, message.mentions[0].mention))
        await client.ban(membro)

#KICKA UM MEMBRO
    elif message.content.lower().startswith('!kick'):
        member = message.mentions[0]
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, "❌ {} Você nao possui permissão para executar este comando!".format(message.author.mention))

        await client.send_message(message.channel, "✔ O staff {} expulsou o membro {}!".format(message.author.mention, message.mentions[0].mention))
        await client.kick(member)

#MUTA UM MEMBRO
    elif message.content.lower().startswith('!mute'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        mention = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Mutado ❌')
        await client.add_roles(mention, cargo)
        await client.send_message(message.channel, '✔ O membro {} foi mutado com sucesso!'.format(mention))

#DESMUTA UM MEMBRO
    elif message.content.lower().startswith('!unmute'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        mention = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Mutado ❌')
        await client.remove_roles(mention, cargo)
        await client.send_message(message.channel, '✔ O membro {} foi desmutado com sucesso!'.format(mention))

#COMANDOS PARA SETAR ROLES
    #FRIEND
    elif message.content.lower().startswith('!setfriend'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Friend 💯')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Friend" foi adicionado ao membro {}!'.format(user.mention))

    elif message.content.lower().startswith('!removefriend'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Friend 💯')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Friend" foi removido do membro {}!'.format(user.mention))

    #MEMBER
    elif message.content.lower().startswith('!setmember'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Membro ⏳')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Membro" foi adicionado ao membro {}!'.format(user.mention))

    elif message.content.lower().startswith('!removemember'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Membro ⏳')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Membro" foi removido do membro {}!'.format(user.mention))

    #STAFF
    elif message.content.lower().startswith('!setstaff'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Staff 🔒')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Staff" foi adicionado ao membro {}!'.format(user.mention))

    elif message.content.lower().startswith('!removestaff'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Staff 🔒')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Staff" foi removido do membro {}!'.format(user.mention))

    #DESIGNER
    elif message.content.lower().startswith('!setdesigner'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Designer 🎨')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Designer" foi adicionado ao membro {}!'.format(user.mention))

    elif message.content.lower().startswith('!removedesigner'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Designer 🎨')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Designer" foi removido do membro {}!'.format(user.mention))

    #YOUTUBER
    elif message.content.lower().startswith('!setyoutuber'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='YouTuber 🎥')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "YouTuber" foi adicionado ao membro {}!'.format(user.mention))

    elif message.content.lower().startswith('!removeyoutuber'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='YouTuber 🎥')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "YouTuber" foi removido do membro {}!'.format(user.mention))

    #GAMER
    elif message.content.lower().startswith('!setgamer'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Gamer 🎮')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Gamer" foi adicionado ao membro {}!'.format(user.mention))

    elif message.content.lower().startswith('!removegamer'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Gamer 🎮')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Gamer" foi removido do membro {}!'.format(user.mention))

    #PROGRAMADOR
    elif message.content.lower().startswith('!setprogramador'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Programador 💻')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Programador" foi adicionado ao membro {}!'.format(user.mention))

    elif message.content.lower().startswith('!removeprogramador'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Programador 💻')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Programador" foi removido do membro {}!'.format(user.mention))

    #ADMINISTRADOR
    elif message.content.lower().startswith('!setadmin'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Administrador ⭐')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Administrador" foi adicionado ao membro {}!'.format(user.mention))

    elif message.content.lower().startswith('!removeadmin'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Administrador ⭐')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Administrador" foi removido do membro {}!'.format(user.mention))

    #CLIENTE
    elif message.content.lower().startswith('!setcliente'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Cliente ✔')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Cliente" foi adicionado ao membro {}!'.format(user.mention))

    elif message.content.lower().startswith('!removecliente'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Cliente ✔')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Cliente" foi removido do membro {}!'.format(user.mention))

    #DISCORD DEVELOPER
    elif message.content.lower().startswith('!setdcdev'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Discord Developer ☕')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Discord Developer" foi adicionado ao membro {}!'.format(user.mention))

    elif message.content.lower().startswith('!removedcdev'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Discord Developer ☕')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, '✔ Grupo "Discord Developer" foi removido do membro {}!'.format(user.mention))

    #GAY
    elif message.content.lower().startswith('!setgay'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Gay 🍌')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, '✔ O membro {} se assumiu e virou gay!'.format(user.mention))

    elif message.content.lower().startswith('!removegay'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Gay 🍌')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, '✔ O membro {} parou de jogar LOL!'.format(user.mention))

#INICIA UMA VOTAÇÃO COM REAÇÃO DE LIKE E DESLIKE
    elif message.content.lower().startswith('!votar'):
        msg = message.content[7:2000]
        botmsg = await client.send_message(message.channel, msg)
        await client.add_reaction(botmsg, '👍')
        await client.add_reaction(botmsg, '👎')
        await client.delete_message(message)

#ALTERE O STATUS DE JOGO DO BOT
    if message.content.startswith('!jogando'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        game = message.content[9:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Status de jogo alterado para: " + game + " ")

#GERA UM GIF/VÍDEO ALEATÓRIO DE GATO
    if message.content.lower().startswith('!cat'):
        async with aiohttp.get('http://aws.random.cat/meow') as r:
            if r.status == 200:
                js = await r.json()
                canal = message.channel
                await client.delete_message(message)
                await client.send_message(canal, js['file'])

#GERA UM GIF/VÍDEO ALEATÓRIO DE CACHORRO
    if message.content.lower().startswith('!dog'):
        async with aiohttp.get('https://random.dog/woof.json') as r:
            if r.status == 200:
                js = await r.json()
                canal = message.channel
                await client.delete_message(message)
                await client.send_message(canal, js['url'])

#PEGA O AVATAR DO USUÁRIO
    elif message.content.lower().startswith('!avatar'):
        try:
            membro = message.mentions[0]
            avatarembed = discord.Embed(
                title="",
                color=0xFF8000,
                description="**[Clique aqui](" + membro.avatar_url + ") para acessar o link de seu avatar!**"
            )
            avatarembed.set_author(name=membro.name)
            avatarembed.set_image(url=membro.avatar_url)
            await client.send_message(message.channel, embed=avatarembed)
        except:
            avatarembed2 = discord.Embed(
                title="",
                color=0xFF8000,
                description="**[Clique aqui](" + message.author.avatar_url + ") para acessar o link de seu avatar!**"
            )
            avatarembed2.set_author(name=message.author.name)
            avatarembed2.set_image(url=message.author.avatar_url)
            await client.send_message(message.channel, embed=avatarembed2)

#APAGA DE 1 A 100 MENSAGENS
    if message.content.lower().startswith('!apagar'):
        qntdd = message.content.strip('!apagar ')
        qntdd = toint(qntdd)

        cargo = discord.utils.find(lambda r: r.name == "Staff 🔒", message.server.roles)

        if message.author.top_role.position >= cargo.position:
            if qntdd <= 100:
                msg_author = message.author.mention
                await client.delete_message(message)
                # await asyncio.sleep(1)
                deleted = await client.purge_from(message.channel, limit=qntdd)
                botmsgdelete = await client.send_message(message.channel,
                                                         '{} mensagens foram excluidas com sucesso, {}.'.format(
                                                             len(deleted), msg_author))
                await asyncio.sleep(5)
                await client.delete_message(botmsgdelete)

            else:
                botmsgdelete = await client.send_message(message.channel,
                                                         'Utilize o comando digitando !apagar <numero de 1 a 100>.')
                await asyncio.sleep(5)
                await client.delete_message(message)
                await client.delete_message(botmsgdelete)

        else:
            await client.send_message(message.channel, 'Você não tem permissão para utilizar este comando.')

#PEGA INFORMAÇÕES DO USUÁRIO
    if message.content.startswith('!user'):
        try:
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]

            userembed = discord.Embed(
                title="Nome:",
                description=user.name,
                color=0xe67e22
            )
            userembed.set_author(
                name="Informações do usuário"
            )
            userembed.add_field(
                name="Entrou no servidor em:",
                value=userjoinedat
            )
            userembed.add_field(
                name="Criou seu Discord em:",
                value=usercreatedat
            )
            userembed.add_field(
                name="TAG:",
                value=user.discriminator
            )
            userembed.add_field(
                name="ID:",
                value=user.id
            )

            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, "Usuário não encontrado!")
        except:
            await client.send_message(message.channel, "Erro, desculpe. ")
        finally:
            pass

    if message.content.startswith('!aviso'):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel, '❌ Você não possui permissão para executar este comando!')
        await client.delete_message(message)
        try:
            user = message.author
            msg = message.content[7:]

            embed = discord.Embed(
                title=" 📢 AVISO 📢",
                description="{}".format(msg),
                color=0xe67e22
            )
            embed.set_footer(
                text="Enviado por: " + user.name,
                icon_url=user.avatar_url
            )

            await client.send_message(message.channel, "@everyone")
            await client.send_message(message.channel, embed=embed)
        finally:
            pass

#GERA UM GIF
    if message.content.startswith('!gif'):
        gif_tag = message.content[5:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

#GERA UM GIF DIVERTIDO
    if message.content.startswith('!diversão'):
        gif_tag = "fun"
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

#MOEDA CARA OU COROA
    if message.content.lower().startswith('!moeda'):
       choice = random.randint(1, 2)
       if choice == 1:
        await client.add_reaction(message, '🌝')
       if choice == 2:
        await client.add_reaction(message, '👑')

#CANAL DE SUGESTÕES, TODA MENSAGEM ENVIADA NESSE CANAL TEM ESSAS DUAS REAÇÕES
    if message.channel.id == ("431895749593137152"):
        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")

#BOT AVISA O QUE FOI DITO
    if message.content.lower().startswith("!say"):
        msg = message.content[5:2000]
        await client.send_message(message.channel, msg)
        await client.delete_message(message)

#INFORMAÇÕES DO BOT NO PRIVADO
    if message.content.lower().startswith('!ajuda'):
        embed = discord.Embed(
            title="Meus comandos:",
            color=0xe67e22,
            description="***!moeda*** » Aposte com seu amigo no cara ou coroa.\n"
                        "***!user*** `<usuário>` » Veja as informações do usuário.\n"
                        "***!convite*** » Pegue nosso convite e espalhe para novas pessoas. \n"
                        "***!ping*** » Veja o meu ping. \n"
                        "***!cargo*** » Escolha UM cargo voluntário. \n"
                        "***!r_cargo*** » Remova um cargo voluntário. \n"
                        "***!gif*** `<tag do gif (de preferencia em inglês)>` » Gere um GIF aleátorio. \n"
                        "***!dado*** » Role um dado com um número de 1 a 6. \n"
                        "***!dog*** » Gere um gif/vídeo de um cachorro. \n"
                        "***!cat*** » Gere um gif/vídeo de um gato. \n"
                        "***!avatar*** `<usuário>` » Veja a foto de perfil de um usuário.\n"
                        "***Qualquer dúvida me contate no Twitter!*** [Clique aqui](https://twitter.com/brunoqq_)"
        )
        embed.set_author(
            name="BrunoBot",
            icon_url=client.user.avatar_url,
            url="https://twitter.com/brunoqq_"
        )
        embed.set_footer(
            text="Copyright © 2018 Bruno",
            icon_url="https://cdn.discordapp.com/emojis/412576344120229888.png?v=1"
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/423159064533532672/424213167317712946/dsg.png"
        )

        await client.send_message(message.channel, "Olá {}, te enviei todos os meus comandos no seu privado!".format(
            message.author.mention))
        await client.send_message(message.author, embed=embed)

    #ADICIONA O CARGO POR REAÇÃO
    if message.content.lower().startswith("!cargo"):
        embed = discord.Embed(
            title="Escolha um cargo:",
            color=BOTCOLOR,
            description="- Programador = 💻\n"
                        "- Gamer = 🎮\n"
                        "- Designer = 🎨"
        )
        msg = await client.send_message(message.channel, embed=embed)
        await client.add_reaction(msg, "💻")
        await client.add_reaction(msg, "🎮")
        await client.add_reaction(msg, "🎨")

        reaction_msg_stuff["role_msg_user_id"] = message.author.id
        reaction_msg_stuff["role_msg_id"] = msg.id

#REMOVE O CARGO POR REAÇÃO
    if message.content.lower().startswith("!r_cargo"):
        embed = discord.Embed(
            title="Remova algum cargo:",
            color=BOTCOLOR,
            description="- Programador = 💻\n"
                        "- Gamer = 🎮\n"
                        "- Designer = 🎨"
        )
        msg = await client.send_message(message.channel, embed=embed)
        await client.add_reaction(msg, "💻")
        await client.add_reaction(msg, "🎮")
        await client.add_reaction(msg, "🎨")

        reaction_msg_stuff["r_role_msg_user_id"] = message.author.id
        reaction_msg_stuff["r_role_msg_id"] = msg.id

#REAÇÃO POR ROLE
@client.event
async def on_reaction_add(reaction, user):
    msgid = reaction.message.id
    try:
        # ADD ROLES
        if reaction.emoji == '💻' and msgid == reaction_msg_stuff["role_msg_id"] and user.id == reaction_msg_stuff[
            "role_msg_user_id"]:
            for role in reaction.message.server.roles:
                if role.name.lower() == "programador 💻":
                    await client.add_roles(user, role)

        if reaction.emoji == '🎮' and msgid == reaction_msg_stuff["role_msg_id"] and user.id == reaction_msg_stuff[
            "role_msg_user_id"]:
            for role in reaction.message.server.roles:
                if role.name.lower() == "gamer 🎮":
                    await client.add_roles(user, role)

        if reaction.emoji == '🎨' and msgid == reaction_msg_stuff["role_msg_id"] and user.id == reaction_msg_stuff[
            "role_msg_user_id"]:
            for role in reaction.message.server.roles:
                if role.name.lower() == "designer 🎨":
                    await client.add_roles(user, role)

        if reaction.emoji == '💻' and msgid == reaction_msg_stuff["r_role_msg_id"] and user.id == reaction_msg_stuff[
            "r_role_msg_user_id"]:
            for role in reaction.message.server.roles:
                if role.name.lower() == "programador 💻":
                    await client.remove_roles(user, role)

        if reaction.emoji == '🎮' and msgid == reaction_msg_stuff["r_role_msg_id"] and user.id == reaction_msg_stuff[
            "r_role_msg_user_id"]:
            for role in reaction.message.server.roles:
                if role.name.lower() == "gamer 🎮":
                    await client.remove_roles(user, role)

        if reaction.emoji == '🎨' and msgid == reaction_msg_stuff["r_role_msg_id"] and user.id == reaction_msg_stuff[
            "r_role_msg_user_id"]:
            for role in reaction.message.server.roles:
                if role.name.lower() == "designer 🎨":
                    await client.remove_roles(user, role)
    except discord.errors.HTTPException as e:
        await client.send_message(reaction.message.channel, e)

#AO ENTRAR ELE ENVIA MENSAGEM NO PRIVADO, SETA ROLE MEMBRO E ENVIA MENSAGEM NO CANAL DO DISCORD
@client.event
async def on_member_join(member):

      await client.send_message(member, "Seja bem vindo ao nosso Discord! Qualquer dúvida, sugestões ou bugs contate nosso fundador Bruno#7647!")
      grupo = discord.utils.find(lambda g: g.name == "Membro ⏳", member.server.roles)
      await client.add_roles(member, grupo)

      channel = client.get_channel('431895597423919105')
      serverchannel = member.server.default_channel
      msg = "Seja bem vindo ao servidor {0}, leia as regras e divirta-se!".format(member.mention, member.server.name)
      await client.send_message(channel, msg)

#MENSAGEM QUANDO ALGUÉM SAI DO SERVIDOR
@client.event
async def on_member_remove(member):

    channel = client.get_channel('')
    serverchannel = member.server.default_channel
    msg = "Xau xau {0}".format(member.name)
    await client.send_message(channel, msg)

client.run(token)
