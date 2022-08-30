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
