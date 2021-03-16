// Import Disord.js First
const Discord = require("discord.js");
// Now Define Client
const client = new Discord.Client();

// Now we're gonna define the prefix
const prefix = "?"; // You can change the prefix to anything

client.on("ready", () => {
  console.log(`${client.user.tag} is now Online!`);
});

client.on("message", (message) => {
  if (message.content === `${prefix}ping`) {
    message.channel.send(`Pong!: ${ws.ping}ms!`);
  } else if (message.content === `${prefix}reply`) {
    message.reply("Replied! :D");
  }
});

client.login("Put Discord Token Here"); // Put your Discord Bot token here
