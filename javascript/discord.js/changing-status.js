//Author:Tasfiqul Tapu
//Credits:
//    -https://stackoverflow.com/questions/55095596/discord-bot-status-from-playing-to-watching/55097604
//    -https://stackoverflow.com/questions/49286640/how-to-set-bots-status
//Description:
//    -Changing custom status

// importing discord.js and defining client
const Discord = require("discord.js");
const client = new Discord.Client();

//changing status
client.on("ready", () => {
  //set how often the status changes(in milliseconds)
  const refresh = 30000;

  //put all your statuses here , Format: [activity,type]
  const status = [
    ["with dog", "PLAYING"],
    ["in the rain", "PLAYING"],
    ["time pass away", "WATCHING"],
    ["clouds float away", "WATCHING"],
    ["starts fall", "WATCHING"],
    ["birds chirping", "LISTENING"],
    ["some jam", "LISTENING"],
    ["life", "STREMING"],
  ];

  //sets a random activity every `refresh` ms
  setInterval(() => {
    const i = Math.floor(Math.random() * (status.length - 1));
    client.user.setActivity(status[i][0], {
      type: status[i][1],
    });
  }, refresh);
});

// logs the bot in
client.login(process.env.BOTTOKEN);
