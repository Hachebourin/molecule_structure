import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_service(host):
    services = ['httpd']
    for s in services:
        service = host.service(s)
        assert not service.is_running


def test_installed_pkg(host):
    assert not host.package('httpd').is_installed


def test_installed_config(host):
    files = ['index.html']
    for conf in files:
        f = host.file('/var/www/html/' + conf)
        assert not f.exists
