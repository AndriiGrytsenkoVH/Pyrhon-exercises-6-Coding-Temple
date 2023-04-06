# Description
Exercises for Python in Coding Temple
## Technologies
- Python (Jupyter)
## Focus topics
- class inheritance
- Python modules
- gitignore
## What I've learned:
> \__pycache__ holds precompiled module to speed up further imports. \__all__ name specifies all the package names in the module to be used when saying " from module import * ". imports inside \__init__.py expand the namespace making access more convenient at the expense of increasing the risk of potential conflicts. Finally, dir() lists all available names to the module specified. Modules are passed as names, not as strings to the dir(). If you pass in a string it will give you all the string methods. Sneaky and confusing, just the way I like it...