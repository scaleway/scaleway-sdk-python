---
name: 🚀 Feature request
about: I have a suggestion (and might want to implement it myself 🙂)!
labels: enhancement
---

<!--- Please keep this note for the community --->

### Community Note

* Please vote on this issue by adding a 👍 [reaction](https://blog.github.com/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/) to the original issue to help the community and maintainers prioritize this request
* Please do not leave "+1" or other comments that do not add relevant new information or questions, they generate extra noise for issue followers and do not help prioritize the request
* If you are interested in working on this issue or have submitted a pull request, please leave a comment

<!--- Thank you for keeping this note for the community --->

## Description

<!-- Describe the problem, limitation, or missing feature that you think SDK-Python should address. -->

## Proposed Solution

<!-- How do you imagine SDK-Python could expose this functionality? -->

```python
# Example of a possible API usage
from scaleway.instance.v1.custom_api import InstanceUtilsV1API
from scaleway_core.client import Client

client = Client.from_config_file_and_env()
instance_api = InstanceUtilsV1API(client)
server = instance_api.new_feature(...)
```
