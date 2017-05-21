README
------

Erklärung der Lauzeitprotokolle:

Cycle 0 : Nest = (2, 3) , {(1, 1): (0, []), (1, 2): (67, []), (1, 3): (0, []), (2, 1): (0, []), (2, 2): (0, []), (2, 3): (0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (3, 1): (68, []), (3, 2): (0, []), (3, 3): (0, [])} 
		 [((1, 1), (2, 1), 0.0, 0.0), ((1, 1), (1, 2), 0.0, 0.0), ((1, 2), (2, 2), 0.0, 0.0), ((1, 2), (1, 3), 0.0, 0.0), ((1, 3), (2, 3), 0.0, 0.0), ((2, 1), (3, 1), 0.0, 0.0), ((2, 1), (2, 2), 0.0, 0.0), ((2, 2), (3, 2), 0.0, 0.0), ((2, 2), (2, 3), 0.0, 0.0), ((2, 3), (3, 3), 0.0, 0.0), ((3, 1), (3, 2), 0.0, 0.0), ((3, 2), (3, 3), 0.0, 0.0)]
		 
Für jeden Zyklus der Ameisenweltsimulation wird der Zustand der Welt in dieser Form dargestellt:
Cycle X: X-ter Zyklus der Simulation
Nest = (X, Y): Die Koordinaten des Nestknotens im Kotengitter.
{(X, Y): (F, [A1, A2, ...]), ...}: Liste aller Knoten im Gitter. (X, Y) ist die Koordinate des jeweiligen Knoten. F ist die Anzahl der dort vorhandenen Essenseinheiten.
	[A1, A2, ...] ist eine Liste mit den sich in diesem Knoten aufhaltenden Ameisen. O bedeuted, dass die Ameise keine Nahrung trägt. 1 bedeuted, dass die Ameise Nahrung trägt.
[((X1, Y1), (X2, Y2), F, N), ...]: Liste aller Kanten im Gitter. (X1, Y1), (X2, Y2) sind die Knoten, die von dieser Kante verbunden werden. F ist die Stärke des Nahrungspeheromons auf dieser Kante. N ist die Stärke des Nestpheromons auf dieser Kante.