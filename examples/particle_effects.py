"""
Example: Particle Systems and Physics
Demonstrates particle system with gravity, velocity, and color interpolation.
"""

from geosandbox.physics import ParticleSystem, Particle, Vec3, Color
import math


def example_fireworks():
    """Create a fireworks explosion effect."""
    system = ParticleSystem()
    
    # Center position
    center = Vec3(x=200, y=150, z=0)
    
    # Create particles radiating outward
    num_particles = 20
    for i in range(num_particles):
        angle = (i / num_particles) * 2 * math.pi
        speed = 300
        
        vel = Vec3(
            x=math.cos(angle) * speed,
            y=math.sin(angle) * speed,
            z=0
        )
        
        particle = Particle(
            pos=center,
            vel=vel,
            acc=Vec3(x=0, y=500, z=0),  # Gravity downward
            life=2.0,  # 2 seconds
            age=0,
            start_color=(255, 200, 0, 255),    # Yellow-orange
            end_color=(255, 50, 0, 0),         # Red-transparent
            start_size=8.0,
            end_size=2.0,
        )
        system.add(particle)
    
    print(f"Fireworks: {system.count()} particles created")
    
    # Simulate 0.5 seconds
    dt = 0.016  # 60 FPS
    time = 0
    while time < 0.5:
        system.update(dt)
        time += dt
    
    print(f"After 0.5s: {system.count()} particles still alive")


def example_rain():
    """Create a rain particle effect."""
    system = ParticleSystem()
    
    # Create falling particles
    import random
    random.seed(42)
    
    for _ in range(50):
        x = random.uniform(0, 400)
        y = random.uniform(-100, 0)  # Start above screen
        
        particle = Particle(
            pos=Vec3(x=x, y=y, z=0),
            vel=Vec3(x=0, y=300, z=0),  # Falling
            acc=Vec3(x=0, y=0, z=0),    # No gravity for rain
            life=3.0,
            age=0,
            start_color=(100, 150, 255, 200),    # Light blue
            end_color=(100, 150, 255, 0),        # Fade to transparent
            start_size=2.0,
            end_size=1.0,
        )
        system.add(particle)
    
    print(f"\nRain: {system.count()} water drops")
    
    # Simulate
    for _ in range(int(3.0 / 0.016)):
        system.update(0.016)
    
    print(f"After 3s: {system.count()} drops remaining")


def example_smoke():
    """Create drifting smoke effect."""
    system = ParticleSystem()
    
    import random
    random.seed(42)
    
    # Emit particles continuously
    for emit_time in range(0, 2, 1):  # Emit for 2 seconds
        x = 200 + random.uniform(-10, 10)
        y = 300
        
        particle = Particle(
            pos=Vec3(x=x, y=y, z=0),
            vel=Vec3(
                x=random.uniform(-30, 30),  # Random drift
                y=-100,                      # Upward
                z=0
            ),
            acc=Vec3(x=0, y=-50, z=0),  # Slight gravity
            life=2.0,
            age=0,
            start_color=(200, 200, 200, 255),    # White
            end_color=(50, 50, 50, 0),           # Dark fade
            start_size=15.0,
            end_size=30.0,  # Expand as it fades
        )
        system.add(particle)
    
    print(f"\nSmoke: {system.count()} smoke particles emitted")


def example_physics_simulation():
    """Detailed physics simulation of a single particle."""
    particle = Particle(
        pos=Vec3(x=0, y=0, z=0),
        vel=Vec3(x=100, y=100, z=0),      # 100 m/s at 45°
        acc=Vec3(x=0, y=-981, z=0),       # Earth gravity (9.81 m/s²)
        life=10.0,
        age=0,
        start_color=(255, 0, 0, 255),
        end_color=(255, 0, 0, 0),
        start_size=5.0,
        end_size=5.0,
    )
    
    print(f"\nProjectile motion simulation:")
    print(f"Initial velocity: {particle.vel.x:.0f} m/s (x), {particle.vel.y:.0f} m/s (y)")
    print(f"Gravity acceleration: {particle.acc.y:.0f} m/s²")
    
    max_height = particle.pos.y
    impact_time = None
    
    dt = 0.01  # 10ms timesteps
    while particle.age < particle.life:
        particle.update(dt)
        
        if particle.pos.y > max_height:
            max_height = particle.pos.y
        
        if particle.pos.y <= 0 and impact_time is None:
            impact_time = particle.age
            break
    
    print(f"Max height: {max_height:.0f} m")
    print(f"Time to impact: {impact_time:.2f} s")
    print(f"Final position: ({particle.pos.x:.0f}, {particle.pos.y:.0f})")


def example_color_interpolation():
    """Demonstrate color and size interpolation."""
    particle = Particle(
        pos=Vec3(0, 0, 0),
        vel=Vec3(0, 0, 0),
        acc=Vec3(0, 0, 0),
        life=1.0,
        age=0,
        start_color=(255, 0, 0, 255),      # Opaque red
        end_color=(0, 0, 255, 0),          # Transparent blue
        start_size=20.0,
        end_size=5.0,
    )
    
    print(f"\nColor interpolation over time:")
    print(f"Time(%) | Color (RGBA)        | Size")
    print(f"--------|---------------------|------")
    
    for percent in [0, 25, 50, 75, 100]:
        particle.age = (percent / 100.0) * particle.life
        color = particle.color()
        size = particle.size()
        
        print(f"{percent:3d}%   | {color} | {size:4.1f}")


if __name__ == "__main__":
    print("=" * 70)
    print("PARTICLE SYSTEMS AND PHYSICS EXAMPLES")
    print("=" * 70)
    
    example_fireworks()
    example_rain()
    example_smoke()
    example_physics_simulation()
    example_color_interpolation()
    
    print("\n" + "=" * 70)
    print("✓ Examples completed")
