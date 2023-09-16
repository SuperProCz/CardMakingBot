from imgurpython import ImgurClient
from removebg import RemoveBg
from PIL import Image, ImageOps
import discord
from discord import app_commands 

client_id = [INSERT YOUR IMGUR CLIENT_ID HERE]
client_secret = [INSERT YOUR IMGUR CLIENT_ID HERE]

imgur_client = ImgurClient(client_id, client_secret)

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
    async def on_ready(self):
        await self.wait_until_ready()
        await tree.sync(guild=discord.Object(id=[INSERT YOUR GUILD_ID HERE]))
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'create', description='Create a card!', guild=discord.Object(id=936936341894221864))
async def test(interaction: discord.Interaction, image: discord.Attachment, remove_background: bool):
    channel = interaction.channel
    await interaction.response.send_message("creating the image...")
    await image.save("discord.png")
    if remove_background:
        remove_background_func("discord.png")
    edit_img("discord.png")
    await channel.send("Link: " + upload_image("discord.png"))
    


def edit_img(image):
    img = Image.open(image)
    width, height = img.size 
    if width % 2 != 0:
        img = img.crop((0, width, 0, 0))
    elif height % 2 != 0:
        img = img.crop((0, 0, 0, height))
    img = img.resize((217,342))
    img_with_border = ImageOps.expand(img,border=4,fill='white')
    img_with_border.save(image)

def remove_background_func(path):
    #print("Removing bg")
    rmbg = RemoveBg(INSERT YOUR REMOVEBG TOKEN HERE, "error.log")
    new_img = rmbg.remove_background_from_img_file(path)
    #print("Bg removed!!")

def upload_image(image):
    #print("Uploading image...")
    image = imgur_client.upload_from_path(image, config=None, anon=True)
    #print("Done")
    #print("The link to the image is: ", image["link"])
    return image['link']

client.run([INSERT YOUR DISCORD BOT TOKEN HERE])
