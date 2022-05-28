from brownie import (
    network,
    config,
    accounts,
    MockV3Aggregator,
    VRFCoordinatorMock,
    LinkToken,
    Contract,
)
from web3 import Web3


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]


DECIMALS = 8
STARTING_PRICE = 200000000000


contract_to_mock = {
    "eth_usd_price_feed": MockV3Aggregator,
    "vrf_coordinator": VRFCoordinatorMock,
    "link_token": LinkToken,
}


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])


def deploy_mocks(decimals=DECIMALS, initial_value=STARTING_PRICE):
    print("Deploying Mocks...")
    account = get_account()
    mock_price_feed = MockV3Aggregator.deploy(
        decimals, initial_value, {"from": get_account()}
    )
    link_token = LinkToken.deploy({"from": account})
    VRFCoordinatorMock.deploy(link_token.address, {"from": account})
    print("Mocks deployed!")


def get_contract(contract_name):
    """
    This function will grab the contract addresses from the brownie config if defined, otherwise,
    it will deploy a mock version of that contract and return that

    Args: contract_name (string)
    Returns:brownie.network.contract.ProjectContract
    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:  # Checks if a MockV3Aggregator has been deployed
            deploy_mocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract
