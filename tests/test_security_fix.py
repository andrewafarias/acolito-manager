import sys
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add src to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from acolito_manager.utils import open_file

def test_open_file_darwin():
    print("Testing darwin...")
    with patch("sys.platform", "darwin"), \
         patch("subprocess.call") as mock_call:
        open_file("test_path.pdf")
        mock_call.assert_called_once_with(["open", "--", "test_path.pdf"])

def test_open_file_win32():
    print("Testing win32...")
    with patch("sys.platform", "win32"), \
         patch("acolito_manager.utils.os.startfile", create=True) as mock_startfile:
        open_file("test_path.pdf")
        mock_startfile.assert_called_once_with("test_path.pdf")

def test_open_file_linux():
    print("Testing linux...")
    with patch("sys.platform", "linux"), \
         patch("subprocess.call") as mock_call:
        open_file("test_path.pdf")
        expected_path = os.path.abspath("test_path.pdf")
        mock_call.assert_called_once_with(["xdg-open", expected_path])

def test_open_file_exception_handling():
    print("Testing exception handling...")
    # Should not raise exception
    with patch("sys.platform", "linux"), \
         patch("subprocess.call", side_effect=Exception("error")):
        open_file("test_path.pdf")

if __name__ == "__main__":
    test_open_file_darwin()
    test_open_file_win32()
    test_open_file_linux()
    test_open_file_exception_handling()
    print("All security tests passed!")
