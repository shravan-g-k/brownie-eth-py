from brownie import accounts,config,SimpleStorage 
# import brownie
def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from" : account})
    stored_value = simple_storage.get_fav_no()
    print(stored_value)  
    transaction = simple_storage.set_fav_no(15,{"from":account})
    transaction.wait(1)
    updated_stored_value = simple_storage.get_fav_no()
    print(updated_stored_value)


def main():
    deploy_simple_storage()