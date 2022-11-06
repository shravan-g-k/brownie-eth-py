from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.get_fav_no()
    print(stored_value)
    transaction = simple_storage.set_fav_no(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.get_fav_no()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "devlopment":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["key"])


def main():
    deploy_simple_storage()
