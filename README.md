# Software Construction - Lab 1

## My adherences to programming rules

### 1. **Abstraction**
The code hides details and gives easy ways to use things.

- Example: The `zoo` class has simple methods like `add_env()`, `add_food()`, and `inventory()` ([`zoo`]).

### 2. **Inheritance**
The code doesn't use inheritance, but it could be added to make new animal types (but i didn't do it)

- Example: A `bird` class could be made in the future

### 3. **Separation of concerns**
Each class does only one thing. This keeps the code simple and easy to change.

- Example: `animal` is for animals and `zoo` manages everything.

### 4. **Dependency inversions**
The `zoo` class does not control `animal`, or any other. It just uses them.

---
