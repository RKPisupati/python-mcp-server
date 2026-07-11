#!/bin/bash
set -e

ssh-keygen -A 2>/dev/null || true
chmod 700 /run/sshd 2>/dev/null || true

echo "PermitRootLogin no" >> /etc/ssh/sshd_config
echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config

echo "mcp:railway" | chpasswd 2>/dev/null || true

/usr/sbin/sshd -D &
wait
