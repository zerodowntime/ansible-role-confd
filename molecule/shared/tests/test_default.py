import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_confd_directories_are_in_correct_paths(host):
    command = host.command('ls /usr/bin')
    assert command.stdout.find('confd') > -1, "no binary for confd"
    command = host.command("ls -l /usr/bin/confd | awk '{print $1}'")
    assert command.stdout.find('rwxr-xr-x') > -1, "confd not executable"
    command = host.command('ls cd /usr/lib/systemd/system/')
    assert command.stdout.find('confd') > -1, "no unit for confd"
    command = host.command('ls /etc/confd')
    assert command.stdout.find('confd.toml') > -1, "no conf file"


def confd_is_enabled(host):
    command = host.command('systemctl is-enabled confd')
    assert command.stdout.find('enabled') > -1, "confd disabled"


def confd_is_active(host):
    command = host.command('systemctl is-active confd')
    assert command.stdout.find('active') > -1, "confd inactive"
