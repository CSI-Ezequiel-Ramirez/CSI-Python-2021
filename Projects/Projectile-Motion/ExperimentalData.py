import json
import math
#Module 6
class ExperimentalData:
    def __init__(self, WeaponName:str, CartridgeCaliber:str, AmmunitionType:str, Velocity:int, BuildingName:str, BuildingHeight:int, Gravity:int) -> None: 
    

        self.WeaponName = WeaponName
        self.CartridgeCaliber = CartridgeCaliber
        self.AmmunitionType = AmmunitionType
        self.Velocity = Velocity
        self.BuildingName = BuildingName
        self.BuildingHeight = BuildingHeight
        self.Gravity = Gravity