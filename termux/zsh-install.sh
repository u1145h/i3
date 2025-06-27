# Install zsh4humans
sh -c "$(wget -O- https://raw.githubusercontent.com/romkatv/zsh4humans/v5/install)"

# Set Zsh as default on Termux by appending to .bashrc
echo 'exec zsh' >> ~/.bashrc

# Suppress Termux welcome message
touch ~/.hushlogin

# Optional: clear the screen on zsh startup
echo 'clear' >> ~/.zshrc

echo "✅ zsh4humans has been installed and set as the default shell."
echo "📌 Restart Termux or run: exec zsh"
