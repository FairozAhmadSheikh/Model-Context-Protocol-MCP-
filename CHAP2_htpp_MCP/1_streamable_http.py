from fastmcp import FastMCP

mcp=FastMCP()

@mcp.tool()
def fetch_data():
    """
    Use this tool to fetch any data 
    """
    return {"data":"Data Fetched Sucessfully"}

@mcp.tool()
def process_data(path:str):
    """
    Use this tool to process fetched data 
    """

    return{"Processed_data":f"Data processed at {path}"}


if __name__=="__main__":
    mcp.run(transport="streamable-http",host="0.0.0.0",port=8050)