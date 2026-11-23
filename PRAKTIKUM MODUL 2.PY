class Hero:
    # Variabel class (private): menghitung total Hero yang dibuat
    __jumlah = 0

    def __init__(self, nama, health, attPower, armor):
        # Base stats (private)
        self.__name = nama
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor

        # Level dan EXP
        self.__level = 1
        self.__exp = 0

        # Atribut dinamis (bergantung pada level)
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        # Darah saat ini
        self.__health = self.__healthMax

        # Tambah jumlah Hero
        Hero.__jumlah += 1

    # Getter gainEXP (hanya formalitas agar setter bisa berfungsi)
    @property
    def gainEXP(self):
        pass

    # Setter gainEXP: gerbang penambahan EXP + logika level up
    @gainEXP.setter
    def gainEXP(self, addEXP):
        self.__exp += addEXP

        while self.__exp >= 100:
            print(f"{self.__name} level up")
            self.__level += 1
            self.__exp -= 100

            # Hitung ulang atribut dinamis berdasarkan level baru
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
            self.__health = self.__healthMax  # darah terisi penuh saat level up

    # Method attack
    def attack(self, musuh):
        self.gainEXP = 50

    # Read-only property (hanya getter)
    @property
    def info(self):
        return (f"{self.__name} level {self.__level}: \n"
                f"\thealth = {self.__health}/{self.__healthMax} \n"
                f"\tattack = {self.__attPower} \n"
                f"\tarmor = {self.__armor}")


# ===== Test Case =====
sora = Hero('sora', 100, 5, 10)
cici = Hero('cici', 100, 5, 10)
print(sora.info)

sora.attack(cici)
sora.attack(cici)
sora.attack(cici)

print(sora.info)
print(cici.info)
