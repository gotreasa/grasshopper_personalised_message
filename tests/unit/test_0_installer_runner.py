import pytest

from modules import personalised_message


def describe_greet():
    def should_error_when_owner_not_string():
        """🧪 should error when something other than a string is entered for the owner"""

        with pytest.raises(ValueError, match="❗️ The owner name must be a string"):
            personalised_message.greet(80, "Daniel")

    def should_error_when_name_not_string():
        """🧪 should error when something other than a string is entered for the name"""

        with pytest.raises(ValueError, match="❗️ The guest name must be a string"):
            personalised_message.greet("Rob", ["Ash"])

    def should_say_hello_boss_matching_names():
        """🧪 should say Hello boss when ower is Daniel and the name is Daniel"""

        assert personalised_message.greet("Daniel", "Daniel") == "Hello boss"
