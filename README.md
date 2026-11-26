# vibe_client: Python SDK for Vibe

[Vibe](https://astartech.ai) trains reinforcement-learning agents on your own Gymnasium environment and serves them
as HTTPS endpoints. Train and deploy an agent in the [web app](https://vibe.astartech.ai), then ask it for actions from
your code:

```bash
pip install "vibe_client>=0.2.0"      # Python 3.12+
```

```python
import os
from vibe_client.sdk import VibeClient

vibe = VibeClient(api_key=os.environ["VIBE_API_KEY"])      # Vibe web app > Account
answer = vibe.query_agent(
    experiment_id="<experiment-id>",
    observations={"continuous": [1.0, 0.0]},
)
print(answer.actions.value)
```

Observations can be `continuous` (a list), `discrete` (an int), `box`, `multi_discrete`, `multi_binary` or `dict`,
matching your environment's observation space. If the agent isn't deployed, `query_agent` raises `NoSuchResource`.

Quickstart with an example environment: https://astartech.ai/quickstart
