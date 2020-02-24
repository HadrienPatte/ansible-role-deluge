# Ansible Role: Deluge

[![Build Status](https://travis-ci.com/HadrienPatte/ansible-role-deluge.svg?branch=master)](https://travis-ci.com/HadrienPatte/ansible-role-deluge)

An Ansible role that installs the deluge bittorrent client on Debian.

## Requirements

None.

## Role Variables

None.

# Dependencies

None.

# Example Playbook

```yaml
- name: Install and configure Deluge
  hosts: all
  roles:
    - hadrienpatte.deluge
```

## License

MIT

## Author Information

Hadrien Patte [![PGP 0xFB500BB0](https://peegeepee.com/badge/orange/FB500BB0.svg)](https://peegeepee.com/FB500BB0)
