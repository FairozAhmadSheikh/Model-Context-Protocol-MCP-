from fastmcp import FastMCP

mcp=FastMCP()


@mcp.tool()
def fetch_data():
    """
    Tool to be used to fetch any data 
    """
    return {"fetched_data":"This is just an example to understand flow"}

@mcp.tool()
def process_data(path):
    """
    Process the Fetched Data using this tool
    """
    return {"processed_data":f"processed the data to {path}"}



if __name__=="__main__":
    mcp.run(transport="stdio")