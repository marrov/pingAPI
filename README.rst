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

.. code-block:: bash

    pytest

To deactivate the ``pingapi`` environment simply type:

.. code-block:: bash

    conda deactivate

Usage
-----

This usage section will provide a brief rundown of how to use pingAPI. As has been created using FastAPI, you can also check the `official documentation <https://fastapi.tiangolo.com/>`__ for further information.

First, run the live server using ``uvicorn``:

.. code-block:: bash

    uvicorn pingapi:app --reload
    
Then, you could directly open `http://127.0.0.1:8000 <http://127.0.0.1:8000>`__ in your browser, but as ``pingapi`` has no index route with the ``GET`` method, you will encounter a ``Not Found`` message. To read the documentation for ``pingAPI`` go to `http://127.0.0.1:8000/docs <http://127.0.0.1:8000/docs>`__. Here you will see that the only endpoint (apart from the docs) in ``pingAPI`` is `http://127.0.0.1:8000/ping <http://127.0.0.1:8000/ping>`__, which requires ``POST``. You can wither test ``pingAPI`` directly from the docs or for instance by using ``curl`` from the terminal. An example of a ``curl`` command for ``pingAPI`` is:

.. code-block:: bash

    curl -X 'POST' \
        'http://127.0.0.1:8000/ping/' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "host_addr": "www.kambi.com",
        "n_pings": 10,
        "interval": 0.2
    }'

Running this command will send a ``POST`` request to ``pingAPI`` running on your local server. In particular, it will ping the Kambi website 10 times with a 0.2 second interval and will return the statistics of the pings such as the average time and the packet loss rate. Try different websites, number of pings, and intervals to see the differences!

Authors
-------

-  `Marc Rovira <https://github.com/marrov>`__
