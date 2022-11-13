# finished on 9 Nov 2022
from brownie import accounts, config, SimpleStorage, network
from scripts.helpful import get_account


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.get_fav_no()
    print(stored_value)
    transaction = simple_storage.set_fav_no(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.get_fav_no()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
