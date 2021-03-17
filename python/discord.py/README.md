# Contributing Discord.py Code

## General
- Specify any priviledged intents that are required
- Please use `@commands.command` (rather than `@bot.command`)
  for commands that aren't in a cog so that it can be used by
  anyone with least hassle using `bot.add_command`
- Ensure each command has appropriate permission checks for the user and bot
- Ensure all edge cases are handled and that you've actually tested the commands
