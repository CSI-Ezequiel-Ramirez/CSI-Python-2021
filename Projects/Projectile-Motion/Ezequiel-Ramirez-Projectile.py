import math
import fractions

Weapon = "ASh-12"
CartridgeCaliber = "12.7x55mm"
AmmunitionType = "12.7x55mm STs-130"
Velocity = 285 #m/s
BuildingName = "Lotte World Tower"
BuildingHeight = 555 #m

Time = round((math.sqrt((2 * -555) / -9.8)), 2) #Formula to determine amount of time
print(f"The time is {Time} seconds.")

Distance = round((Velocity) * (Time), 2) #Formula to determine the distance
print(f"The projectile will travel {Distance} meters.")

print(f"For this project, the projectile weapon being utilized is an {Weapon} assault rifle. The cartridge caliber for this gun is {CartridgeCaliber}. The only type of round this gun is compatible with is {AmmunitionType}. This type of bullets projectile velocity is {Velocity} miles per second. The gun is going to be fired off of the {BuildingName}, which is {BuildingHeight} meters high. After testing, the bullets flied for {Time} seconds and travelled {Distance} meters.")