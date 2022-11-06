from brownie import accounts
# import brownie
def deploy_simple_storage():
    account = accounts.load("eth-project")
    print(account)

def main():
    deploy_simple_storage()