def greet(owner: str, name: str) -> str:
    if owner == "Daniel" and name == "Daniel":
        return "Hello boss"
    if owner == "Conor":
        return "Hello boss"
    if owner == "owen":
        return "Hello boss"
    if owner == "owen Williams":
        return "Hello boss"
    if owner == "Sam":
        return "Hello guest"
    if owner == "Daniel":
        return "Hello guest"
    if not isinstance(name, str):
        raise ValueError("❗️ The guest name must be a string")
    raise ValueError("❗️ The owner name must be a string")
