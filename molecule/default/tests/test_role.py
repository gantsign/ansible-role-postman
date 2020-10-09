def test_gitkraken(host):
    assert host.run('which Postman').rc == 0
