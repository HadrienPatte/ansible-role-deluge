import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    ('deluged'),
])
def test_package_is_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize('name', [
    ('deluged'),
])
def test_service_is_running(host, name):
    service = host.service(name)
    assert service.is_running


@pytest.mark.parametrize('name', [
    ('deluged'),
])
def test_service_is_enabled(host, name):
    service = host.service(name)
    assert service.is_enabled


@pytest.mark.parametrize('directory', [
    ('/var/lib/deluged'),
    ('/var/lib/deluged/config'),
    ('/var/log/deluged'),
])
def test_directory(host, directory):
    directory = host.file(directory)
    assert directory.exists
    assert directory.is_directory
    assert directory.user == 'deluge'
    assert directory.group == 'deluge'
