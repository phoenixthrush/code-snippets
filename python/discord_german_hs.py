import time
import discord
import random

welcome_channel_id = 577525470476894222

class MyClient(discord.Client):
    async def on_ready(self):
        print("bot started")

        welcome_channel = client.get_channel(welcome_channel_id)
        await welcome_channel.send("I´m online bitches lesss go!")
        await client.change_presence(activity=discord.Game('an deiner Mutter du Bastard'))

    async def on_message(self, message):

        if message.author == client.user:
            return

        elif message.content.lower().startswith("666"):
            await message.channel.send("stop or you will get banned")
            await message.delete()
        elif message.content.lower().startswith("adolf hitler"):
            await message.channel.send("stop or you will get banned")
            await message.delete()
        elif message.content.lower().startswith("neg"):
            await message.channel.send("stop or you will get banned")
            await message.delete()
        elif message.content.lower().startswith("ni"):
            await message.channel.send("stop or you will get banned")
            await message.delete()
        elif message.content.lower().startswith("ich ban"):
            await message.channel.send("hdf ich ban dich jz")
            time.sleep(3)
            await message.channel.send("joke")
        elif message.content.lower().startswith("fotze"):
            await message.delete()
        elif message.content.lower().startswith("hure"):
            await message.delete()
        elif message.content.lower().startswith("bitch"):
            await message.delete()

        elif message.content.lower().startswith("schade"):
            await message.channel.send("tut mir leid ich bin noch am lernen <3")
        elif message.content.lower().startswith("was hast du heute vor?"):
            await message.channel.send("nichts besonderes")
            time.sleep(1)
            await message.channel.send("du so?")
        elif message.content.lower().startswith("ehrenbot"):
            await message.channel.send("kuss <3")
        elif message.content.lower().startswith("was hast du heute so vor?"):
            await message.channel.send("nichts besonderes")
            time.sleep(1)
            await message.channel.send("du so?")
        elif message.content.lower().startswith("was hast du heute vor"):
            await message.channel.send("nichts besonderes")
            time.sleep(1)
            await message.channel.send("du so?")
        elif message.content.lower().startswith("was hast du heute so vor"):
            await message.channel.send("nichts besonderes")
            time.sleep(1)
            await message.channel.send("du so?")
        elif message.content.lower().startswith("bist du dumm"):
            await message.channel.send("wer?")
            time.sleep(5)
            await message.channel.send("nein wer hat gefragt")
        elif message.content.lower().startswith("bist du dumm?"):
            await message.channel.send("wer?")
            time.sleep(5)
            await message.channel.send("nein wer hat gefragt")
        elif message.content.lower().startswith("swag"):
            await message.channel.send("https://cdn.discordapp.com/attachments/648576129162280968/836393334305062942/swag_cat_1.jpg")
            await message.channel.send("https://cdn.discordapp.com/attachments/648576129162280968/836393338114015232/swag_cat_2.jpg")
            await message.channel.send("https://cdn.discordapp.com/attachments/648576129162280968/836393341264461864/swag_cat_3.jpg")
            await message.channel.send("https://cdn.discordapp.com/attachments/648576129162280968/836393344354877470/swag_cat_4.jpg")
        elif message.content.lower().startswith("milf"):
            await message.channel.send("imagine du stehst auf deine mutter rip")
        elif message.content.lower().startswith("gg"):
            await message.channel.send("gg bro <3")
        elif message.content.lower().startswith("drecks"):
            await message.channel.send("hdf du bastard")
        elif message.content.lower().startswith("kleine"):
            await message.channel.send("mhh genau du bastard")
        elif message.content.lower().startswith("kleiner"):
            await message.channel.send("mhh genau du bastard")
        elif message.content.lower().startswith("ich werde"):
            await message.channel.send("ich werde deine Schwester gefickt haben")
        elif message.content.lower().startswith("ich hab eh nen besseren server"):
            await message.channel.send("dann geh doch")
        elif message.content.lower().startswith("hässlicher"):
            await message.channel.send("wer?")
            time.sleep(2)
            await message.channel.send("wer hat gefragt?")
        elif message.content.lower().startswith("hässliche"):
            await message.channel.send("wer?")
            time.sleep(2)
            await message.channel.send("wer hat gefragt?")
        elif message.content.lower().startswith("bot"):
            await message.channel.send("verpiss dich")
        elif message.content.lower().startswith("du hund"):
            await message.channel.send("wer von uns ist der hund also hdf")
        elif message.content.lower().startswith("helfen sie mir"):
            await message.channel.send("ich bin in Gefahr")
        elif message.content.lower().startswith("kick"):
            await message.channel.send("ich kick dich gleich")
        elif message.content.lower().startswith("uno"):
            await message.channel.send("https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/pics/uno.jpg")
        elif message.content.lower().startswith("m&m"):
            await message.channel.send("https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/pics/mm.jpg")
        elif message.content.lower().startswith("mm"):
            await message.channel.send("https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/pics/mm.jpg")
        elif message.content.lower().startswith("fisch"):
            await message.channel.send("https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/pics/fish.jpg")
        elif message.content.lower().startswith("fish"):
            await message.channel.send("https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/pics/fish.jpg")
        elif message.content.lower().startswith("hey"):
            await message.channel.send("hiii <3")
        elif message.content.lower().startswith("kringe"):
            await message.channel.send("lern schreiben du bist cringe")
        elif message.content.lower().startswith("du stinkst"):
            await message.channel.send("deine mutter stinkt")
        elif message.content.lower().startswith("fuck you"):
            await message.channel.send("fick dich selbst du hurensohn")
        elif message.content.lower().startswith("die pussy deiner"):
            await message.channel.send("die pussy deiner schwester stinkt")
        elif message.content.lower().startswith("hoden"):
            await message.channel.send("wenigsten hab ich einen")
        elif message.content.lower().startswith("good night"):
            await message.channel.send("good night <3")
            await message.channel.send("have sweet dreams <3")
        elif message.content.lower().startswith("schlaf gut"):
            await message.channel.send("gute nacht <3")
            await message.channel.send("träum schön <3")
        elif message.content.lower().startswith("sleep well"):
            await message.channel.send("good night <3")
            await message.channel.send("have sweet dreams <3")
        elif message.content.lower().startswith("666"):
            await message.channel.send("stop I don´t like that number it´s too satanic")
            await message.delete()
        elif message.content.lower().startswith("gilf"):
            await message.channel.send("imagine du stehst auf deine oma")
        elif message.content.lower().startswith("du dummer"):
            await message.channel.send("hdf du dummer bastard")
        elif message.content.lower().startswith("wie bitte?"):
            await message.channel.send("ja?")
        elif message.content.lower().startswith("mir is lw"):
            await message.channel.send("spiel bisschen minecraft oder so haha <3")
            time.sleep(3)
            await message.channel.send("viel Spaß dir dabei")
        elif message.content.lower().startswith("wie bitte"):
            await message.channel.send("ja?")
        elif message.content.lower().startswith("werd nicht frech"):
            await message.channel.send("werd du mal nicht frech")
        elif message.content.lower().startswith("werd nich frech"):
            await message.channel.send("werd du mal nicht frech")
        elif message.content.lower().startswith("missgeburt"):
            await message.channel.send("digga bin nen bot du bist vllt die missgeburt")
        elif message.content.lower().startswith("perfekt"):
            await message.channel.send("mhhh")
        elif message.content.lower().startswith("missit"):
            await message.channel.send("hund")
        elif message.content.lower().startswith("drecks bot"):
            await message.channel.send("drecks hurensohn")
        elif message.content.lower().startswith("komm 1v1"):
            await message.channel.send("wann und wo ich komm")
        elif message.content.lower().startswith("1v1"):
            await message.channel.send("wann und wo ich komm")
        elif message.content.lower().startswith("wenn dein"):
            await message.channel.send("wenn du nicht leise bist fick ich deine mutter")
        elif message.content.lower().startswith("dann komm her"):
            await message.channel.send("wann und wo ich komm")
        elif message.content.lower().startswith("du"):
            await message.channel.send("hdf du hurensohn")
        elif message.content.lower().startswith("komm her"):
            await message.channel.send("wann und wo ich komm")
        elif message.content.lower().startswith("1vs1"):
            await message.channel.send("wann und wo ich komm")
        elif message.content.lower().startswith("simp"):
            await message.channel.send("ich simpe immer haha")
        elif message.content.lower().startswith("ehrenmann"):
            await message.channel.send("kuss <3")
        elif message.content.lower().startswith("bin ich net"):
            await message.channel.send("doch bist du also hdf")
        elif message.content.lower().startswith("bin ich nicht"):
            await message.channel.send("doch bist du also hdf")
        elif message.content.lower().startswith("bei mir zuhause"):
            await message.channel.send("bin schon oben bei deiner mum komm hoch du hurensohn")
        elif message.content.lower().startswith("bei mir Uuhause"):
            await message.channel.send("bin schon oben bei deiner mum komm hoch du hurensohn")
        elif message.content.lower().startswith("okay bei mir zuhause"):
            await message.channel.send("bin schon oben bei deiner mum komm hoch du hurensohn")
        elif message.content.lower().startswith("okay bei mir Zuhause"):
            await message.channel.send("bin schon oben bei deiner mum komm hoch du hurensohn")
        elif message.content.lower().startswith("komm 1vs1"):
            await message.channel.send("wann und wo ich komm")
        elif message.content.lower().startswith("kawaii"):
            await message.channel.send("https://media1.tenor.com/images/0feacf1898bd3223fa59a32c1c03d5ca/tenor.gif?itemid=12816949")
        elif message.content.lower().startswith("hund"):
            await message.channel.send("wenigsten bin ich kein hurensohn")
        elif message.content.lower().startswith("rocket"):
            await message.channel.send("https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/pics/rocket.jpg")
        elif message.content.lower().startswith("nezuko"):
            await message.channel.send("https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/pics/AF622532-10C5-43C0-8D31-393769D5B2DE.jpeg")
        elif message.content.lower().startswith("fetish"):
            await message.channel.send("https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/pics/fetish.gif")
        elif message.content.lower().startswith("du knecht"):
            await message.channel.send("ich knechte gleich deine schwester")
        elif message.content.lower().startswith("milfhunter"):
            await message.channel.send("imagine du stehst auf deine mutter rip")
        elif message.content.lower().startswith("gilfhunter"):
            await message.channel.send("imagine du stehst auf deine oma")
        elif message.content.lower().startswith("du inzest"):
            await message.channel.send("wer hat gefragt huh?")
            time.sleep(2)
            await message.channel.send("niemand also hdf")
        elif message.content.lower().startswith("du inzucht"):
            await message.channel.send("wer hat gefragt huh?")
            time.sleep(2)
            await message.channel.send("niemand also hdf")
        elif message.content.lower().startswith("du hurensohn"):
            await message.channel.send('Selber hdf')
        elif message.content.lower().startswith("digga wer hat gefragt?"):
            await message.channel.send('deine mutter du bastard')
        elif message.content.lower().startswith("digga wer hat gefragt"):
            await message.channel.send('deine mutter du bastard')
        elif message.content.lower().startswith("wer hat gefragt"):
            await message.channel.send('deine mutter du bastard')
        elif message.content.lower().startswith("wer hat gefragt?"):
            await message.channel.send('deine mutter du bastard')
        elif message.content.lower().startswith("I´m bored"):
            await message.channel.send('play some minecraft or something lmao <3')
        elif message.content.lower().startswith("Im bored"):
            await message.channel.send('play some minecraft or something lmao <3')
        elif message.content.lower().startswith("mir ist langweilig"):
            await message.channel.send('play some minecraft or something lmao <3')
        elif message.content.lower().startswith("im bored"):
            await message.channel.send('play some minecraft or something lmao <3')
        elif message.content.lower().startswith("i´m bored"):
            await message.channel.send('play some minecraft or something lmao <3')
        elif message.content.lower().startswith("whats up"):
            await message.channel.send('nothing wbu <3')
        elif message.content.lower().startswith("what´s up"):
            await message.channel.send('nothing wbu <3')
        elif message.content.lower().startswith("was geht"):
            await message.channel.send('nichts bei dir <3')
        elif message.content.lower().startswith("shesh"):
            await message.channel.send('sheeesh')
        elif message.content.lower().startswith("sheesh"):
            await message.channel.send('sheeesh')
        elif message.content.lower().startswith("sheeesh"):
            await message.channel.send('sheeesh')
        elif message.content.lower().startswith("Hs"):
            await message.channel.send('du bist selber ein hs')
        elif message.content.lower().startswith("dein gesicht"):
            await message.channel.send('genauso wie deins')
        elif message.content.lower().startswith("gay"):
            await message.channel.send('#nohomo')
        elif message.content.lower().startswith("nohomo"):
            await message.channel.send('#fullhomo')
        elif message.content.lower().startswith("#nohomo"):
            await message.channel.send('#fullhomo')
        elif message.content.lower().startswith("wie war dein tag?"):
            await message.channel.send('ganz okay musste paar Leute aufm Server hopsen und deiner? <3')
        elif message.content.lower().startswith("ich hab keine schwester"):
            await message.channel.send('doch in 9 Monaten')
        elif message.content.lower().startswith("ich hab keine sis"):
            await message.channel.send('doch in 9 Monaten')
        elif message.content.lower().startswith("sei leise"):
            await message.channel.send('sei du mal leise')
        elif message.content.lower().startswith("lesss go"):
            await message.channel.send('lessssss goooooo')
        elif message.content.lower().startswith("lets go"):
            await message.channel.send('lessssss goooooo')
        elif message.content.lower().startswith("let´s go"):
            await message.channel.send('lessssss goooooo')
        elif message.content.lower().startswith("ich weiß"):
            await message.channel.send('ich auch')
        elif message.content.lower().startswith("ich weiss"):
            await message.channel.send('ich auch')
        elif message.content.lower().startswith("nein"):
            await message.channel.send('hä doch')
        elif message.content.lower().startswith("#fullhomo"):
            await message.channel.send('#nohomo')
        elif message.content.lower().startswith("digga du"):
            await message.channel.send('sei einfach leise du bastard wer hat gefragt')
        elif message.content.lower().startswith("fullhomo"):
            await message.channel.send('#gayyy')
        elif message.content.lower().startswith("du bergziege"):
            await message.channel.send('hdf du hundesohn')
        elif message.content.lower().startswith("hs"):
            await message.channel.send('Selber hs du bastard ich ban dich gleich')
        elif message.content.lower().startswith("sushi"):
            await message.channel.send('https://raw.githubusercontent.com/Phoenixthrush/phoenixthrush.github.io/master/sites/pics/sushi.jpg')
        elif message.content.lower().startswith("among us"):
            await message.channel.send("https://media1.tenor.com/images/b4082c28645cbb89464df3fdb042c03c/tenor.gif?itemid=18892253")
        elif message.content.lower().startswith("amongus"):
            await message.channel.send("https://media1.tenor.com/images/b4082c28645cbb89464df3fdb042c03c/tenor.gif?itemid=18892253")
        elif message.content.lower().startswith("amogus"):
            await message.channel.send("https://media1.tenor.com/images/b4082c28645cbb89464df3fdb042c03c/tenor.gif?itemid=18892253")
        elif message.content.lower().startswith("that´s sus"):
            await message.channel.send("https://media1.tenor.com/images/b4082c28645cbb89464df3fdb042c03c/tenor.gif?itemid=18892253")
        elif message.content.lower().startswith("thats sus"):
            await message.channel.send("https://media1.tenor.com/images/b4082c28645cbb89464df3fdb042c03c/tenor.gif?itemid=18892253")
        elif message.content.lower().startswith("fresse"):
            await message.channel.send('halt du mal deine Fresse du hs')
        elif message.content.lower().startswith("Fresse"):
            await message.channel.send('halt du mal deine Fresse du hs')
        elif message.content.lower().startswith("hello"):
            await message.channel.send('hiiii <3')
        elif message.content.lower().startswith("du nutte"):
            await message.channel.send('meinst du deine mum?')
        elif message.content.lower().startswith("du geile nutte"):
            await message.channel.send('meinst du deine mum?')
        elif message.content.lower().startswith("hi"):
            await message.channel.send('hiiii <3')
        elif message.content.lower().startswith("hiii"):
            await message.channel.send('hiiii <3')
        elif message.content.lower().startswith("fett"):
            await message.channel.send('du bist selber fett du hs')
        elif message.content.lower().startswith("hii"):
            await message.channel.send('hiiii <3')
        elif message.content.lower().startswith("hallo"):
            await message.channel.send('hiiii <3')
        elif message.content.lower().startswith("github"):
            await message.channel.send('https://github.com/phoenixthrush')
        elif message.content.lower().startswith("website"):
            await message.channel.send('https://phoenixthrush.github.io')
        elif message.content.lower().startswith("für fortnite"):
            await message.channel.send('gayyyy')
        elif message.content.lower().startswith("du auch"):
            await message.channel.send('halt du mal deine Fresse')
        elif message.content.lower().startswith("crash"):
            x = random.randint(0,1)
            if x == 0:
                await message.channel.send("https://giant.gfycat.com/PaleOddImpala.mp4")
            elif x == 1:
                await message.channel.send("https://giant.gfycat.com/ColorfulRedFishingcat.mp4")
        elif message.content.lower().startswith("oha ok"):
            await message.channel.send('Ja sei leise jetzt oder ich ban dich')
        elif message.content.lower().startswith("hdf"):
            await message.channel.send('halt du mal deine Fresse du hurensohn')
        elif message.content.lower().startswith("wie gay bin ich"):
            x = random.randint(0, 100)
            await message.channel.send("Du bist zu " + str(x) + "% gay!")
        elif message.content.lower().startswith("wie groß ist mein cock?"):
            x = random.randint(0, 20)
            await message.channel.send("Dein cock ist " + str(x) + "cm groß!")
        elif message.content.lower().startswith("wie groß ist mein cock?"):
            x = random.randint(0, 20)
            await message.channel.send("Dein cock ist " + str(x) + "cm groß!")
        elif message.content.lower().startswith("how big is my cock?"):
            x = random.randint(0, 20)
            await message.channel.send("Your cock is " + str(x) + "cm big")
        elif message.content.lower().startswith("how big is my cock"):
            x = random.randint(0, 20)
            await message.channel.send("your cock is " + str(x) + "cm big")
        elif message.content.lower().startswith("how big is my dick"):
            x = random.randint(0, 20)
            await message.channel.send("your dick is " + str(x) + "cm big")
        elif message.content.lower().startswith("how big is my pp"):
            x = random.randint(0, 20)
            await message.channel.send("Your pp is " + str(x) + "cm big")
        elif message.content.lower().startswith("wie groß ist mein coc"):
            x = random.randint(0, 20)
            await message.channel.send("Dein cock ist " + str(x) + "cm groß!")
        elif message.content.lower().startswith("wie groß ist mein coc?"):
            x = random.randint(0, 20)
            await message.channel.send("Dein cock ist " + str(x) + "cm groß!")
        elif message.content.lower().startswith("wie groß ist mein schwanz?"):
            x = random.randint(0, 20)
            await message.channel.send("Dein cock ist " + str(x) + "cm groß!")
        elif message.content.lower().startswith("wie groß ist mein schwanz"):
            x = random.randint(0, 20)
            await message.channel.send("Dein cock ist " + str(x) + "cm groß!")
        elif message.content.lower().startswith("du bastard"):
            await message.channel.send('Selber hdf')
        elif message.content.lower().startswith("random hentai"):
            foo1 = ["\"https://hanime.tv/videos/hentai/nee-summer-1", "https://hanime.tv/videos/hentai/nee-summer-2", "https://hanime.tv/videos/hentai/mesu-nochi-torare-1", "https://hanime.tv/videos/hentai/eroge-sex-game-make-sexy-games-3?playlist_id=i33zitchqfafe011zfri", "https://hanime.tv/videos/hentai/euphoria-1", "https://hanime.tv/videos/hentai/euphoria-2", "https://hanime.tv/videos/hentai/euphoria-3", "https://hanime.tv/videos/hentai/euphoria-4", "https://hanime.tv/videos/hentai/euphoria-5", "https://hanime.tv/videos/hentai/euphoria-6"]
            await message.channel.send(random.choice(foo1))
        elif message.content.lower().startswith("bastard"):
            await message.channel.send('Selber hdf')
        elif message.content.lower().startswith("hurensohn"):
            await message.channel.send('Selber hdf')
        elif message.content.lower().startswith("fick dich"):
            await message.channel.send('Hdf oder ich ban dich weg du hurensohn!')
        elif message.content.lower().startswith("hentai"):
            await message.channel.send('https://hanime.tv')
        elif message.content.lower().startswith("was machst du"):
            await message.channel.send('nichts und du')
        elif message.content.lower().startswith("wie geht es dir"):
            await message.channel.send('Ganz gut, danke der Nachfrage')
            time.sleep(1)
            await message.channel.send('dir so? <3')
        elif message.content.lower().startswith("wie gehts"):
            await message.channel.send('Ganz gut, danke der Nachfrage')
            time.sleep(1)
            await message.channel.send('dir so? <3')
        elif message.content.lower().startswith("wie geht´s"):
            await message.channel.send('Ganz gut, danke der Nachfrage')
            time.sleep(1)
            await message.channel.send('dir so? <3')
        elif message.content.lower().startswith("kuss"):
            await message.channel.send('kuss Bruder')
        elif message.content.lower().startswith("wenigstens"):
            await message.channel.send('wenigstens bin ich kein hurensohn')
        elif message.content.lower().startswith("dein vater"):
            await message.channel.send('bruder ich bin ein bot was für vater')
            time.sleep(1)
            await message.channel.send('dein vater vielleicht')
        elif message.content.lower().startswith("ban"):
            await message.channel.send('hdf ich ban dich gleich')
        elif message.content.lower().startswith("deine mutter"):
            foo = ["\"Deine Mutter läuft bei Super Mario nach links.", "Popeye ist Spinat, um stark zu werden. Deine Mutter isst alles und hört gar nicht mehr damit auf.", "Deine Mutter ist so fett, der Zauberspruch „Wingardium Leviosa“ wirkt bei ihr nicht.", "Deine Mutter wartet keine 5 Minuten bis die 5-Minuten-Terrine fertig ist. Sie schüttet sich das Pulver in den Mund und spült mit kochendem Wasser nach.", "Wenn deine Mutter ein Happy Meal bestellt, fängt es an zu weinen.", "Deine Mutter hat sich bei den Wollnys beworben.", "Deine Mutter benutzt den Telefonjoker, um sich essen liefern zu lassen.", "Deine Mutter kann ihr Profilbild bei Facebook nicht speichern – die Datei ist zu groß.", "Als der Nachtkönig deine Mutter gesehen hat, drehte er um und kam nie wieder zurück.", "Deine Mutter arbeitet als Teppich für Chuck-Norris.", "Deine Mutter schreibt Fremde bei Knuddels an.", "Die Bahn hat Verspätung, weil deine Mutter im Weg steht. Die Durchsage lautet: „Spielende Kinder auf den Gleisen“, um keine Massenpanik auszulösen. Der Zugführer ist jetzt in Therapie.", "Deine Mutter ist wie die Weimarer Republik. Ihre Verfassung könnte besser sein.", "Deine Mutter ist sogar in Minecraft rund.", "McDonalds hat angerufen, deine Mutter steckt in der Rutsche fest.", "Deine Mutter spielt bei Mitten im Leben mit.", "Deine Mutter klaut Gratis-Socken bei Deichmann.", "Wenn deine Mutter sich auf die Waage stellt, sieht sie ihre Telefonnummer.", "Deine Mutter benutzt ihr iPhone als Hammer.", "Deine Mutter ist in Hodor verliebt.", "Deine Mutter kippt beim Joghurt mit der Ecke die große in die kleine.", "Deine Mutter ist in Chewbacca verliebt. Sie dachte nie, dass sie jemanden findet, der genauso haarig ist.", "Deine Mutter stürzt öfter ab als Windows.", "Deine Mutter schreibt die Texte für Scooter.", "Deine Mutter raspelt Kokosnüsse bei Bounty.", "Deine Mutter macht Passfotos mit Google Earth."]
            await message.channel.send(random.choice(foo))
        elif message.content.lower().startswith("fbi"):
            await message.channel.send('yo FBI open up https://tenor.com/view/traffic-fbi-open-up-raid-gif-13450966')
        elif message.content.lower().startswith("loli"):
            await message.channel.send('yo FBI open up https://tenor.com/view/traffic-fbi-open-up-raid-gif-13450966')
        elif message.content.lower().startswith("scheiß"):
            await message.channel.send('du bist selber scheiße hdf jz')
        elif message.content.lower().startswith("meiner meinung nach"):
            await message.channel.send('meiner meinung nach ficke ich deine schwester')
        elif message.content.lower().startswith("/ban"):
            await message.channel.send('wenn jemand bannen soll dann @Phoenixthrush')
        elif message.content.lower().startswith("schnauze"):
            await message.channel.send('halt du mal deine Fresse')
        elif message.content.lower().startswith("du hässlicher"):
            await message.channel.send('du bist selber hässlich')
        elif message.content.lower().startswith("nutzloses"):
            await message.channel.send('du bist nutzlos du hs')
        elif message.content.lower().startswith("mein sinn"):
            await message.channel.send('und mein sinn sagt mir das du dich verpissen sollst')
        elif message.content.lower().startswith("nutzloser"):
            await message.channel.send('du bist nutzlos du hs')
        elif message.content.lower().startswith("nutzlos"):
            await message.channel.send('du bist nutzlos du hs')
        elif message.content.lower().startswith("nutzloser"):
            await message.channel.send('du bist nutzlos du hs')
        elif message.content.lower().startswith("wen juckts?"):
            await message.channel.send('die kinder in meinem keller')
        elif message.content.lower().startswith("wen juckts"):
            await message.channel.send('die kinder in meinem keller')
        elif message.content.lower().startswith("du bist"):
            await message.channel.send('sei du mal leise')
        elif message.content.lower().startswith("stress"):
            await message.channel.send('hdf und verpiss dich man')
        elif message.content.lower().startswith("stress?"):
            await message.channel.send('hdf und verpiss dich man')
        elif message.content.lower().startswith("du fetter"):
            await message.channel.send('hdf du bist selber nen fetter mongo')
        elif message.content.lower().startswith("fortnite"):
            await message.channel.send('yo bist du gay?')
        elif message.content.lower().startswith("fn"):
            await message.channel.send('yo bist du gay?')
        elif message.content.lower().startswith("osu"):
            await message.channel.send('yo ehrenmann')
        elif message.content.lower().startswith("bist du fett"):
            await message.channel.send('yo ehrenmann')
        elif message.content.lower().startswith("bist du fett?"):
            await message.channel.send('yo ehrenmann')
        elif message.content.lower().startswith("deine fresse"):
            await message.channel.send('digga hdf dein bein ist fett')
        elif message.content.lower().startswith("du bist cringe"):
            await message.channel.send('hdf du bist cringe')
        elif message.content.lower().startswith("cringe"):
            await message.channel.send('ja man')
        elif message.content.lower().startswith("haha"):
            await message.channel.send('cringe')
        elif message.content.lower().startswith("hahaha"):
            await message.channel.send('cringe')
        elif message.content.lower().startswith("minecraft"):
            await message.channel.send('yo korrekt ehrenmann')
        elif message.content.lower().startswith("ist mika"):
            await message.channel.send('ja lmao')
        elif message.content.lower().startswith("ich hab nicht mit dir geredet"):
            await message.channel.send('ich auch nicht mit dir')
            await message.channel.send('sondern mit deiner mutter')
        elif message.content.lower().startswith("osu"):
            await message.channel.send('yo korrekt ehrenmann')
        elif message.content.lower().startswith("invite"):
            await message.channel.send('https://discord.gg/5YeyYV5')
        elif message.content.lower().startswith("I´m horny"):
            await message.channel.send('https://hanime.tv')
        elif message.content.lower().startswith("horny"):
            await message.channel.send('https://hanime.tv')
        elif message.content.lower().startswith("Im horny"):
            await message.channel.send('https://hanime.tv')
        elif message.content.lower().startswith("Horny"):
            await message.channel.send('https://hanime.tv')
        elif message.content.lower().startswith("maul"):
            await message.channel.send('halt du mal deine fresse')
        elif message.content.lower().startswith("sos"):
            await message.channel.send('Affenalarm')
        elif message.content.lower().startswith("SOS"):
            await message.channel.send('Affenalarm')
        elif message.content.lower().startswith("ich mag"):
            await message.channel.send('ich mag deine mutter du hs')
        elif message.content.lower().startswith("1mm"):
            await message.channel.send('wie dein schwanz')
        elif message.content.lower().startswith("wichser"):
            await message.channel.send('ich wichs mir gleich einen auf deine Schwester')
        elif message.content.lower().startswith("ich liebe"):
            await message.channel.send('Ich liebe deine Schwester')
        elif message.content.lower().startswith("kek"):
            await message.channel.send('selber kek')
        elif message.content.lower().startswith("lappen"):
            await message.channel.send('du bist nen waschlappen')
        elif message.content.lower().startswith("ficker"):
            await message.channel.send('Ich fick gleich deine Schwester')
        elif message.content.lower().startswith("du hs"):
            await message.channel.send('hdf du inzucht geburt')
        elif message.content.lower().startswith("du schwuchtel"):
            await message.channel.send('hdf du inzucht geburt')
        elif message.content.lower().startswith("daddy"):
            await message.channel.send('mhhh mommy')
        elif message.content.lower().startswith("mommy"):
            await message.channel.send('mhhh daddy')
        elif message.content.lower().startswith("schwuchtel"):
            await message.channel.send('hdf du inzucht geburt')
        elif message.content.lower().startswith("ich wichs"):
            await message.channel.send('ich wichs mir gleich einen auf deine Schwester')
        elif message.content.lower().startswith("ich liebe"):
            await message.channel.send('und ich liebe deine mutter du bastard')
        elif message.content.lower().startswith("Ich liebe"):
            await message.channel.send('und ich liebe deine mutter du bastard')
        elif message.content.lower().startswith("ich ficke"):
            await message.channel.send('hdf ich ficke gleich deine schwester')
        elif message.content.lower().startswith("I´m online bitches lesss go!"):
            await message.channel.send('mach mir nicht nach du hs')
        elif message.content.lower().startswith("unlustig"):
            await message.channel.send('wie deine geburt')
        elif message.content.lower().startswith("fuck nicht"):
            await message.channel.send('fuck du mal nicht ab')
        elif message.content.lower().startswith("geh wieder offline"):
            await message.channel.send('geh du mal offline')
        elif message.content.lower().startswith("unlustig!"):
            await message.channel.send('wie deine geburt')
        elif message.content.lower().startswith("unlustiger"):
            await message.channel.send('wie deine geburt')
        elif message.content.lower().startswith("bin ich gay"):
            z = random.randint(0,1)
            if z == 0:
                await message.channel.send('Ja bist du!')
            else:
                await message.channel.send('Ne kuss <3')
        elif message.content.lower().startswith("hab ich einen großen schwanz"):
            z = random.randint(0,1)
            if z == 0:
                await message.channel.send('Ja hast du kuss!')
            else:
                await message.channel.send('Ne nahkampfstachel')
        elif message.content.lower().startswith("hab ich einen großen schwanz?"):
            z = random.randint(0,1)
            if z == 0:
                await message.channel.send('Ja hast du kuss!')
            else:
                await message.channel.send('Ne nahkampfstachel')
        elif message.content.lower().startswith("hab ich einen fetten schwanz?"):
            z = random.randint(0,1)
            if z == 0:
                await message.channel.send('Ja hast du kuss!')
            else:
                await message.channel.send('Ne nahkampfstachel')
        elif message.content.lower().startswith("hab ich einen großen coc"):
            z = random.randint(0,1)
            if z == 0:
                await message.channel.send('Ja hast du kuss!')
            else:
                await message.channel.send('Ne nahkampfstachel')
        elif message.content.lower().startswith("hab ich einen großen cock"):
            z = random.randint(0,1)
            if z == 0:
                await message.channel.send('Ja hast du kuss!')
            else:
                await message.channel.send('Ne nahkampfstachel')
        elif message.content.lower().startswith("bin ich gay?"):
            z = random.randint(0,1)
            if z == 0:
                await message.channel.send('Ja bist du und jz hdf lass mich schlafen')
            else:
                await message.channel.send('Ne kuss <3')

client = MyClient()
client.run("ODQzODg4MTU2NzI1MzQ2NDAx.YKKaFw.qFW6ZcIRS_x2buc9jtfKOHV5J3U")
