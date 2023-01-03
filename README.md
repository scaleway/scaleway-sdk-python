# Scaleway Python SDK

This SDK enables you to interact with Scaleway APIs.

> **Warning**
> The project is in beta, but should be fairly stable. If you have issues using it, please [open an issue](https://github.com/scaleway/scaleway-sdk-python/issues/new).

**🔗  Important links:**

* [Reference documentation](https://scaleway.github.io/scaleway-sdk-python)
* [Example projects](./examples)
* [Developers website](https://developers.scaleway.com) (API documentation)

## Getting Started

You'll need a pair of access and secret keys to connect to Scaleway API. Please check the [documentation](https://www.scaleway.com/docs/console/my-project/how-to/generate-api-key) on how to retrieve them.

**For a simpler setup**, you could retrieve the profile from the configuration file and the environment variables:

```py
from scaleway import Client
from scaleway.registry.v1 import RegistryV1API

client = Client.from_config_file_and_env()

api = RegistryV1API(client)
print(api.list_namespaces())
```

`Client.from_profile` tries to load the configuration file and the environment variables. **Environment variables take precedence over the configuration file** but this feature is configurable.

**For more advanced needs**, please check the examples.

## Pagination

We included some pagination helpers for the methods supporting the feature. Let's take `list_namespaces()` (Registry product) as an example:

Retrieve the **first page**:

```py
result = api.list_namespaces(
    # page=1,
)
```

Retrieve **all the pages**:

```py
namespaces = api.list_namespaces_all()
```

## Types

The project is coded with Python, so don't hesitate to take advantage of it.

1. All **types of a product** are stored in the `scaleway.product.version` namespace. For instance, the `Image` interface of Registry v1 can be accessed with `scaleway.registry.v1.Image`.

## Logging

We are using the standard Python logging library. You can configure it as you wish.

```py
import logging

logger = logging.getLogger("scaleway")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
```

## Development

This repository is at its early stage and is still in active development.
If you are looking for a way to contribute please read [CONTRIBUTING.md](./CONTRIBUTING.md).

## Reach us

We love feedback. Feel free to reach us on [Scaleway Slack community](https://slack.scaleway.com/), we are waiting for you on [#opensource](https://scaleway-community.slack.com/app_redirect?channel=opensource).
