from brownie import FundMe, network, config, MockV3Aggregator
from scripts.deploy import get_account


def deploy_fund_me():
    # get the account from local ganache or goerli network
    account = get_account()
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"We are on network {network.show_active()}")
        print("Deploying Mocks")
        mock_aggregator = MockV3Aggregator.deploy(
            18, 20000000000000000000000, {"from": account}
        )
        price_feed_address = mock_aggregator.address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract Deployed to {fund_me.address}")


def main():
    deploy_fund_me()
