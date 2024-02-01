#!/bin/bash

# Check if the sudoers file exists
if [ ! -f /etc/sudoers ]; then
    echo "Error: Sudoers file not found."
    exit 1
fi

# Check if the required aliases are defined in the sudoers file
if grep -qE '^\s*User\s*,\s*Admin\s*,\s*Default\s*=' /etc/sudoers; then
    echo "Required aliases (User, Admin, Default) found in sudoers file."
else
    echo "Required aliases (User, Admin, Default) not found in sudoers file."
fi
