//Author:Tasfiqul Tapu
//Credits:
//    -https://www.npmjs.com/package/dotenv
//    -https://discordjs.guide
//Description:
//    -Using dotenv for storing configuration

// first of all rename .env-sample to .env and put your bot token and prefix
require("dotenv").config(); // configures .env
const Discord = require("discord.js"); //imports discord.js

const client = new Discord.Client(); // defines client
const prefix = process.env.PREFIX;

client.once("ready", () => {
  console.log(`${client.user.username} is up and running`);
});

//This is called everytime someone sends a message
client.on("message", message => {
  //Ignores any message if it doesn't start with the prefix or if a bot sends the message
  if (!message.content.startsWith(prefix) || message.author.bot) return;
  //Put your commands or command handler here
  //This is a simple ping command
  if (message.content.startsWith(`${prefix}ping`)) {
    message.channel.send(
      `🏓 Latency is ${Date.now() -
        message.createdTimestamp}ms. API Latency is ${Math.round(
        client.ws.ping
      )}ms`
    );
  }
});

client.login(process.env.BOTTOKEN); // Logs in
