Modeful - A diagram editor with modes
=====================================

WARNING
-------
This is PRE-PRE-ALPHA software. Not in any usable state.
Use at your own risk.


About
-----
Modeful attempts to bring the power of modal editing to diagram software.
Once you've felt the power of vim_, or emacs_, you sometimes wish more 
software would focus on power users. Enable them to create, modify and 
navigate like true ninjas, without leaving home row.

Modeful is focused on power users. The current version is a proof
of concept to show that modal editing indeed does work for diagram creation.

This first version of modeful is built using on Kivy_. It's a fantastic
framework to create quick proof of concepts. If things get more serious
a rewrite might be needed in a compiled language (C++/C#/...), we'll see...

.. _vim: https://www.vim.org
.. _emacs: https://www.gnu.org/software/emacs/
.. _Kivy: https://kivy.org


Shortcuts
---------
Currently the following shortcuts are supported (and hard-coded, these
are supposed to go to a separate config file)

==========  ===========
 Command     Shortcut
==========  ===========
Move left   ``h``
Move down   ``j``
Move up     ``k``
Move right  ``l``
Open file   ``f o``
Add Class   ``a c``
Add Note    ``a n``
==========  ===========
 

Installlation
-------------
Install the latest development version

.. code-block:: bash

   git clone https://github.com/Modeful/poc modeful-poc
   cd modeful-poc && python setup.py

(Note: As of yet I haven't acutally tested this...)

To run it use:

.. code-block:: bash

    bin/modeful [filenames ...]

Example files can be found in the ``tests/testdata`` directory.


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
