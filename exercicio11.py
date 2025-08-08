
def valida_string(string, min, max):
    if len(string) < min or len(string) > max:
        return False
    else:
        return True

print(valida_string('cachorro', 1 , 5))

print(valida_string('gato', 1 , 5))