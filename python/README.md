# Contributing Python Code

## General

- Make sure all required libraries are imported
- Specify requirements if any

## Code Quality

- Code must be formatted with [`black`](https://pypi.org/project/black)
- Imports must be sorted with [`isort`](https://pypi.org/project/isort)
- These can be installed using `python3 -m pip install -r python/requirements-dev.txt` (from repo root)

## Discord.py Checklist

- Specify any priviledged intents that are required
- Please use `@commands.command` (rather than `@bot.command`)
  for commands that aren't in a cog so that it can be used by
  anyone with least hassle using `bot.add_command`
- Ensure each command has appropriate permission checks for the user and bot
- Ensure all edge cases are handled and that you've actually tested the commands
