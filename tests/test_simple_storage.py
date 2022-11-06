from brownie import accounts,SimpleStorage

def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from" : account})
    start_value = simple_storage.get_fav_no()
    expect_value = 0
    assert start_value == expect_value

def text_updating_fav_no():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from" : account})
    value = 1
    simple_storage.set_fav_no(value,{"from" : account})
    assert simple_storage.get_fav_no() == value