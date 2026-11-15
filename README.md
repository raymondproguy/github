## Contributors

This project welcomes collaboration.

## Utilities

A growing collection of small, dependency-free Python utilities.

### slugify

Convert arbitrary text to a URL-safe slug.

```bash
python slugify.py "Hello, World!"
# hello-world
```

```python
from slugify import slugify

slugify("Crème brûlée")  # -> "creme-brulee"
slugify("Hello World", separator="_")  # -> "hello_world"
```

Run the tests with:

```bash
python -m unittest test_slugify.py
```
