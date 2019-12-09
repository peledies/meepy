# Meep Morp

>meep morp clink clank

## Examples
---

### Import
```python
from meepy import Meep
```

### Meep morp the current line number
```python
Meep.morp()
```

### Meep morp with a custom message
```python
Meep.morp(message='a custom message')
```

### Meep morp with the method path and line
```python
from meepy import Meep

class Example:
    def test():
        Meep.morp(self)
        # or
        Meep.morp(parent=self)
```
