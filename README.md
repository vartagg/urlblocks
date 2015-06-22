# URLBlocks 2

[![Build Status](https://secure.travis-ci.org/zacharyvoase/urlobject.png?branch=master)](http://travis-ci.org/zacharyvoase/urlobject)

`URLBlocks` is a utility class for manipulating URLs. The latest incarnation of
this library builds upon the ideas of its predecessor, but aims for a clearer
API, focusing on proper method names over operator overrides. It's also being
developed from the ground up in a test-driven manner, and has full Sphinx
documentation.

## Installation

URLBlocks is hosted on [PyPI](http://pypi.python.org/pypi/URLBlocks). Install
it using `pip`:

    pip install URLBlocks


## Quickstart

Check out the
[quickstart](https://urlobject.readthedocs.org/en/latest/quickstart.html) on
ReadTheDocs to get started.


## (Un)license

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this
software, either in source code form or as a compiled binary, for any purpose,
commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this
software dedicate any and all copyright interest in the software to the public
domain. We make this dedication for the benefit of the public at large and to
the detriment of our heirs and successors. We intend this dedication to be an
overt act of relinquishment in perpetuity of all present and future rights to
this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>


### Credits

This library bundles [six][], which is licensed as follows:

  [six]: http://packages.python.org/six/

> Copyright (c) 2010-2012 Benjamin Peterson
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Many thanks go to [Aron Griffis](http://arongriffis.com/) for porting this
library to Python 3, and to [vmalloc](https://github.com/vmalloc) for work on
the comprehensive API documentation and Sphinx setup.
