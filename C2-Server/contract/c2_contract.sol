// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract C2Research {

    struct Command {
        uint id;
        string cmd;
        string target;
    }

    Command[] public commands;

    function addCommand(string memory _cmd, string memory _target) public {
        commands.push(Command(commands.length, _cmd, _target));
    }

    function getCommand(uint index) public view returns(string memory, string memory){
        return (commands[index].cmd, commands[index].target);
    }

    function commandCount() public view returns(uint){
        return commands.length;
    }
}