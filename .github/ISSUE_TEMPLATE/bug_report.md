---
name: 🐛 Bug Report
about: Unexpected or broken behavior of SDK-python 🤔
labels: bug
---

<!--- Please keep this note for the community --->

### Community Note

* Please vote on this issue by adding a 👍 [reaction](https://blog.github.com/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/) to the original issue to help the community and maintainers prioritize this request
* Please do not leave "+1" or other comments that do not add relevant new information or questions, they generate extra noise for issue followers and do not help prioritize the request
* If you are interested in working on this issue or have submitted a pull request, please leave a comment

<!--- Thank you for keeping this note for the community --->

## Command attempted

<!-- Please provide the minimal Python code that reproduces the issue. -->

```python
from scaleway_core.client import Client
from scaleway.instance.v1.types import BootType
from scaleway.instance.v1.custom_api import InstanceUtilsV1API

client = Client.from_config_file_and_env()
instance_api = InstanceUtilsV1API(client)

server = instance_api.create_server(
    commercial_type="DEV1-S",
    zone="fr-par-1",
    name="test-server",
    dynamic_ip_required=False,
    volumes={},
    protected=False,
    boot_type=BootType.LOCAL,
)
```
### Expected Behavior

<!--- What should have happened? --->

### Actual Behavior

<!--- What actually happened? --->

## More info

SDK-Python version: <!-- e.g. 1.32.0 -->

Python version: <!-- e.g. 3.10.0 -->

OS version: <!-- e.g. Ubuntu 22.04 -->

<!--- Add any other context, logs, screenshots, or system outputs about the problem --->

