#!/usr/bin/env python3
"""
Module to creat abstract class
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class to be a template for other class
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Subclass of Animal to try the abstract class and
    abstract method.
    """

    def sound(self):
        """
        Function that will bark.
        """

        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal to try the abstract class and
    abstract method.
    """

    def sound(self):
        """
        Function that will meow.
        """

        return "Meow"
