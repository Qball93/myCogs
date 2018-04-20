import discord
from discord.ext import commands
import discord.ext
import random
import aiohttp

#
#
##
#
#
##

class r_Management():
    def __init__(self, bot):
        self.bot = bot
       
  

    #@Client.event
    async def on_member_join(self, new_user):
        """Automatically add roles"""

        
        server_list = new_user.server.roles

        await self.bot.add_roles(new_user, discord.utils.get(server_list, name='sub human'), discord.utils.get(server_list, name='testrole'))



    @commands.command(pass_context=True)
    async def assign(self, ctx, new_role):
        """adds new roles to user, role is case sensitive"""
        is_role = False

        User = ctx.message.author

        server_roles = ctx.message.server.roles

        temp_list =[] 
        new_role = new_role.lower()


        if new_role == "second squeakers" or new_role == "king squeaker":
            await self.bot.say(f"{User.mention} stop being such a faggot")
            return

        for n in server_roles:
            if new_role == n.name.lower():
                await self.bot.add_roles(User, n)
                is_role = True
                for p in User.roles:
                    if p.is_everyone != True:
                        temp_list.append(p.name)
                    else:
                        pass

                await self.bot.say(f"these are your roles {temp_list} ")
            
        if is_role == False:
            await self.bot.say("role does not exist or it is mispelled")
            return
      

        

        


    @commands.command(pass_context=True)
    async def removeRole(self, ctx, old_role):
        """deletes a role"""
        is_role = False

        old_role = old_role.lower()

        User = ctx.message.author

        temp_list =[] 


        for n in User.roles:
            if old_role == n.name.lower():
                await self.bot.remove_roles(User, n)
                is_role = True
                for p in User.roles:
                    if p.is_everyone != True:
                        temp_list.append(p.name)
                    else:
                        pass

                await self.bot.say(f"these are your current roles {temp_list} ")
            
        if is_role == False:
            await self.bot.say("You didn't have that role faggot, or its mispelled (brainlet) ")
            return



class Jokes:
    def __init__(self, bot):
        self.bot = bot     

    @commands.command()
    async def joke(self, *args):
        """this makes some cringey dad joke"""

        #Your code will go here
 
   
        if args:
            url = "https://icanhazdadjoke.com/search"
            search_term = args[0]

            async with aiohttp.get(url, 
            headers={"Accept": "application/json"},
            params={"term":search_term}
            ).json() as res:

                if(res["total_jokes"] < 1):
                    await self.bot.say("there are no jokes of that topic")
                    #print("there are no jokes of that topic")

                else:
                    rand_int = (random.randint(0,len(res['results'])-1))
                    await self.bot.say(res['results'][rand_int]['joke'])
                    #print(res['results'][rand_int]['joke'])
        
        else:
            url = "https://www.icanhazdadjoke.com"
            async with aiohttp.get(url, headers={"Accept": "application/json"}) as response:
                data = await response.json()

                await self.bot.say(data["joke"])


    @commands.command()
    async def Hello(self):
        """Special greeting from the bot"""

        await self.bot.say("The fuck do you want faggot?")
       

        

def setup(bot):
    bot.add_cog(r_Management(bot))
    bot.add_cog(Jokes(bot))
