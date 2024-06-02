#!/bin/bash
command=${1:-"up -d"}
sops exec-env .secret/homelab-notifier.enc.json "docker compose $command"
