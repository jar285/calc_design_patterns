'''This file contains the tests for the 'multiplication' command in the app'''
import pytest
from app import App

def test_app_multiply_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'multiply' command, takes two numbers as input, and outputs their product."""
    # Setup the input for the 'multiply' command followed by two numbers and then 'exit'
    inputs = iter(['multiplication', '4', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    # Check that the exit was graceful with the correct exit code
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output from the 'multiply' command
    out, _ = capfd.readouterr()

    # Assert that the product of the numbers was printed to stdout
    # Ensure the expected output matches exactly what your 'multiply' command outputs, including any newlines or formatting
    expected_output = "The result of multiplying 4.0 by 5.0 is: 20.0"
    assert expected_output in out, f"The 'multiply' command did not produce the expected output. Got: {out}"

    # Optionally, include additional checks or variations to test different input scenarios
