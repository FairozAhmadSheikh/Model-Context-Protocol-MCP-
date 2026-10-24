import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
        client=MultiServerMCPClient(
                {
                        "data_fetch_mcp":{
                                "transport":"stdio",
                                "command":"uvx",
                                "args":['duckduckgo-mcp-server']
                }
                        
        
        }
        )

        tools=await client.get_tools()
        for tool in tools:
                print("Available tools:",tool.name)

        fetch_tool=tools[0]
        result=await fetch_tool.ainvoke({'query':"what about the strait of hormuz?"})
        print("MCP Response :",result)

if __name__=="__main__":
        asyncio.run(main())