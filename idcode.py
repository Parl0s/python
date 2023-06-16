def quit_check(data: str) -> bool:
    if data.lower() == "exit":
        return True
    return False


def check_user_input(data: str) -> bool:
    if not data.isdigit():
        print("ID code must contain only digits")
        return False
    if len(data) > 11:
        print("ID code too long")
        return False
    elif len(data) < 11:
        print("ID code too short")
        return False
    return True


def get_gender(data: int) -> str:
    if data % 2 == 0:
        return "female"
    return "male"


def get_century(data: str) -> int:
    if data in "12":
        return 18
    elif data in "34":
        return 19
    elif data in "56":
        return 20
    elif data in "78":
        return 21


def get_region(data: int) -> str:
    if 1 <= data <= 10:
        return "Kuressaare haigla"
    elif 11 <= data <= 19:
        return "Tartu Ülikooli Naistekliinik"
    elif 21 <= data <= 150:
        return "Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)"
    elif 151 <= data <= 160:
        return "Keila haigla"
    elif 161 <= data <= 220:
        return "Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)"
    elif 221 <= data <= 270:
        return "Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= data <= 370:
        return "Maarjamõisa kliinikum (Tartu), Jõgeva haigla"
    elif 371 <= data <= 420:
        return "Narva haigla"
    elif 421 <= data <= 470:
        return "Pärnu haigla"
    elif 471 <= data <= 490:
        return "Haapsalu haigla"
    elif 491 <= data <= 520:
        return "Järvamaa haigla (Paide)"
    elif 521 <= data <= 570:
        return "Rakvere haigla, Tapa haigla"
    elif 571 <= data <= 600:
        return "Valga haigla"
    elif 601 <= data <= 650:
        return "Viljandi haigla"
    elif 651 <= data <= 700:
        return "Lõuna-Eesti haigla (Võru), Põlva haigla"
    else:
        return "Random place"


def calculate_checksum(id_code: str, numbers: str) -> int:
    result = 0
    for i in range(10):
        result += int(id_code[i]) * int(numbers[i])
    return result


def get_control_number(data: str) -> int:
    first_numbers = "1234567891"
    first_checksum = calculate_checksum(data, first_numbers) % 11
    if first_checksum < 10:
        return first_checksum
    second_numbers = "3456789123"
    second_checksum = calculate_checksum(data, second_numbers) % 11
    if second_checksum < 10:
        return second_checksum
    return 0


def switch_menu_items(item: int, id_code: str) -> bool:
    if item == 1:
        gender = get_gender(int(id_code[0]))
        print("This id code belongs to " + gender)
        return True
    elif item == 2:
        print(f"{id_code[5:7]}.{id_code[3:5]}.{get_century(id_code[0])}{id_code[1:3]}")
        return True
    elif item == 3:
        print(f"The place of birth is {get_region(int(id_code[7:10]))}")
        return True
    elif item == 4:
        print(f"Control number has to be {get_control_number(id_code)}")
        return True
    return False


if __name__ == '__main__':
    while True:
        user_input = input("Enter ID code: ")
        if quit_check(user_input):
            quit()
        if not check_user_input(user_input):
            continue
        while True:
            user_menu = input("Enter: 1) gender\n2) date\n3) region\n4) validation\n")
            if not switch_menu_items(int(user_menu), user_input):
                continue
            break

