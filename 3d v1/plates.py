class Plate:
    # An enclosed surface on the plated whose boundaries are defined by Rifts and Subduction Zones.
    def __init__(self, id, wrapping, creation_time):
        self.id = id
        self.wrapping = wrapping
        self.creation_time = creation_time
        self.stress = 0

class Fault:
    # Fault where new crust is made.
    def __init__(self, id):
        self.id = id # Positive Ids are Rifts, Negative are Subduction Zones
        self.geometry = self.generate_fault

    def generate_rift(self):
        # Find Areas of high stress
        #   > Under Large Landmasses
        #   > Failed Rifts reactiving
        #   > Subduction Zone induced rift

        # Choose a Random Point on the Sphere
        # Pick a direction (Limited)
        # Choose a new Point

        # Flash Icon on Screen when Created (Since it may not be obvious)
        pass

    def generate_subduction_zone(self):
        # Subduction Zones will have gentler curves
        # Should generate near
        #   > Very Old Ocean Crust
        #   > Areas of conflicting plate movement
        #   > Behind Continental Movement
        pass