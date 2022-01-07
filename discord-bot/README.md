# Discord bot

Deletes the contents of non-sensitive channels from the HeroCTF discord server.

## Installation

```bash
# Part I
$ git clone https://github.com/HeroCTF/heroctf-stack
$ cd heroctf-stack/discord-bot
$ echo 'TOKEN=XXXXX' > .env

# Part II
## With docker-compose
$ sudo docker-compose up -d

## With docker
$ sudo docker build . -t discord-bot
$ sudo docker run -t --rm discord-bot

## Directly on host
$ python3 -m pip install -r requirements.txt
$ python3 main.py
```

## Usage

### Commands

- `>clear_all` : Deletes the content of non-sensitive channels (required role : `Hero`).

## Made with

- [discord.py](https://discordpy.readthedocs.io/en/stable/)