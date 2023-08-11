.. Scaleway Python SDK documentation master file, created by
   sphinx-quickstart on Fri Oct 21 12:20:18 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#########################################
Scaleway Python SDK documentation
#########################################

Installation
============

This library is made to work with Python 3.8 but should work on the latest versions too.

The SDK is available in two flavors, a synchronous and an asynchronous one.

Install from PyPI::

   pip install scaleway

Install from PyPI (async)::

   pip install scaleway-async

Initialization
==============

You'll need a pair of access and secret keys to connect to Scaleway API. Please check the `documentation <https://www.scaleway.com/en/docs/identity-and-access-management/iam/how-to/create-api-keys>`_ on how to retrieve them.

:mod:`scaleway` APIs must be initialized with a :class:`scaleway.Client`. 

A **minimal setup** would look like this::

   from scaleway import Client
   from scaleway.registry.v1 import RegistryV1API

   client = Client(
      access_key="SCWXXXXXXXXXXXXXXXXX",
      secret_key="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      default_project_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      default_region="fr-par",
      default_zone="fr-par-1",
   )

   registry_api = RegistryV1API(client)

.. autofunction:: scaleway.Client

For a simpler setup, you could retrieve the profile from either the configuration file or the environment variables::

   from scaleway import Client

   client = Client.from_config_file_and_env()  

.. autofunction:: scaleway.Client.from_config_file_and_env

Pagination
==========

We included some pagination helpers for the methods supporting the feature. Let's take :meth:`scaleway.registry.v1.RegistryV1API.list_namespaces` as an example:

Retrieve the **first page**::

   result = api.list_namespaces(
      # page=1,
   )

.. autofunction:: scaleway.registry.v1.RegistryV1API.list_namespaces

Retrieve **all the pages**::

   namespaces = api.list_namespaces_all()

.. autofunction:: scaleway.registry.v1.RegistryV1API.list_namespaces_all

Types
=====

The project is coded with Python, so don't hesitate to take advantage of it.

1. All **types of a product** are stored in the `scaleway.product.version` namespace. For instance, :class:`scaleway.registry.v1.Image`.

Logging
=======

We are using the standard Python logging library. You can configure it as you wish::

   import logging

   logger = logging.getLogger("scaleway")
   logger.addHandler(logging.StreamHandler())
   logger.setLevel(logging.DEBUG)


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   scaleway
   scaleway-async
   scaleway-core



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
