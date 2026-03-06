pragma solidity ^0.8.0;

contract C2Command {

    string public command;

    function setCommand(string memory _cmd) public {
        command = _cmd;
    }

    function getCommand() public view returns (string memory) {
        return command;
    }
}