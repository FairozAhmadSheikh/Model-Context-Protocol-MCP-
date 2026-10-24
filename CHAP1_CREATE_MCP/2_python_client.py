from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
import os
import asyncio

# Absolute path to the MCP server script
mcp_server_script = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "1_mcp_server.py"
)

# Setup Server Params
server_parmas=StdioServerParameters(
    command="python",
    args=[str(mcp_server_script)],
    env={}
)

# Setup Client
async def main():
    async with stdio_client(server_parmas) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools=await session.list_tools()
            print(f'Available Tools{tools}')


if __name__=="__main__":
    asyncio.run(main())

