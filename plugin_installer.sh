#!/bin/bash
#Check if correct arguments were provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 /path/to/plugins.txt @wp_cli_alias"
  exit 1
fi

# Set the path to the plugin file and WP CLI alias from arguments
PLUGIN_FILE="$1"
WP_ALIAS="$2"

# Check if plugin file exists
if [ ! -f "$PLUGIN_FILE" ]; then
  echo "Plugin file not found: $PLUGIN_FILE"
  exit 1
fi

echo "Content of $PLUGIN_FILE:"
cat "$PLUGIN_FILE"
echo ""

# Convert Windows line endings (CRLF) to Unix (LF), if necessary
sed -i 's/\r$//' "$PLUGIN_FILE"

# Read file into an array
IFS=$'\n' read -d '' -r -a plugins < "$PLUGIN_FILE"
for plugin in "${plugins[@]}"
do
  echo "Checking plugin - $plugin"

  # Check if the plugin is installed
  if wp @$WP_ALIAS plugin is-installed $plugin > /dev/null 2>&1; then
    echo "Plugin $plugin is already installed."
  else
    echo "Installing plugin: $plugin"
    if ! wp @$WP_ALIAS plugin install $plugin > /dev/null 2>&1; then
      echo "Failed to install plugin: $plugin"
    fi
  fi
done

echo "Script execution completed."
