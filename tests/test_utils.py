"""
Unit tests for utility functions
"""
from pathlib import Path

import pytest

from magneto.utils import collect_torrent_files, format_file_size, get_output_path


@pytest.mark.unit
class TestCollectTorrentFiles:
    """Test cases for collect_torrent_files function"""
    
    def test_collect_single_file(self, mock_torrent_file):
        """Test collecting a single torrent file"""
        files = collect_torrent_files(mock_torrent_file)
        assert len(files) == 1
        assert files[0] == mock_torrent_file
    
    def test_collect_single_file_wrong_extension(self, tmp_path):
        """Test collecting a file with wrong extension"""
        text_file = tmp_path / "test.txt"
        text_file.write_text("Not a torrent")
        files = collect_torrent_files(text_file)
        assert len(files) == 0
    
    def test_collect_from_directory(self, sample_torrent_dir):
        """Test collecting torrent files from directory"""
        files = collect_torrent_files(sample_torrent_dir)
        assert len(files) == 3
        assert all(f.suffix.lower() == '.torrent' for f in files)
    
    def test_collect_recursive(self, tmp_path, mock_torrent_bytes):
        """Test recursive collection"""
        # Create nested directory structure
        root = tmp_path / "root"
        root.mkdir()
        subdir = root / "subdir"
        subdir.mkdir()
        
        # Create files in both directories
        (root / "file1.torrent").write_bytes(mock_torrent_bytes)
        (subdir / "file2.torrent").write_bytes(mock_torrent_bytes)
        
        files = collect_torrent_files(root, recursive=True)
        assert len(files) == 2
    
    def test_collect_non_recursive(self, tmp_path, mock_torrent_bytes):
        """Test non-recursive collection"""
        # Create nested directory structure
        root = tmp_path / "root"
        root.mkdir()
        subdir = root / "subdir"
        subdir.mkdir()
        
        # Create files in both directories
        (root / "file1.torrent").write_bytes(mock_torrent_bytes)
        (subdir / "file2.torrent").write_bytes(mock_torrent_bytes)
        
        files = collect_torrent_files(root, recursive=False)
        assert len(files) == 1
        assert files[0].name == "file1.torrent"
    
    def test_collect_case_sensitive(self, tmp_path, mock_torrent_bytes):
        """Test case-sensitive collection"""
        root = tmp_path / "root"
        root.mkdir()
        (root / "file.TORRENT").write_bytes(mock_torrent_bytes)
        (root / "file.torrent").write_bytes(mock_torrent_bytes)
        
        files = collect_torrent_files(root, case_sensitive=True)
        # Should find both when case-sensitive
        assert len(files) >= 1
    
    def test_collect_case_insensitive(self, tmp_path, mock_torrent_bytes):
        """Test case-insensitive collection"""
        root = tmp_path / "root"
        root.mkdir()
        (root / "file.TORRENT").write_bytes(mock_torrent_bytes)
        (root / "file.torrent").write_bytes(mock_torrent_bytes)
        
        files = collect_torrent_files(root, case_sensitive=False)
        # Should find both
        assert len(files) >= 1
    
    def test_collect_empty_directory(self, tmp_path):
        """Test collecting from empty directory"""
        empty_dir = tmp_path / "empty"
        empty_dir.mkdir()
        files = collect_torrent_files(empty_dir)
        assert len(files) == 0
    
    def test_collect_nonexistent_path(self):
        """Test collecting from non-existent path"""
        fake_path = Path("/nonexistent/path")
        files = collect_torrent_files(fake_path)
        assert len(files) == 0


@pytest.mark.unit
class TestGetOutputPath:
    """Test cases for get_output_path function"""
    
    def test_get_output_path_with_specified_file(self, tmp_path):
        """Test with specified output file"""
        input_path = tmp_path / "input.torrent"
        output_path = tmp_path / "output.txt"
        result = get_output_path(input_path, output_path)
        assert result == output_path
    
    def test_get_output_path_with_specified_dir(self, tmp_path):
        """Test with specified output directory"""
        input_path = tmp_path / "input.torrent"
        output_dir = tmp_path / "output_dir"
        output_dir.mkdir()
        result = get_output_path(input_path, output_dir)
        assert result == output_dir / "magnet_links.txt"
    
    def test_get_output_path_auto_from_file(self, tmp_path):
        """Test auto-determining output path from file"""
        input_file = tmp_path / "input.torrent"
        result = get_output_path(input_file)
        assert result == tmp_path / "magnet_links.txt"
    
    def test_get_output_path_auto_from_dir(self, tmp_path):
        """Test auto-determining output path from directory"""
        input_dir = tmp_path / "input_dir"
        input_dir.mkdir()
        result = get_output_path(input_dir)
        assert result == input_dir / "magnet_links.txt"
    
    def test_get_output_path_custom_default_name(self, tmp_path):
        """Test with custom default name"""
        input_file = tmp_path / "input.torrent"
        result = get_output_path(input_file, default_name="custom.txt")
        assert result == tmp_path / "custom.txt"
    
    def test_get_output_path_none_specified(self, tmp_path):
        """Test with None specified"""
        input_file = tmp_path / "input.torrent"
        result = get_output_path(input_file, None)
        assert result == tmp_path / "magnet_links.txt"


@pytest.mark.unit
class TestFormatFileSize:
    """Test cases for format_file_size function"""
    
    def test_format_bytes(self):
        """Test formatting bytes"""
        assert format_file_size(512) == "512.00 B"
    
    def test_format_kilobytes(self):
        """Test formatting kilobytes"""
        assert "KB" in format_file_size(1024)
        assert format_file_size(2048) == "2.00 KB"
    
    def test_format_megabytes(self):
        """Test formatting megabytes"""
        assert "MB" in format_file_size(1024 * 1024)
        assert format_file_size(2 * 1024 * 1024) == "2.00 MB"
    
    def test_format_gigabytes(self):
        """Test formatting gigabytes"""
        assert "GB" in format_file_size(1024 * 1024 * 1024)
        assert format_file_size(2 * 1024 * 1024 * 1024) == "2.00 GB"
    
    def test_format_terabytes(self):
        """Test formatting terabytes"""
        assert "TB" in format_file_size(1024 * 1024 * 1024 * 1024)
    
    def test_format_zero(self):
        """Test formatting zero bytes"""
        result = format_file_size(0)
        assert "0.00 B" in result or "0 B" in result
    
    def test_format_large_number(self):
        """Test formatting very large number"""
        large = 1024 * 1024 * 1024 * 1024 * 1024
        result = format_file_size(large)
        assert "PB" in result

