import pytest

from modules import personalised_message


def describe_greet():
    def should_error_when_not_string():
        """🧪 should error when something other than a string is entered for the owner"""

    with pytest.raises(ValueError, match="❗️ The owner name must be a string"):
        personalised_message.greet(80, "Daniel")
