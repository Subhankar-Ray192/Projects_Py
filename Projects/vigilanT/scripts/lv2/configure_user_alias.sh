Adding User_Alias 'USER' to sudoers file..."
echo "User_Alias USER = dummy" | sudo tee -a /etc/sudoers > /dev/null

echo "Adding User_Alias 'ADMIN' to sudoers file..."
echo "User_Alias ADMIN = dummy" | sudo tee -a /etc/sudoers > /dev/null