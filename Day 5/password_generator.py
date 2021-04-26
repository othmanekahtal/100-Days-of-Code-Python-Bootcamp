import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_of_alpha = int(input("Enter the Number of the alphabet : "))
number_of_Symbol = int(input("Enter the Number of the symbol : "))
number_of_digits = int(input("Enter the Number of the digit :"))


def random_choice(number_alpha, number_symbol, number_number):
    random_arr: list[str] = []
    for i in range(0, number_alpha):
        # random_arr.append(alphabet[random.randint(0, len(alphabet) - 1)])
        random_arr.append(random.choice(letters))
    for i in range(0, number_symbol):
        # random_arr.append(symbol[random.randint(0, len(symbol) - 1)])
        random_arr.append(random.choice(symbols))
    for i in range(0, number_number):
        # random_arr.append(numbers[random.randint(0, len(numbers) - 1)])
        random_arr.append(random.choice(numbers))
        # return "".join(random.sample(random_arr, len(random_arr)))
        ### list reorder randomly=>shuffle change the original sequence :!
    random.shuffle(random_arr)
    return "".join(random_arr)


# you can you basically choice for getting random element into array or list


output = random_choice(number_of_alpha, number_of_Symbol, number_of_digits)
print(f"Your password :{output}")
