from integer import return_integer

def test():
    i = return_integer()
    assert(i<=10 and i>=0)