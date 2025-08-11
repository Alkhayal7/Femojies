            
            ███████╗▄▄███▄▄· ██████╗  ██╗ ██╗     ███████╗███╗   ███╗ ██████╗      ██╗██╗███████╗
            ██╔════╝██╔════╝██╔═══██╗████████╗    ██╔════╝████╗ ████║██╔═══██╗     ██║██║██╔════╝
            █████╗  ███████╗██║██╗██║╚██╔═██╔╝    █████╗  ██╔████╔██║██║   ██║     ██║██║███████╗
            ██╔══╝  ╚════██║██║██║██║████████╗    ██╔══╝  ██║╚██╔╝██║██║   ██║██   ██║██║╚════██║
            ██║     ███████║╚█║████╔╝╚██╔═██╔╝    ███████╗██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║███████║
            ╚═╝     ╚═▀▀▀══╝ ╚╝╚═══╝  ╚═╝ ╚═╝     ╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝╚══════╝
                                                                                                


Removes all emojis from files.

## Usage

```bash
# Process current directory
python femojis.py

# Process specific files
python femojis.py file1.txt file2.py

# Process specific directories
python femojis.py /path/to/dir1 /path/to/dir2

# Mix files and directories
python femojis.py file1.txt /path/to/directory file2.py
```

## What it does

- Scans text files (skips binary files and hidden directories)
- Removes all Unicode emoji characters
- Overwrites original files
- Shows count of emojis destroyed per file

## Requirements

Python 3.6+
