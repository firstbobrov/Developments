class car:
    def __init__(self,number,speed):
        self.number = number
        self.speed = speed
        if speed > 60:
            if number[1] != number[2] and number[2] != number[3] and number[1] != number[3]:
                self.taxe = 100
            elif number[1] == number[2] == number[3]:
                self.taxe = 1000
            else:
                self.taxe = 500
        else:
            self.taxe = 0
totaltaxe = 0
c = 1
while True:
    print("машина №",c)
    newcar = car(str(input("введите номер: ")),int(input("введите скорость: ")))
    if newcar.number == "Б000ОС":
        break
    else:
        totaltaxe += newcar.taxe
    c += 1
print("сумма штрафов за день:", totaltaxe)
