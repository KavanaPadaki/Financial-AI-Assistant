from mcp.server.fastmcp import FastMCP

mcp = FastMCP("test")

@mcp.tool()
def hello():
    return "hello"

if __name__ == "__main__":
    mcp.run()