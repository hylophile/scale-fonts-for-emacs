# Scale fonts for Emacs

Packages like [mixed-pitch](https://gitlab.com/jabranham/mixed-pitch) allow mixing fixed and variable pitch fonts in Emacs. But often, the variable pitch fonts tend to be too small. 

This script scales up the given font files by a given scale factor and appends `Emacs` to the font family name.

Usage: 
`./scale.py <scaling_factor> <font_files>`

Example: 
`./scale.py 1.2 myfont.ttf myotherfont.ttf`


