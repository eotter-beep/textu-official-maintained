import click
import os

@click.group()
def main():
    pass

@main.command()
@click.argument('content')
@click.argument('name')
def write(content, name):
    remove = False
    if content.startswith("-"):
        remove = True
        content = content[1:]  # Strip the leading '-'

    # Read existing lines if the file exists
    if os.path.exists(name):
        with open(name, "r") as f:
            lines = f.readlines()
    else:
        lines = []

    if remove:
        # Remove lines containing content
        lines = [line for line in lines if content not in line]
    else:
        # Add new content with a newline
        lines.append(content + "\n")

    # Write the updated content back to the file
    with open(name, "w") as f:
        f.writelines(lines)
    
if __name__ == '__main__':
    main()
