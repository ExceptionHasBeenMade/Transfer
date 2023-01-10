import sys

def function(operator):
    if(operator == "'w'"):
        return True
    else:
        return False

if __name__ == "__main__":
    print("Press \"w\" to send trigger")
    while True:
        work = repr(sys.stdin.read(1))
        callback = function(work)
        # if __name__ != "__main__":
        break

def run(variable):
    variable = repr(sys.stdin.read(1))
    return variable

while True:
    work = repr(sys.stdin.read(1))
    callback = run(work)#function(work)
    break
# if __name__ == "__main__":
