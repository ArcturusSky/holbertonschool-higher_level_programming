#!/usr/bin/env python3
"""Module that demonstrates Multiple Inheritance."""


class Fish:
    """Class representing a fish with swimming and habitat behaviors."""

    def swim(self):
        """Print a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message about the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird with flying and habitat behaviors."""

    def fly(self):
        """Print a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message about the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Print a message indicating the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a message indicating the flying fish is swimming."""
        print("The flying fish is swimming")

    def habitat(self):
        """Print a message about the flying fish's dual habitat."""
        print("The flying fish lives both in water and the sky!")
