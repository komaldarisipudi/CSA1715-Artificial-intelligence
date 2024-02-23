% Facts: Planets and their distances from the sun (in astronomical units, AE)
ae(mercury, 0.39).
ae(venus, 0.72).
ae(earth, 1).
ae(mars, 1.52).
ae(jupiter, 5.20).
ae(saturn, 9.54).
ae(uranus, 19.22).
ae(neptune, 30.06).

% Moons orbiting planets
orbits(moon, earth).
orbits(deimos, mars).
orbits(phobos, mars).
orbits(ganymede, jupiter).
orbits(callisto, jupiter).
orbits(io, jupiter).
orbits(europa, jupiter).
orbits(titan, saturn).
orbits(enceladus, saturn).
orbits(titania, uranus).
orbits(oberon, uranus).
orbits(umbriel, uranus).
orbits(ariel, uranus).
orbits(miranda, uranus).
orbits(triton, neptune).

% Predicate to find moons of a given planet
moons_of_planet(Planet, Moons) :-
    findall(Moon, orbits(Moon, Planet), Moons).

% Example usage:
% ?- moons_of_planet(jupiter, JupiterMoons).
% JupiterMoons = [ganymede, callisto, io, europa].
