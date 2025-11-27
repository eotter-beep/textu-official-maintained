"""
textu

Description:
This script provides a command-line interface (CLI) to add or remove lines
in a text file using the 'click' library.

Requirements:
- Python 3.x
- click library (install with: pip install click)

Usage:

Command Structure:
    python script_name.py <command> <arguments>

Commands:

write
    Adds or removes a line in a specified text file.

    Arguments:
    1. content - The text to add or remove.
       - To remove a line, prefix the content with '-'.
         Example: -line to remove
    2. name - The name of the file to modify.

Examples:

    Add a line:
        python script_name.py write "Hello World" myfile.txt

    Remove a line:
        python script_name.py write "-Hello World" myfile.txt

Notes:
- If the file does not exist, it will be created when adding a new line.
- Removing a line only removes lines that contain the specified content.
"""
