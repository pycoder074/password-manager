import random

def generate_password(num_required=False, char_required=False, length=12, caps_required=False):
    password_array = []

    def generate_number():
        return str(random.randint(0, 9))

    def generate_char():
        char_array = [33, 95, 64, 38, 35, 37, 36, 42, 43]
        index = random.randint(0, len(char_array) - 1)
        return chr(char_array[index])

    def generate_caps():
        return chr(random.randint(65, 90))

    def generate_small():
        return chr(random.randint(97, 122))

    def generate(len):
        turn = len // 3
        rem = len

        if char_required:
            temp = random.randint(1, turn)
            for i in range(temp):
                password_array.append(generate_char())
            rem -= temp

        if num_required:
            temp = random.randint(1, turn)
            for i in range(temp):
                password_array.append(generate_number())
            rem -= temp

        if caps_required:
            temp = random.randint(1, turn)
            for i in range(temp):
                password_array.append(generate_caps())
            rem -= temp

        for i in range(rem):
            password_array.append(generate_small())

        return password_array

    def shuffle_array(arr):
        for i in range(len(arr) - 1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

    result_array = shuffle_array(generate(length))
    output = ''.join(result_array)
    return output

if __name__ == "__main__":
    print(generate_password())
