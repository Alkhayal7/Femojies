import argparse
import os
import sys
from pathlib import Path

EMOJI_RANGES = [
    (0x1F600, 0x1F64F), (0x1F300, 0x1F5FF), (0x1F680, 0x1F6FF), (0x1F1E0, 0x1F1FF),
    (0x2600, 0x26FF), (0x2700, 0x27BF), (0x1F900, 0x1F9FF), (0x1FA70, 0x1FAFF),
    (0x231A, 0x231B), (0x2328, 0x2328), (0x23E9, 0x23F3), (0x23F8, 0x23FA),
    (0x2B05, 0x2B07), (0x2B1B, 0x2B1C), (0x2B50, 0x2B55), (0x3030, 0x3030),
    (0x303D, 0x303D), (0x3297, 0x3299), (0xFE0F, 0xFE0F), (0x200D, 0x200D),
]


def validate_path(path_str):
    """Validate that a path exists and is accessible"""
    try:
        path = Path(path_str).resolve()
    except (OSError, ValueError) as e:
        print(f"Error: Invalid path '{path_str}': {e}")
        return False

    if not path.exists():
        print(f"Error: Path '{path_str}' does not exist.")
        return False

    try:
        if not os.access(path, os.R_OK):
            print(f"Error: Path '{path_str}' is not readable.")
            return False
    except OSError as e:
        print(f"Error: Cannot access path '{path_str}': {e}")
        return False

    return True


def remove_emojis_from_text(text):
    emoji_count = 0
    cleaned_chars = []

    for char in text:
        char_code = ord(char)
        is_emoji = False

        for start, end in EMOJI_RANGES:
            if start <= char_code <= end:
                is_emoji = True
                emoji_count += 1
                break
        if not is_emoji:
            cleaned_chars.append(char)

    cleaned_text = "".join(cleaned_chars)
    return cleaned_text, emoji_count


def should_process_file(file_path):
    if any(part.startswith(".") for part in file_path.parts):
        return False
    binary_extensions = {
        ".exe",
        ".bin",
        ".dll",
        ".so",
        ".dylib",
        ".a",
        ".lib",
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".ico",
        ".svg",
        ".mp3",
        ".mp4",
        ".avi",
        ".mov",
        ".wav",
        ".flac",
        ".zip",
        ".tar",
        ".gz",
        ".rar",
        ".7z",
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".pyc",
        ".pyo",
        ".pyd",
        ".whl",
    }

    if file_path.suffix.lower() in binary_extensions:
        return False

    # Try to detect if file is text-based
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            # Read first 1024 bytes to check if it's text
            sample = f.read(1024)
            # If we can read it and it doesn't contain too many null bytes, it's probably text
            null_ratio = sample.count("\x00") / len(sample) if sample else 0
            return null_ratio < 0.1
    except (OSError, IOError, UnicodeError, PermissionError):
        return False


def destroy_emojis_in_file(file_path):
    """Process a single file and destroy emojis"""
    try:
        # Read file content
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            original_content = f.read()

        # Remove emojis
        cleaned_content, emoji_count = remove_emojis_from_text(original_content)

        # Only write back if emojis were found
        if emoji_count > 0:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(cleaned_content)

            print(f"Destroyed {emoji_count} emojis in {file_path}")

        return emoji_count, 1

    except PermissionError:
        print(f"Skipped {file_path}: Permission denied")
    except UnicodeError:
        print(f"Skipped {file_path}: Encoding error")
    except OSError as e:
        print(f"Skipped {file_path}: {e}")
    except IOError as e:
        print(f"Skipped {file_path}: File I/O error - {e}")

    return 0, 0


def destroy_emojis_in_directory(directory_path):
    """Crawl directory and destroy all emojis"""
    root = Path(directory_path)
    total_emojis_destroyed = 0
    files_processed = 0

    print(f"Scanning directory: {directory_path}")

    for file_path in root.rglob("*"):
        if file_path.is_file() and should_process_file(file_path):
            emoji_count, processed = destroy_emojis_in_file(file_path)
            total_emojis_destroyed += emoji_count
            files_processed += processed

    return total_emojis_destroyed, files_processed


def destroy_emojis_in_paths(paths):
    """Process multiple paths (files and directories)"""
    total_emojis_destroyed = 0
    files_processed = 0

    print("Starting emoji destruction mission...")

    for path_str in paths:
        path = Path(path_str)

        if path.is_file():
            if should_process_file(path):
                print(f"Processing file: {path}")
                emoji_count, processed = destroy_emojis_in_file(path)
                total_emojis_destroyed += emoji_count
                files_processed += processed
            else:
                print(f"Skipped {path}: Not a processable text file")
        elif path.is_dir():
            emoji_count, processed = destroy_emojis_in_directory(path)
            total_emojis_destroyed += emoji_count
            files_processed += processed

    return total_emojis_destroyed, files_processed


def print_ascii():
    """Print beautiful ASCII art victory message"""
    ascii_art = """
    
    ███████╗ ██╗ ██╗  ██████╗ ▄▄███▄▄·    ███████╗███╗   ███╗ ██████╗      ██╗██╗███████╗
    ██╔════╝████████╗██╔═══██╗██╔════╝    ██╔════╝████╗ ████║██╔═══██╗     ██║██║██╔════╝
    █████╗  ╚██╔═██╔╝██║██╗██║███████╗    █████╗  ██╔████╔██║██║   ██║     ██║██║███████╗
    ██╔══╝  ████████╗██║██║██║╚════██║    ██╔══╝  ██║╚██╔╝██║██║   ██║██   ██║██║╚════██║
    ██║     ╚██╔═██╔╝╚█║████╔╝███████║    ███████╗██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║███████║
    ╚═╝      ╚═╝ ╚═╝  ╚╝╚═══╝ ╚═▀▀▀══╝    ╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝╚══════╝
                                                                                        
    """
    print(ascii_art)


def main():
    """Main function to run the emoji destroyer"""
    try:
        # Create argument parser
        parser = argparse.ArgumentParser(
            description="Emoji Destroyer - Eliminate ALL emojis from your project",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="Because sometimes you just need to say F$@# EMOJIS!",
        )

        parser.add_argument(
            "paths",
            nargs="*",
            default=["."],
            help="Target files and/or directories to process (default: current directory)",
        )

        # Parse arguments
        try:
            args = parser.parse_args()
        except SystemExit as e:
            # argparse calls sys.exit on error, we catch it to handle gracefully
            if e.code != 0:
                sys.exit(2)  # Exit code 2 for invalid arguments
            raise

        # Validate all paths
        for path_str in args.paths:
            if not validate_path(path_str):
                sys.exit(1)  # Exit code 1 for invalid path

        # Display target paths
        print("Target paths:")
        for path_str in args.paths:
            try:
                abs_path = os.path.abspath(path_str)
                path_type = "file" if Path(path_str).is_file() else "directory"
                print(f"  {abs_path} ({path_type})")
            except (OSError, ValueError) as e:
                print(f"Error: Cannot resolve path '{path_str}': {e}")
                sys.exit(1)

        # Confirm destruction
        try:
            response = input("\nAre you sure you want to DESTROY all emojis? (Y/n): ")
        except (EOFError, KeyboardInterrupt):
            print("\nMission aborted.")
            sys.exit(0)

        if response.lower() == "n":
            print("Mission aborted.")
            return

        # Execute the destruction
        try:
            total_destroyed, files_processed = destroy_emojis_in_paths(args.paths)
        except KeyboardInterrupt:
            print("\nOperation interrupted by user.")
            sys.exit(130)  # Standard exit code for SIGINT
        except OSError as e:
            print(f"Error: Cannot access target paths: {e}")
            sys.exit(1)

        # Victory report
        print(f"Files processed: {files_processed}")
        print(f"Total emojis destroyed: {total_destroyed}")

        print_ascii()

    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
        sys.exit(130)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
