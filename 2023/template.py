import pysnooper

# @pysnooper.snoop()
def main(input):
    with open(input, "r") as f:
        content = f.read()
    return content
 
# input = "./example"
input = "./input"

print(main(input))
