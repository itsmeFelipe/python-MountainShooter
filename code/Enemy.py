#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, WIN_HEIGHT, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vertical_speed = ENTITY_SPEED[self.name]
        self.moving_down = True

    def move(self):
        # Movimento horizontal (da direita para a esquerda)
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento vertical com verificação de borda
        if self.moving_down:
            self.rect.centery += self.vertical_speed * 2  # Dobrar a velocidade ao descer
            # Verificar se atingiu a borda inferior
            if self.rect.bottom >= WIN_HEIGHT:
                self.moving_down = False  # Mudar a direção para cima
        else:
            self.rect.centery -= self.vertical_speed
            # Verificar se atingiu a borda superior
            if self.rect.top <= 0:
                self.moving_down = True  # Mudar a direção para baixo
