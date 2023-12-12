def greet(owner: str, name: str) -> str:
    if not isinstance(name, str):
        raise ValueError("❗️ The guest name must be a string")
    if not isinstance(owner, str):
        raise ValueError("❗️ The owner name must be a string")
    if owner.lower() == name.lower():
        return "Hello boss"
    return "Hello guest"
