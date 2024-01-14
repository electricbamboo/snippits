#### WP CLI Plugin Installer

So I got tired of being handed X # of new sites and having to manually install all the same plugins across of them.

1) Create your plugins.txt file.
   Each plugin needs to be the wp-cli name (what you get when you go
   ```
   wp @yoursitealias plugin list
   ```
   One per line!
2) Make sure you give the .sh file execute permissions
   ```
   chmod +x plugin_installer.sh
   ```
3) Go nuts:
   ./plugin_installer /path/to/plugins.txt yoursitealias
