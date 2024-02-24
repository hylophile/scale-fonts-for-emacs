# Scale fonts for Emacs

Packages like [mixed-pitch](https://gitlab.com/jabranham/mixed-pitch) allow mixing fixed and variable pitch fonts in Emacs. But often, the variable pitch font tends to be too small compared to the fixed pitch font.

This script scales up the given font files by a given scale factor and appends `ScaledForEmacs` to the font family name. You need to have `fontforge` installed.

Usage: 
`./scale.py <scaling_factor> <font_files>`

Example: 
`./scale.py 1.2 myfont.ttf myotherfont.ttf`


