#!/bin/bash

# Check if the sudoers file exists
if [ ! -f /etc/sudoers ]; then
    echo "Error: Sudoers file not found."
    exit 1
fi

# Check if the required aliases are defined in the sudoers file
if sudo grep -qE '^User_Alias' /etc/sudoers; then
    echo "User_Alias found in sudoers file."
else
    echo "User_Alias not found in sudoers file."
fi
