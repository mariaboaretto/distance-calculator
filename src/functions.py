import math

import matplotlib.pyplot as plt


def calc_distance(x1, y1, x2, y2):
    square_x = (x2 - x1) ** 2
    square_y = (y2 - y1) ** 2

    distance = math.sqrt(square_x + square_y)

    return distance


def graph(x_init, y_init, x_coord_dst, y_coord_dst, index):
    dst_point_x = x_coord_dst.pop(index)
    dst_point_y = y_coord_dst.pop(index)

    x_points = [x_init, dst_point_x]
    y_points = [y_init, dst_point_y]

    plt.figure(figsize=(16, 9))
    plt.scatter(x_points, y_points, color='r')
    plt.scatter(x_coord_dst, y_coord_dst, color='b')
    plt.plot(x_points, y_points, color='r')

    plt.show()


def get_init_points():
    while True:
        try:
            x_init, y_init = [float(x) for x in input("Insira as coordenadas do ponto inicial (x, y): ").split(",")]
            return x_init, y_init
        except ValueError:
            print("Número inválido. Tente novamente.")


def get_dst_points():
    x_coord_dst = []
    y_coord_dst = []

    user_message = "S"

    while user_message.lower() == "s":
        try:
            x_dst, y_dst = [float(x) for x in input("Insira as coordenadas do ponto de destino (x, y): ").split(",")]
            x_coord_dst.append(x_dst)
            y_coord_dst.append(y_dst)
            user_message = input("Você quer inserir outro ponto de destino? [s/n]: ")
        except ValueError:
            print("Número inválido. Tente novamente.")

    return x_coord_dst, y_coord_dst


def get_min_distance(x_initial, y_initial, x_coord_dst, y_coord_dst):
    min_distance = None
    index = None

    for i in range(len(x_coord_dst)):
        dst = calc_distance(x_initial, y_initial, x_coord_dst[i], y_coord_dst[i])

        if i == 0 or dst < min_distance:
            min_distance = dst
            index = i

    formatted_min = "{:.2f}".format(min_distance)

    return formatted_min, index


def init_graph():
    x_initial, y_initial = get_init_points()
    x_coord_dst, y_coord_dst = get_dst_points()
    min_distance, index = get_min_distance(x_initial, y_initial, x_coord_dst, y_coord_dst)
    print("A menor distância é: {}.".format(min_distance))
    graph(x_initial, y_initial, x_coord_dst, y_coord_dst, index)
