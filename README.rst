urlblocks
=========

`urlblocks` is the module provided URL string class which can be operated as a constructor, consisting of some blocks - URL components.

This is the fork of `zacharyvoase/URLObject project <https://github.com/zacharyvoase/urlobject>`__
but with several key changes and new functionality:

-  Following `PEP-20, the zen of Python <https://www.python.org/dev/peps/pep-0020/>`__, errors should never pass silently. To comply with this standard, invalid URLs, such as empty, hostless or schemeless now got denied.
-  Domains manipulation support.
-  Additional helpers (such as manipulations with trailing slashes) are available.



Installation
============

.. code:: bash

    pip install urlblocks


Documentation
=============

Coming soon.



(Un)license
===========

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

For more information, please refer to `unlicense.org <http://unlicense.org/>`__


Credits
=======

    This library bundles `six <http://packages.python.org/six/>`__, which is licensed as follows:

    Copyright (c) 2010-2012 Benjamin Peterson

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
    of the Software, and to permit persons to whom the Software is furnished to do
    so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

Many thanks go to `Aron Griffis <http://arongriffis.com/>`__ for porting
this library to Python 3, and to `vmalloc <https://github.com/vmalloc>`__ for
work on the comprehensive API documentation and Sphinx setup.
