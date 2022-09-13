# Installs a python command locally
# ---------------------------------
# Creates a small shell script under ~/.local/bin to launch the python module


# CONFIGURATION
COMMAND_NAME="pbaygtk"
REQUIREMENTS="pygobject requests datasize"


rm ~/.local/bin/$COMMAND_NAME
pip uninstall $REQUIREMENTS
rm ~/.local/share/icons/$COMMAND_NAME.png
rm ~/.local/share/applications/$COMMAND_NAME.desktop
