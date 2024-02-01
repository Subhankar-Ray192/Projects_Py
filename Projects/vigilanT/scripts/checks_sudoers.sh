#!/bin/bash

# Check if the sudoers file exists
if [ ! -f /etc/sudoers ]; then
    echo "Error: Sudoers file not found."
    exit 1
fi


