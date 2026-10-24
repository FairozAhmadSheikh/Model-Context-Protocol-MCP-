from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio


async def main():
    client=MultiServerMCPClient(
        # MCP Server Config(JSON)
        {
            "data_fetch_mcp_stdio":{
                "transport":"stdio",
                "command":r"C:\Users\habra\OneDrive\Desktop\mcp-server\.venv\Scripts\python.exe",
                "args":[r"C:\Users\habra\OneDrive\Desktop\mcp-server\CHAP1_CREATE_MCP\1_mcp_server.py"]
            }
        }
    )

    tools=await client.get_tools()
    print("available tools : ",tools)

if __name__=="__main__":
    asyncio.run(main())