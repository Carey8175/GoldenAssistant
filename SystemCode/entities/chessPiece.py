from __future__ import annotations
from SystemCode.entities.bond import Bond
from SystemCode.entities.equipment import Equipment


class ChessPiece:
    def __init__(self):
        # --- Basic Attribute ---
        self.name = ""
        self.leveling = 1
        self.position = []
        self.is_alive = True
        self.cost = 0
        self.bond = []
        # --- Fight Attribute ---
        self.attack_damage = 0
        self.ability_power = 0
        self.mana = 0
        self.armor = 0
        self.magical_resistance = 0
        self.health = 0
        self.range = 0
        self.attack_speed = 0
        self.critical_strike_chance = 0
        self.critical_strike_damage = 0
        self.move_speed = 0

    def attack(self, target: ChessPiece):
        pass

    def use_ability(self, target: ChessPiece):
        pass

    def move_to(self, position: list):
        pass

    def apply_equipment(self, equipment: Equipment):
        pass

    def apply_bond(self, bond: Bond):
        pass
