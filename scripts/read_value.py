from brownie import SimpleStorage,accounts,config

def read_contract():
    simple_storage = SimpleStorage[-1]
    print(simple_storage.get_fav_no())
def main():
    read_contract()