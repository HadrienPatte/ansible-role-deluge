# Ansible Role: Deluge

[![Build Status](https://travis-ci.com/HadrienPatte/ansible-role-deluge.svg?branch=master)](https://travis-ci.com/HadrienPatte/ansible-role-deluge)

An Ansible role that installs the deluge bittorrent client on Debian.

## Requirements

None.

## Role Variables

* `deluge_user`: name of the system user that runs deluge, defaults to `deluge`
* `deluge_group`: group of the system user that runs deluge, defaults to
  `deluge`

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
