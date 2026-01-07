"""
Utility functions module
"""
from pathlib import Path
from typing import List, Optional


def collect_torrent_files(
    input_path: Path, 
    recursive: bool = False,
    case_sensitive: bool = False
) -> List[Path]:
    """
    Collect torrent files
    
    Args:
        input_path: Input path (file or directory)
        recursive: Whether to recursively search subdirectories
        case_sensitive: Whether to be case-sensitive
        
    Returns:
        List of torrent file paths
    """
    torrent_files = []
    
    if input_path.is_file():
        # Single file
        suffix = input_path.suffix.lower() if not case_sensitive else input_path.suffix
        if suffix == '.torrent':
            torrent_files.append(input_path)
    elif input_path.is_dir():
        # Directory
        if recursive:
            # Recursive search
            pattern = '**/*.torrent' if not case_sensitive else '**/*.TORRENT'
            torrent_files.extend(list(input_path.glob(pattern)))
            if case_sensitive:
                torrent_files.extend(list(input_path.glob('**/*.torrent')))
        else:
            # Current directory only
            torrent_files.extend(list(input_path.glob('*.torrent')))
            torrent_files.extend(list(input_path.glob('*.TORRENT')))
    
    # Remove duplicates and sort
    torrent_files = sorted(set(torrent_files))
    return torrent_files


def get_output_path(
    input_path: Path,
    output_path: Optional[Path] = None,
    default_name: str = "magnet_links.txt"
) -> Path:
    """
    Determine output file path
    
    Args:
        input_path: Input path
        output_path: User-specified output path
        default_name: Default output file name
        
    Returns:
        Output file path
    """
    if output_path:
        # If specified path is a directory, add default filename
        if output_path.is_dir() or (not output_path.suffix and not output_path.exists()):
            return output_path / default_name
        return output_path
    
    # Auto-determine output path
    if input_path.is_dir():
        return input_path / default_name
    else:
        return input_path.parent / default_name


def format_file_size(size: int) -> str:
    """
    Format file size
    
    Args:
        size: File size in bytes
        
    Returns:
        Formatted file size string
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"
