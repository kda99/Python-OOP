class SmartPhone:
    pass


class IPhone(SmartPhone):
    pass

phone = IPhone()

print(isinstance(phone, SmartPhone))