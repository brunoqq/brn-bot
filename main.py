import discord
import asyncio
import io
import requests
import safygiphy
import random
import os

client = discord.Client()

g = safygiphy.Giphy()
brunoid = "359129090285895680"

msg_id = None
msg_user = None
msg_author = None
qntdd = int
reaction_msg_stuff = {"role_msg_id": None, "role_msg_user_id": None, "r_role_msg_id": None, "r_role_msg_user_id": None}
BOTCOLOR = 0x547e34
version = "Beta 1.0.0"

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
    print(f"Bot Versão: {version}")
    print("=================================")
    await client.change_presence(game=discord.Game(name="!AJUDA", url='https://twitch.tv/TheDiretor', type=1))

@client.event
async def on_message(message):
    
    if message.content.lower().startswith('!convite'):
        invite = await client.create_invite(message.channel, max_uses=1, xkcd=True)
        await client.send_message(message.author, "Seu convite é {}".format(invite.url))
        await client.send_message(message.channel, "Olá {}, acabei de enviar um convite na sua direct.".format(message.author.mention))

    if message.content.startswith('!jogando') and message.author.id == brunoid:
        game = message.content[9:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Status de jogo alterado para: " + game + " ")

    if message.content.lower().startswith('!apagar'):
        qntdd = message.content.strip('!apagar ')
        qntdd = toint(qntdd)

        cargo = discord.utils.find(lambda r: r.name == "MEMBRO", message.server.roles)

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
                        "***!gif*** » Gere um GIF aleátorio."
        )
        embed.set_author(
            name="BrunoBot",
            icon_url="https://cdn.discordapp.com/attachments/423159064533532672/424213167317712946/dsg.png",
            url="https://twitter.com/brunoqq_"
        )
        embed.set_footer(
            text="Copyright © 2018 Bruno",
            icon_url="https://cdn.discordapp.com/emojis/412576344120229888.png?v=1"
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/423159064533532672/424213167317712946/dsg.png"
        )

        await client.send_message(message.channel, "Olá {}, te enviei todos os meus comandos no seu privado!".format(message.author.mention))
        await client.send_message(message.author, embed=embed)

    if message.content.startswith('!gif'):
        gif_tag = message.content[5:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

    if message.content.startswith('!diversão'):
        gif_tag = "fun"
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

    if message.content.lower().startswith('!moeda'):
       choice = random.randint(1, 2)
       if choice == 1:
        await client.add_reaction(message, '🌝')
       if choice == 2:
        await client.add_reaction(message, '👑')

    if message.channel.id == ("423558695516110848"):
        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")

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
        
    if message.content.lower().startswith("!say"):
        msg = message.content[5:2000]
        await client.send_message(message.channel, msg)
        await client.delete_message(message)  
        
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

@client.event
async def on_member_join(member):

      await client.send_message(member, "Seja bem vindo ao nosso Discord! Qualquer dúvida, sugestões ou bugs contate nosso fundador Bruno#7647!")
      grupo = discord.utils.find(lambda g: g.name == "MEMBRO", member.server.roles)
      await client.add_roles(member, grupo)

      channel = client.get_channel('423159064533532672')
      serverchannel = member.server.default_channel
      msg = "Seja bem vindo ao servidor {0}, divirta-se!".format(member.mention, member.server.name)
      await client.send_message(channel, msg)

@client.event
async def on_member_remove(member):

    channel = client.get_channel('423159064533532672')
    serverchannel = member.server.default_channel
    msg = "Xau xau {0}".format(member.mention)
    await client.send_message(channel, msg)

client.run('NDI0MjExODY0NzI2Mjc0MDQ4.DZcJ6w.rl-VphijKvXjAod0I1JIFj4DwxU')
