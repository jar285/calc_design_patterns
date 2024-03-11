'''This file contains the tests for the 'subtract' command in the app'''
import pytest
from app import App

def test_app_substract_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'subtract' command, takes two numbers as input, and outputs their difference."""
    # Setup the input for the 'subtract' command followed by two numbers and then 'exit'
    inputs = iter(['substract', '10', '3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    # Check that the exit was graceful with the correct exit code
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output from the 'subtract' command
    out, _ = capfd.readouterr()

    # Assert that the difference of the numbers was printed to stdout
    # Ensure the expected output matches exactly what your 'subtract' command outputs, including any newlines or formatting
    expected_output = "The result of subtracting 3.0 from 10.0 is: 7.0"
    assert expected_output in out, f"The 'subtract' command did not produce the expected output. Got: {out}"

    # Optionally, include additional checks or variations to test different input scenarios, like negative numbers
