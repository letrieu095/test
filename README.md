# README

## Overview

A basic program send and receive messages between client & server.

Written in [Python](https://www.python.org/)

## Prerequisites

- Must have superuser privileges on server machine that will run program.
- [docker](https://www.docker.com/) & [docker-compose](https://docs.docker.com/compose/) installed on server machine.

## Deployment

- Add IP address in `deployment/hosts` file.
- Run: 

```bash 
$ ansible-playbook -i deployment/hosts deployment/site.yml -u <user> -l <ip_host/group> -t <client/server>
```