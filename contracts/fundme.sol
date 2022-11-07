//SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    mapping(address => uint256) public mapAddressToValue;
    address public owner;
    address[] public funders;

    constructor() {
        owner = msg.sender;
    }

    function fundMe() public payable {
        require(msg.value > 650000000000000, "Spend at least 50 Usd");
        mapAddressToValue[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e
        );
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e
        );
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer);
    }

    function getConversionRate(uint256 ethAmt) public view returns (uint256) {
        uint256 ethPrice = getPrice();
        uint256 ethAmtInUSD = (ethPrice * ethAmt) / 1000000000000000000;
        return ethAmtInUSD;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function withdraw() public payable onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
        for (
            uint256 funderIndx = 0;
            funderIndx < funders.length;
            funderIndx++
        ) {
            address funder = funders[funderIndx];
            mapAddressToValue[funder] = 0;
        }
        funders = new address[](0);
    }
}
