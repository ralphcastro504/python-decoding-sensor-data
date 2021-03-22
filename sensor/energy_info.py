from house_info import HouseInfo
from datetime import date
from datetime import datetime


class EnergyData(HouseInfo):
    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0xF0

    def _get_energy(self, rec):
        energy = int(rec, base=16)
        energy = energy | ENER