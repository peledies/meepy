# Meep Morp

>meep morp clink clank

Meepy is a package who's sole purpose is to print basic diagnostic information to the log. It is particularly useful when you want to use `print()` in your code but you want to know where it came from.


## Options
* `message`   [default: None]
* `parent`    [default: None]
* `expected`  [default: None]

## Examples
---

### Import
```python
from meepy import Meep
```

### Basic Usage
```python
Meep.morp()
```

### Option: **message**
Adds a custom message to the output
```python
Meep.morp(message='a custom message')
```

### Option: **parent**
By adding the `parent` meepy will print the path to the file where the Meep.morp occurred.
```python
from meepy import Meep

class Example:
    def test():
        Meep.morp(self)
        # or
        Meep.morp(parent=self)
```

## Option: **expected**
Lets face it, sometimes you want to straddle a line of code to see if its a suspect line. Using the `expected` option can help identify your morps.

```python
Meep.morp()
# this is the suspect line of code
Meep.morp(False)
# or
Meep.morp(expected=False)
```