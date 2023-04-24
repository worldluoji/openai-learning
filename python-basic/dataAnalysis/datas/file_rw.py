
def write(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)

def read(filepath):
    with open(filepath, 'r') as f:
        return f.read()