# Installs a python command locally
# ---------------------------------
# Creates a small shell script under ~/.local/bin to launch the python module


# CONFIGURATION
COMMAND_NAME="pbaygtk"
REQUIREMENTS="pygobject requests datasize"


set -e
pip install $REQUIREMENTS
mkdir -p ~/.local/bin
cat << EOF > ~/.local/bin/$COMMAND_NAME
#!/bin/bash
python3 $PWD/$COMMAND_NAME @?
EOF
chmod +x ~/.local/bin/$COMMAND_NAME
mkdir -p ~/.local/share/applications
mkdir -p ~/.local/share/icons
cp icon.png ~/.local/share/icons/$COMMAND_NAME.png
cat > ~/.local/share/applications/$COMMAND_NAME.desktop << EOF 
[Desktop Entry]
Type = Application
Name = $COMMAND_NAME
Exec = python3 $PWD/$COMMAND_NAME
Icon = $COMMAND_NAME
EOF
