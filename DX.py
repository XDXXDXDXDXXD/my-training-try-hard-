
calls = 0
def count_calls():
    global calls
    calls += 1
    return

def string_info(n):
    s1 = n.upper()
    s2 = n.lower()
    n = tuple(n)
    count_calls()
    return (len(n), s1, s2)


def is_contains(string, lst):
    count_calls()
    return string.lower() in [f.lower() for f in lst]



print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))

print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)




