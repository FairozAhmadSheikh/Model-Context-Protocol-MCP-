import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client=MultiServerMCPClient({
        # Mcp Server Config
        "data_fetch_mcp_http":{
            "transport":"streamable-http",
            "url":"http://localhost:8050/mcp"
        }
    })
    tools=await client.get_tools()
    print("Available Tools:",tools)

if __name__=="__main__":
    asyncio.run(main())