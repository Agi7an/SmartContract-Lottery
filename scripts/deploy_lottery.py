from scripts.support_functions import get_account, get_contract
from brownie import Lottery, config, network


def deploy_lottery():
    account = get_account(id="Aylan")
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("DEPLOYED LOTTERY!")


def main():
    deploy_lottery()