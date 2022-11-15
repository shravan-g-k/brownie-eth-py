from brownie import Token
from scripts.helpfulscripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000,"ether")

def main():
    account = get_account()
    our_token = Token.deploy(initial_supply,{"from":account})
    print(our_token.name())
 