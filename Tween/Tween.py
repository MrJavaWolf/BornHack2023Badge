#!/usr/bin/python
# -*- coding: utf-8 -*-
# Src: https://github.com/Polynominal/PyFlax

import math


def linear(x: float):
    return x
def quad(x: float):
    return x * x
def quadout(x: float):
    return 1 - quad(x)
def cubic(x: float):
    return x * x * x
def cubicout(x: float):
    return 1 - cubic(x)
def quint(x: float):
    return x * x * x * x
def quintout(x: float):
    return 1 - quint(x)
def sine(x: float):
    return -math.cos(x * (math.pi * .5)) + 1
def sineout(x: float):
    return 1 - sine(x)
def cosine(x: float):
    return -math.sine(x * (math.pi * .5)) + 1
def cosineout(x: float):
    return 1 - cosine(x)

def easeOutElastic(x: float):
    c4 = (2 * math.pi) / 3
    if  x == 0:
        return 0
    if x == 1:
        return 1
    return math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * c4) + 1

def BounceEaseIn(t: float) -> float:
    return 1 - BounceEaseOut(1 - t)

def BounceEaseOut(t: float) -> float:
    if t < 4 / 11:
        return 121 * t * t / 16
    elif t < 8 / 11:
        return (363 / 40.0 * t * t) - (99 / 10.0 * t) + 17 / 5.0
    elif t < 9 / 10:
        return (4356 / 361.0 * t * t) - (35442 / 1805.0 * t) + 16061 / 1805.0
    return (54 / 5.0 * t * t) - (513 / 25.0 * t) + 268 / 25.0