//SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    uint256 public fav_no;
    People[] public people;

    mapping(string => uint256) public nametoage;

    struct People {
        uint256 age;
        string name;
    }

    function set_fav_no(uint256 n) public  returns(uint256) {
        fav_no = n;
        return fav_no;
    }

    function get_fav_no() public view returns (uint256) {
        // fav_no = fav_no+fav_no;
        return fav_no;
    }

    function addpeople(uint256 _age, string memory _name) public {
        people.push(People(_age, _name));
        nametoage[_name] = _age;
    }


}
