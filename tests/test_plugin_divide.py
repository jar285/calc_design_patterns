'''Test the 'divide' command in the app'''
import pytest
from app import App

def test_app_divide_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'divide' command, takes two numbers as input, and outputs their quotient."""
    # Setup the input for the 'divide' command followed by two numbers and then 'exit'
    inputs = iter(['divide', '10', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    # Check that the exit was graceful with the correct exit code
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output from the 'divide' command
    out, _ = capfd.readouterr()

    # Assert that the quotient of the numbers was printed to stdout
    # Ensure the expected output matches exactly what your 'divide' command outputs, including any newlines or formatting
    expected_output = "The result of dividing 10.0 by 2.0 is: 5.0"
    assert expected_output in out, f"The 'divide' command did not produce the expected output. Got: {out}"

# Optionally, include additional checks or variations to test different input scenarios, like division by zero
