class Weapon:
    def __init__(self, bullets):
        self.bullets = int(bullets)
        self.bullets_loaded = int(self.bullets)

    def shoot(self):
        if self.bullets_loaded > 0:
            self.bullets_loaded -= 1
            return "shooting..."
        else:  # here I used <= 0 in judge
            return f"no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets_loaded}"


# this is not passed to judge
weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)
