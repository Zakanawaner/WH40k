from Objects.Races.Humans import Human
from Objects.Armies.DarkAngels import Mesh, Weapons as DarkAngelWeapons


class Infantry:
    def __init__(self):
        self.POINTS = 0
        self.M = 6
        self.WS = 3
        self.BS = 3
        self.S = 4
        self.T = 4
        self.W = 1
        self.A = 1
        self.Ld = 7
        self.Sv = 3
        self.InvSv = 0
        self.Gun1 = None
        self.Gun2 = None
        self.Gun3 = None
        self.Gun4 = None

    def replace_gun_1(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun1.POINTS if self.Gun1 is not None else 0
            self.Gun1 = weapon
            self.POINTS += self.Gun1.POINTS

    def replace_gun_2(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun2.POINTS if self.Gun2 is not None else 0
            self.Gun2 = weapon
            self.POINTS += self.Gun2.POINTS

    def replace_gun_3(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun3.POINTS if self.Gun3 is not None else 0
            self.Gun3 = weapon
            self.POINTS += self.Gun3.POINTS

    def replace_gun_4(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun4.POINTS if self.Gun4 is not None else 0
            self.Gun4 = weapon
            self.POINTS += self.Gun4.POINTS


class Sergeant:
    def __init__(self):
        self.A += 1
        self.Ld += 1
        self.Gun5 = None

    # Sergeant weapons List
    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        if sergeant_weapon_1 is not None:
            self.POINTS -= self.Gun1.POINTS
            self.Gun1 = sergeant_weapon_1
            self.POINTS += self.Gun1.POINTS
        if sergeant_weapon_2 is not None:
            self.POINTS -= self.Gun2.POINTS
            self.Gun2 = sergeant_weapon_2
            self.POINTS += self.Gun2.POINTS


class Vehicle:
    def __init__(self):
        self.POINTS = 0
        self.M = 6
        self.WS = 3
        self.BS = 3
        self.S = 6
        self.T = 7
        self.W = 8
        self.A = 4
        self.Ld = 8
        self.Sv = 3
        self.InvSv = 0
        self.Gun1 = None
        self.Gun2 = None
        self.Gun3 = None
        self.Gun4 = None
        self.Gun5 = None
        self.Gun6 = None
        self.FirstM = 9
        self.SecondM = 6
        self.ThirdM = 3
        self.FirstWS = 2
        self.SecondWS = 3
        self.ThirdWS = 4
        self.FirstBS = 2
        self.SecondBS = 3
        self.ThirdBS = 4
        self.FirstW = 6
        self.SecondW = 3

    def replace_gun_1(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun1.POINTS if self.Gun1 is not None else 0
            self.Gun1 = weapon
            self.POINTS += self.Gun1.POINTS

    def replace_gun_2(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun2.POINTS if self.Gun2 is not None else 0
            self.Gun2 = weapon
            self.POINTS += self.Gun2.POINTS

    def replace_gun_3(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun3.POINTS if self.Gun3 is not None else 0
            self.Gun3 = weapon
            self.POINTS += self.Gun3.POINTS

    def replace_gun_4(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun4.POINTS if self.Gun4 is not None else 0
            self.Gun4 = weapon
            self.POINTS += self.Gun4.POINTS

    def replace_gun_5(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun5.POINTS if self.Gun5 is not None else 0
            self.Gun5 = weapon
            self.POINTS += self.Gun5.POINTS

    def replace_gun_6(self, weapon=None):
        if weapon is not None:
            self.POINTS -= self.Gun6.POINTS if self.Gun6 is not None else 0
            self.Gun6 = weapon
            self.POINTS += self.Gun6.POINTS

    def damage_update(self):
        if self.W >= self.FirstW:
            self.M = self.FirstM
            self.WS = self.FirstWS
            self.BS = self.FirstBS
        if self.FirstW > self.W >= self.SecondW:
            self.M = self.SecondM
            self.WS = self.SecondWS
            self.BS = self.SecondBS
        if self.W < self.SecondW:
            self.M = self.ThirdM
            self.WS = self.ThirdWS
            self.BS = self.ThirdBS


class TacticalMarine(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.TacticalMarineBolter)
        self.POINTS = 13
        self.Gun1 = DarkAngelWeapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = DarkAngelWeapons.Boltgun()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = DarkAngelWeapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = DarkAngelWeapons.KrakGrenade()
        self.POINTS += self.Gun4.POINTS


class TacticalMarineSergeant(TacticalMarine, Sergeant):
    def __init__(self):
        super().__init__()

    def take_melta_bombs(self):
        self.Gun5 = DarkAngelWeapons.MeltaBomb()


class Intercessor(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.PrimarisIntercessor)
        self.POINTS = 18
        self.W += 1
        self.A += 1
        self.Gun1 = DarkAngelWeapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = DarkAngelWeapons.BoltRifle()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = DarkAngelWeapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = DarkAngelWeapons.KrakGrenade()
        self.POINTS += self.Gun4.POINTS


class IntercessorSergeant(Intercessor, Sergeant):
    def __init__(self):
        super().__init__()

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass

    def take_power_sword(self):
        self.Gun5 = DarkAngelWeapons.PowerSword(A=self.A, S=self.S)
        self.POINTS += self.Gun5.POINTS


class Scout(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.ScoutBolter)
        self.POINTS = 11
        self.Sv += 1
        self.Gun1 = DarkAngelWeapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = DarkAngelWeapons.Boltgun()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = DarkAngelWeapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = DarkAngelWeapons.KrakGrenade()
        self.POINTS += self.Gun4.POINTS
        self.camo_cloak = False

    def take_camo_cloak(self):
        self.camo_cloak = True
        self.POINTS += 3


class ScoutSergeant(Scout, Sergeant):
    def __init__(self):
        super().__init__()

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass


class Veteran(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.VanguardVeteranBoltPistol_ChainSword)
        self.POINTS = 16
        self.A += 1
        self.Ld += 1
        self.Gun1 = DarkAngelWeapons.BoltPistol()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = DarkAngelWeapons.ChainSword(A=self.A, S=self.S)
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = DarkAngelWeapons.FragGrenade()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = DarkAngelWeapons.KrakGrenade()
        self.POINTS += self.Gun4.POINTS

    # Storm Shield or Melee weapons or Pistols List
    def replace_gun_1(self, weapon=None):
        self.POINTS -= self.Gun1.POINTS
        self.Gun1 = weapon
        if weapon is not None:
            self.POINTS += self.Gun1.POINTS
        else:
            self.InvSv = 3
            self.POINTS += 5

    # Storm Shield (weapon=None) or BoltGun or Melee weapons or Pistols list or Combi weapons or Special Weapons
    def replace_gun_2(self, weapon=None):
        self.POINTS -= self.Gun2.POINTS
        self.Gun2 = weapon
        if weapon is not None:
            self.POINTS += self.Gun2.POINTS
        else:
            self.InvSv = 3
            self.POINTS += 5

    def take_combat_shield(self):
        self.InvSv = 5
        self.POINTS += 4


class VeteranSergeant(Veteran, Sergeant):
    def __init__(self):
        super().__init__()


class DeathWingTerminator(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.TerminatorPowerfist_Stormbolter)
        self.POINTS = 26
        self.M -= 1
        self.W += 1
        self.A += 1
        self.Ld += 1
        self.Sv -= 1
        self.Gun1 = DarkAngelWeapons.PowerFist(A=self.A, S=self.S)
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = DarkAngelWeapons.StormBolter()
        self.POINTS += self.Gun2.POINTS


class DeathWingTerminatorSergeant(DeathWingTerminator, Sergeant):
    def __init__(self):
        super().__init__()

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass


class DeathWingKnight(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.DeathwingKnightMace)
        self.POINTS = 45
        self.M -= 1
        self.W += 1
        self.A += 1
        self.Ld += 1
        self.Sv -= 1
        self.Gun1 = DarkAngelWeapons.MaceOfAbsolution(A=self.A, S=self.S)
        self.POINTS += self.Gun1.POINTS
        self.InvSv = 3
        self.POINTS += 5


class DeathWingKnightMaster(DeathWingKnight, Sergeant):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.DeathingKnightFlail)
        self.POINTS += self.Gun1.POINTS
        self.Gun1 = DarkAngelWeapons.FlailOfTheUnforgiven(A=self.A, S=self.S)
        self.POINTS += self.Gun1.POINTS

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass


class DeathWingCataphractiiTerminator(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self)  # TODO Not Mesh
        self.POINTS = 30
        self.M -= 2
        self.W += 1
        self.A += 1
        self.Ld += 1
        self.Sv -= 1
        self.Gun1 = DarkAngelWeapons.CombiBolter()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = DarkAngelWeapons.PowerFist(A=self.A, S=self.S)
        self.POINTS += self.Gun2.POINTS


class DeathWingCataphractiiTerminatorSergeant(DeathWingCataphractiiTerminator, Sergeant):
    def __init__(self):
        DeathWingCataphractiiTerminator.__init__(self)
        Sergeant.__init__(self)
        self.POINTS += self.Gun2.POINTS
        self.Gun2 = DarkAngelWeapons.PowerSword(A=self.A, S=self.S)
        self.POINTS += self.Gun2.POINTS

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass

    def take_grenade_harness(self):
        self.Gun3 = DarkAngelWeapons.GrenadeHarness()
        self.POINTS += self.Gun3.POINTS


class DeathWingTartarosTerminator(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self)  # TODO Not Mesh
        self.POINTS = 26
        self.W += 1
        self.A += 1
        self.Ld += 1
        self.Sv -= 1
        self.Gun1 = DarkAngelWeapons.CombiBolter()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = DarkAngelWeapons.PowerFist(A=self.A, S=self.S)
        self.POINTS += self.Gun2.POINTS

    def take_grenade_harness(self):
        self.Gun3 = DarkAngelWeapons.GrenadeHarness()
        self.POINTS += self.Gun3.POINTS


class DeathWingTartarosTerminatorSergeant(DeathWingTartarosTerminator, Sergeant):
    def __init__(self):
        DeathWingTartarosTerminator.__init__(self)
        Sergeant.__init__(self)
        self.POINTS += self.Gun2.POINTS
        self.Gun2 = DarkAngelWeapons.PowerSword(A=self.A, S=self.S)
        self.POINTS += self.Gun2.POINTS

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass


class Dreadnought(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.Dreadnought_CombatWeapon_AssaultCannon)
        self.POINTS = 70
        self.Gun1 = DarkAngelWeapons.AssaultCannon()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = DarkAngelWeapons.StormBolter()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = DarkAngelWeapons.DreadnoughtCombatWeapon(A=self.A, S=self.S)
        self.POINTS += self.Gun3.POINTS

    def damage_update(self):
        pass


class VenerableDreadnought(Dreadnought):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.VenerableDreadnought3_3Autocannon_Assaultcannon)
        self.POINTS = 90
        self.WS = 2
        self.BS = 2

    def damage_update(self):
        pass


class ContemptorDreadnought(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self)  # TODO Not Mesh
        self.POINTS = 98
        self.T = 7
        self.W = 10
        self.InvSv = 5
        self.damage_update()
        self.Gun1 = DarkAngelWeapons.MultiMelta()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = DarkAngelWeapons.CombiBolter()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = DarkAngelWeapons.DreadnoughtCombatWeapon(A=self.A, S=self.S)
        self.POINTS += self.Gun3.POINTS


class RedemptorDreadnought(Vehicle, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.RedemptorDreadnought)
        self.POINTS = 140
        self.T = 7
        self.W = 13
        self.InvSv = 5
        self.FirstW = 7
        self.SecondW = 4
        self.FirstM = 8
        self.SecondM = 6
        self.FirstWS = 3
        self.SecondWS = 4
        self.ThirdWS = 5
        self.FirstBS = 3
        self.SecondBS = 4
        self.ThirdBS = 5
        self.damage_update()
        self.Gun1 = DarkAngelWeapons.HeavyOnslaughtGatlingCannon()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = DarkAngelWeapons.HeavyFlamer()
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = DarkAngelWeapons.FragStormGrenadeLauncher()
        self.POINTS += self.Gun3.POINTS
        self.Gun4 = DarkAngelWeapons.FragStormGrenadeLauncher()
        self.POINTS += self.Gun4.POINTS
        self.Gun5 = DarkAngelWeapons.RedemptorFist(A=self.A, S=self.S)
        self.POINTS += self.Gun5.POINTS


class Aggressor(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self, Mesh.PrimarisAggressor)
        self.POINTS = 21
        self.M = 5
        self.T = 5
        self.W = 2
        self.A = 2
        self.Gun1 = DarkAngelWeapons.AutoboltStormGauntlets()
        self.POINTS += self.Gun1.POINTS
        self.Gun2 = DarkAngelWeapons.AutoboltStormGauntletsMelee(A=self.A, S=self.S)
        self.POINTS += self.Gun2.POINTS
        self.Gun3 = DarkAngelWeapons.FragStormGrenadeLauncher()
        self.POINTS += self.Gun3.POINTS


class AggressorSergeant(Aggressor, Sergeant):
    def __init__(self):
        Aggressor.__init__(self)
        Sergeant.__init__(self)

    def choose_sergeant_weapon(self, sergeant_weapon_1=None, sergeant_weapon_2=None):
        pass


class Servitor(Infantry, Human):
    def __init__(self):
        super().__init__()
        Human.__init__(self)  # TODO not mesh
        self.POINTS = 2
        self.M = 5
        self.WS = 5
        self.BS = 5
        self.S = 3
        self.T = 3
        self.Ld = 6
        self.Sv = 4
        self.Gun1 = DarkAngelWeapons.ServoArm(A=self.A, S=self.S)
        self.POINTS += self.Gun1.POINTS