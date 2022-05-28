# Expected eth for entry => 0.0284079610470038 eth => 28407961047003800 wei (approx.)=> 28000000000000000

from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_getEntraceFee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_pricefeed"],
        {"from": account},
    )
    # assert lottery.getEntranceFee() > Web3.toWei(0.028, "ether")
    # assert lottery.getEntranceFee() < Web3.toWei(0.029, "ether")
