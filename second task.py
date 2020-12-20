def personal(name, surname, birth_year, city, email, phone):
    return f"Вас зовут {name}, Ваша фамилия {surname}, Вы родились в {birth_year}-м году," \
           f"Вы живете в городе {city}, " \
           f"Ваш email: {email} и Ваш телефон: {phone}"


user_name = input("Как Вас зовут? ")
user_surname = input("Какая у Вас фамилия? ")
user_birth = input("В каком году Вы родились? ")
user_city = input("В каком городе вы живете? ")
user_email = input("Введите Вашу электронную почту: ")
user_phone = input("Введите Ваш номер телефона: ")

information = personal(name=user_name, surname=user_surname, birth_year=user_birth,
                       city=user_city, email=user_email, phone=user_phone)
print(information)

