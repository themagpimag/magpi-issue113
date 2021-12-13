from gpiozero import MCP3008

uv = MCP3008(0)

while True:  
    print("UV: %-3.5f V" % (3.3 * uv.value), end = "\r")