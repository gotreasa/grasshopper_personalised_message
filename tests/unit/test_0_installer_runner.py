import pytest

from modules import personalised_message

BOSS_MESSAGE = "Hello boss"


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

        assert personalised_message.greet("Daniel", "Daniel") == BOSS_MESSAGE

    def should_say_hello_guest_non_matching_names():
        """🧪 should say Hello guest when ower is Sam and the name is Daniel"""

        assert personalised_message.greet("Sam", "Daniel") == "Hello guest"

    def should_say_hello_boss_matching_Conor():
        """🧪 should say Hello boss when ower is Conor and the name is Conor"""

        assert personalised_message.greet("Conor", "Conor") == BOSS_MESSAGE

    def should_say_hello_boss_matching_different_cases():
        """🧪 should say Hello boss when ower is owen and the name is Owen"""

        assert personalised_message.greet("owen", "Owen") == BOSS_MESSAGE

    def should_say_hello_boss_matching_different_cases_multiple_name():
        """🧪 should say Hello boss when ower is owen Williams and the name is Owen williams"""

        assert personalised_message.greet("owen Williams", "Owen williams") == BOSS_MESSAGE

    def should_say_hello_guest_sligtly_different_names_Daniel():
        """🧪 should say Hello guest when ower is Daniel and the name is Danielle"""

        assert personalised_message.greet("Daniel", "Danielle") == "Hello guest"

    def should_say_hello_guest_sligtly_different_names_Michele():
        """🧪 should say Hello guest when ower is Michele and the name is Michel"""

        assert personalised_message.greet("Michele", "Michel") == "Hello guest"
