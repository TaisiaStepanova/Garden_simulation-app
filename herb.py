import random

class Herb:  # Все растения
    def __init__(self, life_day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        self.__age = life_day
        self.__disease = disease
        self.__pest = pest
        self.__harvest_day = harvest_day

    def pest_control(self) -> None:
        if self.__pest is True:
            self.__pest = False
            print('Растение успешно обработано от вредителей')
        else:
            print('Растению не нужна обработка от вредителей')

    def disease_control(self) -> None:
        if self.__disease is True:
            self.__disease = False
            print('Растение успешно вылечено от болезней')
        else:
            print('Растение не заражено болезнями')

    def get_age(self) -> int:
        return self.__age

    def get_name(self) -> str:
        return "None"

    def day(self) -> None:
        self.__age += 1

    def get_info(self) -> dict:
        tmp_dict = {"ill": self.__disease, "pest": self.__pest, "life_day": self.__age,
                    "harvest_day": self.__harvest_day, "type": self.get_name()}
        return tmp_dict

    def get_ill(self) -> bool:
        return self.__disease

    def get_pest(self) -> bool:
        return self.__pest

    def get_harvest_day(self) -> int:
        return self.__harvest_day

    def harvesting(self) -> None:
        self.__harvest_day = 0

    def plus_harvest_day(self) -> None:
        self.__harvest_day += 1

    def maybe_ill_pest(self) -> None:
        if not self.get_pest():
            if random.choice([1, 2, 3, 4, 5]) == 1:
                self.__pest = True
        if not self.get_ill():
            if random.choice([1, 2, 3, 4, 5]) == 1:
                self.__disease = True


class Tree(Herb):  # Деревья
    def __init__(self, life_day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(life_day, harvest_day, disease, pest)
        self.__fruiting_period = 5
        self.__growth_time = 7

    def check_harvest(self) -> bool:
        if super().get_harvest_day() >= self.__fruiting_period:
            return True
        else:
            return False

    def day(self) -> None:
        super().day()
        if super().get_age() >= self.__growth_time:
            super().plus_harvest_day()

    def maybe_adult(self):
        if super().get_age() >= self.__growth_time:
            return True
        return False


class AppleTree(Tree):  # Яблоня
    def __init__(self, life_day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(life_day, harvest_day, disease, pest)
        self.__name = 'apple'
        self.__lifetime = 22
        self.__crop_price = 20

    def get_name(self) -> str:
        return self.__name

    def harvesting(self) -> int:
        super().harvesting()
        return self.__crop_price

    def check_alive(self) -> bool:
        if super().get_pest() and super().get_ill():
            return False
        elif super().get_age() >= self.__lifetime:
            return False
        else:
            return True


class PeerTree(Tree):  # Груша
    def __init__(self, life_day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(life_day, harvest_day, disease, pest)
        self.__name = 'pear'
        self.__lifetime = 20
        self.__crop_price = 20

    def get_name(self) -> str:
        return self.__name

    def harvesting(self) -> int:
        super().harvesting()
        return self.__crop_price

    def check_alive(self) -> bool:
        if super().get_pest() and super().get_ill():
            return False
        elif super().get_age() >= self.__lifetime:
            return False
        else:
            return True


class CultivatedPlant(Herb):  # Культурные растения
    def __init__(self, water: int, fertilizer: int, life_day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(life_day, harvest_day, disease, pest)
        self.__water_lvl = water
        self.__fertilization_lvl = fertilizer
        self.__fruiting_period = 3
        self.__growth_time = 4

    def check_harvest(self) -> bool:
        if super().get_harvest_day() >= self.__fruiting_period:
            return True
        else:
            return False

    def water_level(self) -> int:
        return self.__water_lvl

    def set_water_level(self, num: int) -> None:
        self.__water_lvl = num

    def fertilization_level(self) -> int:
        return self.__fertilization_lvl

    def set_fertilization_level(self, num: int) -> None:
        self.__fertilization_lvl = num

    def water(self) -> None:  # Полить
        self.__water_lvl = 100

    def fertilize(self) -> None:  # Удобрить
        self.__fertilization_lvl = 100

    def get_info(self) -> dict:
        tmp_dict = super().get_info()
        tmp_dict["water"] = self.__water_lvl
        tmp_dict["level_fertilization"] = self.__fertilization_lvl
        return tmp_dict

    def get_short_info(self) -> str:
        if super().get_ill():
            tmp_str = "Ill+|"
        else:
            tmp_str = "Ill-|"
        if super().get_pest():
            tmp_str = tmp_str + "Pest+|"
        else:
            tmp_str = tmp_str + "Pest-|"
        if self.check_harvest():
            tmp_str = tmp_str + "Harvest+|"
        else:
            tmp_str = tmp_str + "Harvest-|"
        tmp_str = tmp_str + "Water-{}".format(self.__water_lvl) + "|Fertiliser-{}|".format(self.__fertilization_lvl)
        return tmp_str

    def get_info_about_plant(self):
        info = {}
        info['Ill'] = super().get_ill()
        info['Pest'] = super().get_pest()
        info['Harvest'] = self.check_harvest()
        info['Water'] = self.__water_lvl
        info['Fertiliser'] = self.__fertilization_lvl
        return info

    def min_w(self, num: int) -> None:
        self.__water_lvl -= num

    def day(self) -> None:
        super().day()
        if super().get_age() >= self.__growth_time:
            super().plus_harvest_day()

    def maybe_adult(self):
        if super().get_age() >= self.__growth_time:
            return True
        return False


class Potato(CultivatedPlant):
    def __init__(self, water: int, fertilizer: int, day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(water, fertilizer, day, harvest_day, disease, pest)
        self.__name = 'potato'
        self.__lifetime = 10
        self.__crop_price = 10
        self.__water_consumption = 5
        self.__fertilizer_consumption = 5

    def day(self) -> None:
        super().day()
        super().set_water_level(super().water_level() - self.__water_consumption)
        super().set_fertilization_level(super().fertilization_level() - self.__fertilizer_consumption)

    def get_name(self) -> str:
        return self.__name

    def harvesting(self) -> int:
        super().harvesting()
        return self.__crop_price

    def check_alive(self) -> bool:
        if super().water_level() < 0 or super().fertilization_level() < 0:
            return False
        elif super().get_age() >= self.__lifetime:
            return False
        else:
            return True


class Tomato(CultivatedPlant):
    def __init__(self, water: int, fertilizer: int, day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(water, fertilizer, day, harvest_day, disease, pest)
        self.__name = 'tomato'
        self.__lifetime = 14
        self.__crop_price = 14
        self.__water_consumption = 10
        self.__fertilizer_consumption = 15

    def day(self) -> None:
        super().day()
        super().set_water_level(super().water_level() - self.__water_consumption)
        super().set_fertilization_level(super().fertilization_level() - self.__fertilizer_consumption)

    def get_name(self) -> str:
        return self.__name

    def harvesting(self) -> int:
        super().harvesting()
        return self.__crop_price

    def check_alive(self) -> bool:
        if super().water_level() < 0 or super().fertilization_level() < 0:
            return False
        elif super().get_age() >= self.__lifetime:
            return False
        else:
            return True


class Pepper(CultivatedPlant):
    def __init__(self, water: int, fertilizer: int, day: int, harvest_day: int, disease: bool, pest: bool) -> None:
        super().__init__(water, fertilizer, day, harvest_day, disease, pest)
        self.__name = 'pepper'
        self.__lifetime = 12
        self.__crop_price = 12
        self.__water_consumption = 10
        self.__fertilizer_consumption = 10

    def day(self) -> None:
        super().day()
        super().set_water_level(super().water_level() - self.__water_consumption)
        super().set_fertilization_level(super().fertilization_level() - self.__fertilizer_consumption)

    def get_name(self) -> str:
        return self.__name

    def harvesting(self) -> int:
        super().harvesting()
        return self.__crop_price

    def check_alive(self) -> bool:
        if super().water_level() < 0 or super().fertilization_level() < 0:
            return False
        elif super().get_age() >= self.__lifetime:
            return False
        else:
            return True