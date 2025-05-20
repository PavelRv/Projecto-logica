import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

cantidad = int(input("Cuantos conjuntos ingresara (2 o 3)? "))
if cantidad == 2:
    # Conjunto A
    a = set()
    cantidad_a = int(input("Cuantos elementos tendra el conjunto A? "))
    for i in range(cantidad_a):
        elemento = input(f"Ingrese el elemento #{i+1} para A: ")
        a.add(elemento)

    # Conjunto B
    b = set()
    cantidad_b = int(input("Cuantos elementos tendra el conjunto B? "))
    for i in range(cantidad_b):
        elemento = input(f"Ingrese el elemento #{i+1} para B: ")
        b.add(elemento)

    diagrama = venn2(subsets=(a,b), set_labels=['A', 'B'], set_colors=['purple', 'green'])
    diagrama.get_label_by_id('10').set_text('\n'.join(a - b))
    diagrama.get_label_by_id('01').set_text('\n'.join(b - a))
    diagrama.get_label_by_id('11').set_text('\n'.join(a & b))
    plt.text(-0.70, 0.589, 'Universo', fontsize=10, color='black')
    plt.text(-0.65, -0.35, 'Uva', fontsize=8, color='black')
    plt.text(-0.65, -0.398, 'Uva', fontsize=8, color='black')
    plt.gca().set_axis_on()
    plt.show()

elif cantidad == 3:
    a = set()
    cantidad_a = int(input("¿Cuántos elementos tendrá el conjunto A? "))
    for i in range(cantidad_a):
        elemento = input(f"Ingrese el elemento #{i+1} para A: ")
        a.add(elemento)

    # Conjunto B
    b = set()
    cantidad_b = int(input("¿Cuántos elementos tendrá el conjunto B? "))
    for i in range(cantidad_b):
        elemento = input(f"Ingrese el elemento #{i+1} para B: ")
        b.add(elemento)

    # Conjunto C
    c = set()
    cantidad_c = int(input("¿Cuántos elementos tendrá el conjunto C? "))
    for i in range(cantidad_c):
        elemento = input(f"Ingrese el elemento #{i+1} para C: ")
        c.add(elemento)

    diagrama = venn3(subsets=(a,b,c), set_labels=['A', 'B','C'], set_colors=['purple', 'green', 'blue'])
    diagrama.get_label_by_id('100').set_text('\n'.join(a - b - c))
    diagrama.get_label_by_id('010').set_text('\n'.join(b - a - c))
    diagrama.get_label_by_id('001').set_text('\n'.join(c - a - b))
    diagrama.get_label_by_id('110').set_text('\n'.join(a & b - c))
    diagrama.get_label_by_id('101').set_text('\n'.join(c & a - b))
    diagrama.get_label_by_id('011').set_text('\n'.join(c & b - a))
    diagrama.get_label_by_id('111').set_text('\n'.join(c & a & b))
    plt.text(-0.70, 0.688, 'Universo', fontsize=10, color='black')
    plt.text(-0.57, -0.35, 'Uva', fontsize=8, color='black')
    plt.text(-0.57, -0.398, 'Uva', fontsize=8, color='black')
    plt.gca().set_axis_on()
    plt.show()