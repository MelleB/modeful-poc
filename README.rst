Modeful - A diagram editor with modes
=====================================

Status
------
This is PRE-PRE-ALPHA software. Not in any usable state.
To run it use:

.. code-block:: bash

    bin/modeful [filenames ...]

Navigate the elements with the ``h``, ``j``, ``k``, ``l`` keys,
Open the filebrowser with ``f o`` (First press ``f``, then ``o``, as in: file, open)

Example files can be found in the ``tests/testdata`` directory.


About
-----
Modeful attempts to bring the power of modal editing to diagram software.
Once you've felt the power of vim_, or emacs_, you sometimes wish more 
software would focus on power users. Enable them to create, modify and 
navigate swiftly, without leaving home row.

Modeful is focused on power users. The current version is a proof
of concept to show that modal editing indeed does work for diagram creation.

This first version of modeful is built using on Kivy_. It's a fantastic
framework to create quick proof of concepts. If things get more serious
a rewrite might be needed in a compiled language (C++/C#/...), we'll see...

.. _vim: https://www.vim.org
.. _emacs: https://www.gnu.org/software/emacs/
.. _Kivy: https://kivy.org


Installlation
-------------
NOTE: This is how it should work in the future!

Install the latest published version using pip:

.. code-block:: bash

   pip install modeful

Install the latest development version

.. code-block:: bash

   git clone https://github.com/Modeful/modeful-poc modeful
   cd modeful && python setup.py


File format
-----------
Both configuration and diagrams are stored as TOML_ files.
It's human readable, which makes it easy to diff and put under version control.

.. _TOML : https://github.com/toml-lang/toml


Contributions
-------------
All contributions are very welcome!
Not sure what to contribute?
Check to see if the documentation can be improved, or check the issue list!


License
-------
Modeful is released under GNU GPLv3, please see the LICENSE.txt_ file for the full license.

.. _LICENSE.txt: ./LICENSE.txt
