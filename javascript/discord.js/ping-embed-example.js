//Author:Tasfiqul Tapu
//Credits:
//    -https://stackoverflow.com/questions/63411268/discord-js-ping-command
//    -https://discordjs.guide
//Description:
//    -A ping command with latency and embed
//Node-modules:
//    - discord.js ^12
//Try it here: https://glitch.com/edit/#!/ping-embed-example

const Discord = require("discord.js"); //imports discord.js
const client = new Discord.Client(); // defines client
// Add your bot prefix here
const prefix = "!";

//This happens once when your bot boots up
client.once("ready", () => {
  console.log(`${client.user.username} is up and running`);
});

//This is called everytime someone sends a message
client.on("message", message => {
  //Ignores any message if it doesn't start with the prefix or if a bot sends the message
  if (!message.content.startsWith(prefix) || message.author.bot) return;
  //This is the ping command
  if (message.content.startsWith(`${prefix}ping`)) {
    //Start a new embed
    const embed = new Discord.MessageEmbed();
    embed.setColor("WHITE"); // Put your embed color
    embed.setTitle("**Ping Pong**🏓"); //Put embed title here
    // Date.now is the time bot receives the message and message.createdTimestamp is the time user used the command and client.ws.ping is websocket delay
    embed.setDescription(
      `Latency is ${Date.now() -
        message.createdTimestamp}ms. API Latency is ${Math.round(
        client.ws.ping
      )}ms`
    );
    message.channel.send(embed); //sends the embed
  }
});

client.login("BOTTOKEN"); // Put your bot token here
