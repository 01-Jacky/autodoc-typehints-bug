This repo shows a bug since autodoc-typehints 1.8.0

Make a venv and...
```
pip install -r requirements.txt
cd docs
make html
```

This produces the warning: 

my_module\foo.py:docstring of my_module.foo.Foo:5: WARNING: Field list ends without a blank line; unexpected unindent.

However the docstring doesn't seem to have blank line or unindent issue.

Might relate to how html out ends up generating parameters twice?