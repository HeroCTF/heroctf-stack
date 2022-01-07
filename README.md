# HeroCTF stack

List of self-hosted projects.

## Projects

- [discord-bot](discord-bot) : A Discord bot that helps us to reinitialize the Discord server after a CTF.
- [nextcloud](nextcloud) : Project management and self hosting.
- [nginx](nginx) : Acts as a reverse-proxy in front of all web applications exposed to the web.

## Installation

Each project contains a `docker-compose.yml` file. You can run each of them using `docker-compose up -d`.

You can also use a simple bash script to do it :

```bash
$ git clone https://github.com/HeroCTF/heroctf-stack.git
$ cd heroctf-stack
$ bash install.sh
```