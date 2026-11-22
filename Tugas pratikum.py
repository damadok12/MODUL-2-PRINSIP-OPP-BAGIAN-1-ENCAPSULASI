class Hero:

    def __init__(self, nama, health, attPower, armor):
        self.__armorStandar = armor

        # Level & EXP
        self.__level = 1
        self.__exp = 0

        # Atribut dinamis (bergantung pada level)
        self.__healthMax = self.__healthStandard * self.__level
        self.__attPower = self.__attPowerStandard * self.__level
        self.__armor = self.__armorStandar * self.__level

        # Darah saat ini
        self.__health = self.__healthMax

        # Tambah jumlah Hero
        Hero.__jumlah += 1

    # Getter gainEXP (hanya agar setter bisa berfungsi)
    @property
    def gainEXP(self):
        pass

    # Setter gainEXP: gerbang penambahan EXP + sistem level up
    @gainEXP.setter
    def gainEXP(self, addEXP):
        self.__exp += addEXP

        while self.__exp >= 100:
            print(f"{self.__name} level up")
            self.__level += 1
            self.__exp -= 100

            # Hitung ulang atribut dinamis berdasarkan level baru
            self.__healthMax = self.__healthStandard * self.__level
            self.__attPower = self.__attPowerStandard * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self, musuh):
        self.gainEXP = 50

    # Read-only property: hanya getter
    @property
    def info(self):
        return (
            f"{self.__name} level {self.__level}: \n"
            f"\thealth = {self.__health}/{self.__healthMax} \n"
            f"\tattack = {self.__attPower} \n"
            f"\tarmor = {self.__armor}"
        )


if __name__ == "__main__":

    hero_1 = Hero("Atsu", 100, 20, 10)
    hero_2 = Hero("Budi", 80, 25, 5)

    print(hero_1.info)

    hero_1.attack(hero_2)
    hero_1.attack(hero_2)  # EXP 100 -> level up

    print(hero_1.info)