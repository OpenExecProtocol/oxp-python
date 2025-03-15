# Health

Methods:

- <code title="get /health">client.health.<a href="./src/oxp/resources/health.py">check</a>() -> None</code>

# Tools

Types:

```python
from oxp.types import ToolListResponse, ToolCallResponse
```

Methods:

- <code title="get /tools">client.tools.<a href="./src/oxp/resources/tools.py">list</a>() -> <a href="./src/oxp/types/tool_list_response.py">ToolListResponse</a></code>
- <code title="post /tools/call">client.tools.<a href="./src/oxp/resources/tools.py">call</a>(\*\*<a href="src/oxp/types/tool_call_params.py">params</a>) -> <a href="./src/oxp/types/tool_call_response.py">ToolCallResponse</a></code>
