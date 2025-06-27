#!/data/data/com.termux/files/usr/bin/bash

# Install Zsh
pkg update -y && pkg install -y zsh wget git curl

# Install Zsh4Humans
sh -c "$(wget -O- https://raw.githubusercontent.com/romkatv/zsh4humans/v5/install)"

# Set Zsh as default shell in Termux
echo 'exec zsh' >> ~/.bashrc

# Suppress Termux welcome message
touch ~/.hushlogin

# Optional: Clear screen on Zsh startup
echo 'clear' >> ~/.zshrc

echo "✅ Zsh4Humans has been installed."
echo "✅ Zsh has been set as the default shell for Termux."
echo "📌 Please restart Termux or run: exec zsh"
