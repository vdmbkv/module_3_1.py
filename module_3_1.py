# Счетчик вызовов

calls = 0

def count_calls():
    global calls
    calls += 1

    return

def string_info(word):
    count_calls()

    word_len = len(word)
    word_up = word.upper()
    word_low = word.lower()

    return(str(word_len), word_up, word_low)

def is_contains(string, list_to_search):
    count_calls()

    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    if string_lower in list_lower:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)