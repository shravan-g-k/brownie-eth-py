from brownie import FundMe, network, config
from scripts.deploy import get_account


def deploy_fund_me():
    # get the account from local ganache or goerli network
    account = get_account()
    if network.show_active() != "development":
        price_feed_address = config["network"][network.show_active()][
            "eth_usd_price_feed"
        ]
    

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=True,
    )
    print(f"Contract Deployed to {fund_me.address}")


def main():
    deploy_fund_me()
