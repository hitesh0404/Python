- every python file is module
- collection of module is known as package
- previous version of python require `__init__`
 module to create an package
- `__str__` is the method which represent the object in a string 
- `__str__` these type of methods also known as megic method or dunder methods


| **Category**             | **Magic Method**                        | **Description**                                      | **Example Usage**               |
| ------------------------ | --------------------------------------- | ---------------------------------------------------- | ------------------------------- |
| **Object Lifecycle**     | `__new__(cls, …)`                       | Creates and returns a new instance.                  | `MyClass()`                     |
|                          | `__init__(self, …)`                     | Initializes the newly created instance.              | `MyClass(args)`                 |
|                          | `__del__(self)`                         | Destructor called before object deletion.            | `del obj`                       |
| **Representation**       | `__str__(self)`                         | User-friendly string (used by `print()` or `str()`). | `print(obj)`                    |
|                          | `__repr__(self)`                        | Unambiguous string for debugging (used by `repr()`). | `repr(obj)`                     |
| **Comparison**           | `__eq__(self, other)`                   | Defines `==` operator.                               | `obj1 == obj2`                  |
|                          | `__lt__(self, other)`                   | Defines `<` operator.                                | `obj1 < obj2`                   |
|                          | `__gt__(self, other)`                   | Defines `>` operator.                                | `obj1 > obj2`                   |
| **Numeric & Arithmetic** | `__add__(self, other)`                  | Implements `+`.                                      | `obj1 + obj2`                   |
|                          | `__sub__(self, other)`                  | Implements `-`.                                      | `obj1 - obj2`                   |
|                          | `__mul__(self, other)`                  | Implements `*`.                                      | `obj1 * obj2`                   |
|                          | `__len__(self)`                         | Defines behavior for `len()`.                        | `len(obj)`                      |
| **Container & Sequence** | `__getitem__(self, key)`                | Access items using `[]`.                             | `obj[key]`                      |
|                          | `__setitem__(self, key, value)`         | Assign items using `[]`.                             | `obj[key] = value`              |
|                          | `__iter__(self)`                        | Returns an iterator for loops.                       | `for item in obj:`              |
| **Attribute Access**     | `__getattr__(self, name)`               | Called when attribute not found.                     | Accessing nonexistent attribute |
|                          | `__setattr__(self, name, value)`        | Called when setting any attribute.                   | `obj.attr = value`              |
| **Other**                | `__call__(self, …)`                     | Makes an object callable like a function.            | `obj()`                         |
|                          | `__enter__(self)` / `__exit__(self, …)` | Context manager for `with` statements.               | `with obj:`                     |
