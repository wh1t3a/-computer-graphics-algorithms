"""Particle system physics simulation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

Color = tuple[int, int, int, int]


@dataclass
class Vec3:
    """3D vector for spatial calculations."""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __add__(self, other: "Vec3") -> "Vec3":
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, value: float) -> "Vec3":
        return Vec3(self.x * value, self.y * value, self.z * value)


@dataclass
class Particle:
    """Individual particle with physics and visual properties."""
    pos: Vec3
    vel: Vec3
    acc: Vec3
    life: float
    age: float
    start_color: Color
    end_color: Color
    start_size: float
    end_size: float
    spin: float = 0.0
    angle: float = 0.0
    frame_offset: int = 0

    @property
    def alive(self) -> bool:
        return self.age < self.life

    @property
    def t(self) -> float:
        return min(1.0, max(0.0, self.age / self.life))

    def update(self, dt: float) -> None:
        """Update particle physics using Euler integration."""
        self.vel = self.vel + self.acc * dt
        self.pos = self.pos + self.vel * dt
        self.age += dt
        self.angle += self.spin * dt

    def color(self) -> Color:
        """Calculate interpolated color."""
        t = self.t
        return tuple(
            int(self.start_color[i] + (self.end_color[i] - self.start_color[i]) * t)
            for i in range(4)
        )

    def size(self) -> float:
        """Calculate interpolated size."""
        return self.start_size + (self.end_size - self.start_size) * self.t


class ParticleSystem:
    """Container and manager for particle effects."""

    def __init__(self) -> None:
        self.particles: list[Particle] = []

    def add(self, particle: Particle) -> None:
        """Add a single particle."""
        self.particles.append(particle)

    def extend(self, particles: Iterable[Particle]) -> None:
        """Add multiple particles."""
        self.particles.extend(particles)

    def update(self, dt: float) -> None:
        """Update all particles and remove dead ones."""
        for particle in self.particles:
            particle.update(dt)
        self.particles = [p for p in self.particles if p.alive]

    def sort_for_transparency(self) -> None:
        """Sort particles by depth (Z) for correct transparency blending."""
        self.particles.sort(key=lambda p: p.pos.z)

    def clear(self) -> None:
        """Remove all particles."""
        self.particles.clear()

    def count(self) -> int:
        """Get number of active particles."""
        return len(self.particles)
