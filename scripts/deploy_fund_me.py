from brownie import FundMe, network, config, MockV3Aggregator
from web3 import Web3
from scripts.helpful import deploy_mocks, get_account,LOCAL_BLOCKACHAIN_ENVIRONMENTS


def deploy_fund_me():
    # get the account from local ganache or goerli network
    account = get_account()
    if network.show_active() not in  LOCAL_BLOCKACHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract Deployed to {fund_me.address}")


def main():
    deploy_fund_me()
