def greet(owner: str, name: str) -> str:
    if owner == "Daniel":
        return "Hello boss"
    if not isinstance(name, str):
        raise ValueError("❗️ The guest name must be a string")
    raise ValueError("❗️ The owner name must be a string")
