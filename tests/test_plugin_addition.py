'''This file contains the tests for the 'addition' command in the app'''
import pytest
from app import App

def test_app_addition_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command, takes two numbers as input, and outputs their sum."""
    # Setup the input for the 'add' command followed by two numbers and then 'exit'
    inputs = iter(['addition', '3', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    # Check that the exit was graceful with the correct exit code
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output from the 'add' command
    out, _ = capfd.readouterr()

    # Assert that the sum of the numbers was printed to stdout
    # Ensure the expected output matches exactly what your 'add' command outputs, including any newlines or formatting
    expected_output = "The sum is: 8.0"
    assert expected_output in out, f"The 'addition' command did not produce the expected output. Got: {out}"

    # Optionally, include additional checks or variations to test different input scenarios
