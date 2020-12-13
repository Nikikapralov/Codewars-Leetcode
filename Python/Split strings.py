def solution(s):
    string = s
    result = []
    if len(string) % 2 != 0:
        string += '_'
    current_string = ''
    for char in string:
        current_string += char
        if len(current_string) == 2:
            result.append(current_string)
            current_string = ''
    return result


