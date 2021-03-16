# Contributing Python Code

## General

- Make sure all required libraries are imported
- Specify requirements if any

## Code Quality

- Code must follow [PEP8](https://www.python.org/dev/peps/pep-0008/). This repository uses [`flake8`](https://flake8.pycqa.org/en/latest/) to check code format.   
  Here are some good tools to help with formatting:
  - [`flake8`](https://flake8.pycqa.org/en/latest/): checks your code for formatting errors
  - [`black`](https://pypi.org/project/black): automatically formats your code. 
  - [`isort`](https://pypi.org/project/isort): automatically formats your imports.
- These can be installed using `python3 -m pip install -r python/requirements-dev.txt` (from repo root)
- `noqa` may be used but is not encouraged. Only use it if 100% neccesary.

## Discord.py Checklist

- Specify any priviledged intents that are required
- Please use `@commands.command` (rather than `@bot.command`)
  for commands that aren't in a cog so that it can be used by
  anyone with least hassle using `bot.add_command`
- Ensure each command has appropriate permission checks for the user and bot
- Ensure all edge cases are handled and that you've actually tested the commands
