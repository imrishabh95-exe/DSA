
'''.
func() runs the function and func return the object
Decorator always returns a function but if there is no internal function then if we inline append the string
then we wont be able to do. So we use inner function and return the inner function but 
if there is no inline modifications then we can do it.
'''
def strong(func):
    return func

def italics(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

@italics
@strong
def introduction():
    return 'This is a basic program'
 
print(introduction())