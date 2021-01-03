import os

def gen_passwd():
    return os.urandom(15)
    
    
if __name__ == '__main__':
    print(gen_passwd())