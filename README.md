Ansible Role: Postman
=====================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-postman.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-postman)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.postman-blue.svg)](https://galaxy.ansible.com/gantsign/postman)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-postman/master/LICENSE)

Role to download and install the [Postman](https://www.getpostman.com) HTTP
tool.

Requirements
------------

* Ansible

    * Minimum 2.4

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Xenial (16.04)
            * Bionic (18.04)

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# URL to download the Postman redistributable package from
postman_redis_url: 'https://dl.pstmn.io/download/latest/linux?arch=64'

# Base installation directory for the Postman distribution
postman_install_dir: '/opt/Postman'

# Directory to store files downloaded for the Postman installation
postman_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - role: gantsign.postman
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
