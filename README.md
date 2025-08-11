    

 ______   __  __     __  __     __  __        ______     __    __     ______       __     __     ______    
/\  ___\ /\_\_\_\   /\_\_\_\   /\_\_\_\      /\  ___\   /\ "-./  \   /\  __ \     /\ \   /\ \   /\  ___\   
\ \  __\ \/_/\_\/_  \/_/\_\/_  \/_/\_\/_     \ \  __\   \ \ \-./\ \  \ \ \/\ \   _\_\ \  \ \ \  \ \___  \  
 \ \_\     /\_\/\_\   /\_\/\_\   /\_\/\_\     \ \_____\  \ \_\ \ \_\  \ \_____\ /\_____\  \ \_\  \/\_____\ 
  \/_/     \/_/\/_/   \/_/\/_/   \/_/\/_/      \/_____/   \/_/  \/_/   \/_____/ \/_____/   \/_/   \/_____/ 
                                                                                                           
                                                 

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
