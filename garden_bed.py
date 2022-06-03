from herb import*

class GardenBed:  # ГрядОчка
    def __init__(self, day: int, weed: bool, herb: bool) -> None:
        self.__DAY = day
        self.__WEED = weed
        self.__HERB = herb

    def check_herb(self) -> bool:
        if isinstance(self.__HERB, Herb):
            return True
        else:
            return False

    def get_herb(self) -> Herb:
        if isinstance(self.__HERB, Herb):
            return self.__HERB

    def plant_herb(self, cultivated_plant_name: str) -> None:
        if cultivated_plant_name == 'potato':
            self.__HERB = Potato(100, 100, 0, 0, False, False)
        elif cultivated_plant_name == 'tomato':
            self.__HERB = Tomato(100, 100, 0, 0, False, False)
        else:
            self.__HERB = Pepper(100, 100, 0, 0, False, False)

    def day(self) -> None:
        self.__DAY += 1
        if self.__DAY > 2:
            self.__WEED = True

    def weeding(self) -> None:
        self.__WEED = False

    def get_info(self) -> dict:
        tmp_dict = {"DAY": self.__DAY, "WEED": self.__WEED}
        return tmp_dict

    def get_weed(self) -> bool:
        return self.__WEED

    def set_herb(self, herb: Herb) -> None:
        self.__HERB = herb

    def water(self) -> None:
        if isinstance(self.__HERB, (Potato, Tomato, Pepper)):
            self.__HERB.water()

    def fertilize(self) -> None:
        if isinstance(self.__HERB, (Potato, Tomato, Pepper)):
            self.__HERB.fertilize()

    def del_herb(self) -> None:
        self.__HERB = False

    def maybe_weed(self) -> None:
        if random.choice([1, 2, 3]) == 1:
            self.__WEED = True