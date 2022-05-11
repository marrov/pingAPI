pingAPI
=======

``pingAPI`` is a simple API made in python using fastAPI. It allows a client to make asynchronous ping requests to any website from the server.

Requirements
------------

This simple API fulfills the following requirements:

* Answers "questions" with a JSON payload
* Calls an arbitrary external executable (in this case Linux/UNIX ping)
* Handles custom massages for HTTP status codes #400, #404, #500, #501, etc.
* Handles new requests while performing a blocking call (asynchronous operation)
* Performs graceful shutdowns (stops requests and serves premature output of the terminated requests)
* Uses sample unit test for th API (using TestClient)

Installation
------------

These instructions will get you a copy of the project up and running on your local machine for usage, development, and testing purposes. **Please note** that only Linux environments have been tested in the current implementation but the code should work independently of the OS.

Open a terminal window and clone this repository by writing:

.. code-block:: bash

    git clone https://github.com/marrov/pingapi

To use ``pingapi`` several `Python 3 <https://www.python.org/>`__ packages are required. Creating a brand new `Conda <https://docs.conda.io/en/latest/>`__ environment for this is recommended. This can be done easily with the provided ``environment.yml`` file as follows:

.. code-block:: bash

    conda env create -f environment.yml
    conda activate pingapi

The environment is self-contained to not influence other local python installations and avoid conflicts with previously installed packages. 

You can test out your installation by running: 

.. code-block:: python

    pytest

To deactivate the ``pingapi`` environment simply type:

.. code-block:: bash

    conda deactivate

Authors
-------

-  `Marc Rovira <https://github.com/marrov>`__