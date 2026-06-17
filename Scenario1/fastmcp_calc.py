#libraries 
from fastmcp import FastMCP

mcp = FastMCP(name = "Calculator")

@mcp.tool() 
def multiply(a : float, b:float) -> float:
    """ Multiplys Two Numbers and Return the Value"""
    return a * b 

@mcp.tool(
    name = "add",
    description="Add Two Number",
    tags = {"math", "airthmetic"}
)
def addition(x : float, y : float) -> float :
    """ Adds two numbers are Returns the value""" 
    return x + y

@mcp.tool() 
def subtract(a : float, b:float) -> float:
    """ Substract Two Numbers and Return the Value"""
    return a - b 

@mcp.tool() 
def division(a : float , b : float) -> float :
    """Divides the Numbers and Returns the Value"""
    if b == 0:
        raise ValueError("Cannot Divide by Zero")
    return a / b


if __name__ == "__main__":
    mcp.run() #STDIO by Default
