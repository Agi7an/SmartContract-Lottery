// SPDX-License-Identifier: MIT

pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract Lottery {
    // address payable is a data type that gives additional functionality to the stored user address such asuser.send(), user.transfer() and user.call()
    address payable[] public players;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethusdPriceFeed;

    constructor(address _priceFeedAddress) public {
        usdEntryFee = 50 * 10**18;
        ethusdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    function enter() public payable {
        players.push(msg.sender);
    }

    function getEntranceFee() public view returns (uint256) {}

    function startLottery() public {}

    function endLottery() public {}
}
