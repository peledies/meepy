### increment git tag
```
git tag -a n.n.n -m 'release message'
```

### Run setup file again.

```
python3 setup.py sdist bdist_wheel.
```

### Push to pypi
```
python3 -m twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
```