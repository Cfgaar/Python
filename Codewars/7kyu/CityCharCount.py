# https://www.codewars.com/kata/5b358a1e228d316283001892
def get_strings(city):
    unique_char = []
    city = city.lower()
    city = city.replace(' ', '')
    for c in city:
        if c not in unique_char:
            unique_char.append(c)
    count_string = ""
    for i in unique_char:
        count_string += (i + ":" + "*" * city.count(i))
        if i != unique_char[len(unique_char) - 1]:
            count_string += ','
    return count_string


print(get_strings('Chicago'))

