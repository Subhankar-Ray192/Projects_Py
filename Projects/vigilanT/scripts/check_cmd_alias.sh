#!/bin/bash

# Check if the required aliases are defined in the sudoers file
if sudo grep -qE '^Cmd_Alias' /etc/sudoers; then
    echo "Cmd_Alias found in sudoers file."
else
    echo "Cmd_Alias not found in sudoers file."
fi