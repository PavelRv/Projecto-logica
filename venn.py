import matplotlib.pyplot as plt
from matplotlib_set_diagrams import VennDiagram


# Diagrama 4: 4 conjuntos definidos
VennDiagram(
    {
        (1, 0, 0, 0): 4.0,
        (0, 1, 0, 0): 3.0,
        (0, 0, 1, 0): 2.0,
        (0, 0, 0, 1): 1.0,
        (1, 1, 0, 0): 0.9,
        (1, 0, 1, 0): 0.8,
        (1, 0, 0, 1): 0.7,
        (0, 1, 1, 0): 0.6,
        (0, 1, 0, 1): 0.5,
        (0, 0, 1, 1): 0.4,
        (1, 1, 1, 0): 0.3,
        (1, 1, 0, 1): 0.25,
        (1, 0, 1, 1): 0.2,
        (0, 1, 1, 1): 0.15,
        (1, 1, 1, 1): 0.1,
    }
    )
plt.show()
