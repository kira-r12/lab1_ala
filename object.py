import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

lynx = np.array([
[209.70, 368.42], [157.63, 332.16], [118.82, 284.21], [80.95, 224.56], [43.08, 244.44], [20.36, 266.67], [-4.26, 293.57], [2.37, 263.16], [-20.36, 292.40], [-39.29, 299.42], [-21.30, 259.65],
[-50.65, 267.84], [-39.29, 242.11], [-55.38, 240.94], [-100.83, 300.58], [-149.11, 345.03], [-172.78, 361.40], [-189.82, 300.58], [-192.66, 225.73], [-181.30, 145.03], [-168.05, 104.09], [-184.14, 66.67],
[-186.98, 31.58], [-183.20, 3.51], [-208.76, -4.68], [-197.40, -29.24], [-182.25, -44.44], [-203.08, -43.27], [-172.78, -92.40], [-131.12, -126.32], [-101.78, -147.37], [-74.32, -163.74], [-110.30, -224.56],
[-143.43, -287.72], [-161.42, -240.94], [-282.60, -221.05], [-388.64, -205.85], [-370.65, -301.75], [-339.41, -397.66], [18.46, -397.66], [345.09, -400.00], [359.29, -378.95], [367.81, -342.69], [346.98, -362.57], [363.08, -302.92], [357.40, -243.27], [348.88, -266.67], [336.57, -201.17], [290.18, -135.67], [240.00, -118.13], [258.93, -164.91], [257.99, -228.07], [252.31, -271.35], [256.09, -333.33],
[247.57, -359.06], [230.53, -307.60], [194.56, -238.60], [160.47, -181.29], [120.71, -149.71], [165.21, -132.16], [201.18, -100.58], [183.20, -99.42], [221.07, -73.68], [253.25, -24.56], [222.01, -23.39],
[251.36, -1.17], [262.72, 24.56], [234.32, 25.73], [214.44, 42.11], [202.13, 60.82], [220.12, 101.75], [234.32, 160.23], [240.00, 230.41], [232.43, 316.96], [209.70, 368.42]
])
#
# x = lynx[:, 0]
# y = lynx[:, 1]
#
# plt.figure(figsize=(6,6))
# plt.plot(x, y, color='violet')
# plt.fill(x, y, color='violet', alpha=0.2)
# plt.axhline(0, color='black', lw=0.6)
# plt.axvline(0, color='black', lw=0.6)
# plt.axis('equal')
# plt.xlabel('X')
# plt.ylabel('Y')
#
# plt.grid(True)
#
# plt.show()

#functions

def stretch(X, a, b):
    X = X.copy()
    transformation = np.array([[a,0],[0,b]])
    print(f"Stretch:\n{transformation}")
    return (transformation @ X.T).T

def shear(X,a,b):
    X = X.copy()
    transformation = np.array([[1, a], [b, 1]])
    print(f"Shear:\n{transformation}")
    return (transformation @ X.T).T

def reflection(X,a,b):
    X = X.copy()
    multiplier = a**2 + b**2
    transformation = (1/multiplier) * np.array([[a**2-b**2, 2*a*b],
                                                [2*a*b, b**2-a**2]])
    print(f"Reflection:\n{transformation}")
    return (transformation @ X.T).T

def rotation(X, alpha):
    X = X.copy()
    transformation = np.array([[np.cos(alpha), np.sin(-alpha)],
                               [np.sin(alpha), np.cos(alpha)]])
    print(f"Rotation:\n{transformation}")
    return (transformation @ X.T).T

#
# def show(result, title, color, position):
#     plt.subplot(2, 2, position)
#     plt.plot(lynx[:, 0], lynx[:, 1], color='gray', lw=0.8, ls='--')
#     plt.plot(result[:, 0], result[:, 1], color=color)
#     plt.fill(result[:, 0], result[:, 1], color=color, alpha=0.3)
#     plt.axhline(0, color='black', lw=0.6)
#     plt.axvline(0, color='black', lw=0.6)
#     plt.axis('equal')
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title(title)
#     plt.grid(True)
#
#
# plt.figure(figsize=(12, 12))
# plt.suptitle('Stretch', fontsize=16)
# show(stretch(lynx, 1.5, 0.7), 'Stretch (1.5, 0.7)', 'blue', 1)
# show(stretch(lynx, 2, 2), 'Stretch (2, 2)', 'blue', 2)
# show(stretch(lynx, 0.5, 1), 'Stretch (0.5, 1)', 'blue', 3)
# show(stretch(lynx, -1, 1), 'Stretch (-1, 1)', 'blue', 4)
# plt.tight_layout()
# plt.show()
#
# plt.figure(figsize=(12, 12))
# plt.suptitle('Shear', fontsize=16)
# show(shear(lynx, 0.5, 0), 'Shear (0.5, 0)', 'green', 1)
# show(shear(lynx, 0, 0.5), 'Shear (0, 0.5)', 'green', 2)
# show(shear(lynx, 0.5, 0.5), 'Shear (0.5, 0.5)', 'green', 3)
# show(shear(lynx, 1, 1), 'Shear (1, 1)', 'green', 4)
# plt.tight_layout()
# plt.show()
#
# plt.figure(figsize=(12, 12))
# plt.suptitle('Reflection', fontsize=16)
# show(reflection(lynx, 1, 0), 'Reflection (1, 0)', 'red', 1)
# show(reflection(lynx, 0, 1), 'Reflection (0, 1)', 'red', 2)
# show(reflection(lynx, 1, 1), 'Reflection (1, 1)', 'red', 3)
# show(reflection(lynx, 1, 2), 'Reflection (1, 2)', 'red', 4)
# plt.tight_layout()
# plt.show()
#
# plt.figure(figsize=(12, 12))
# plt.suptitle('Rotation', fontsize=16)
# show(rotation(lynx, np.pi / 6), 'Rotation (30)', 'orange', 1)
# show(rotation(lynx, np.pi / 2), 'Rotation (90)', 'orange', 2)
# show(rotation(lynx, -np.pi / 4), 'Rotation (-45)', 'orange', 3)
# show(rotation(lynx, np.pi), 'Rotation (180)', 'orange', 4)
# plt.tight_layout()
# plt.show()


#2 task

def show_task2(result, title, color, position):
    plt.subplot(3, 3, position)
    plt.plot(lynx[:, 0], lynx[:, 1], color='gray', lw=0.8, ls='--')
    plt.plot(result[:, 0], result[:, 1], color=color)
    plt.fill(result[:, 0], result[:, 1], color=color, alpha=0.3)
    plt.axhline(0, color='black', lw=0.6)
    plt.axvline(0, color='black', lw=0.6)
    plt.axis('equal')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.grid(True)

plt.figure(figsize=(15, 15))
plt.suptitle('Task 2', fontsize=16)

#Stretch -> Shear -> Rotation
print("\nStretch -> Shear -> Rotation")
v1_s1 = stretch(lynx, 1.5, 0.5)
v1_s2 = shear(v1_s1, 0.5, 0)
result_v1 = rotation(v1_s2, np.pi/4)
show_task2(v1_s1, 'Order 1, step 1: Stretch', 'violet', 1)
show_task2(v1_s2, 'Order 1, step 2: + Shear', 'pink', 2)
show_task2(result_v1, 'Order 1 result: + Rotation', 'purple', 3)

#Rotation -> Shear -> Stretch
print("\nOrder 2: Rotation -> Shear -> Stretch")
v2_s1 = rotation(lynx, np.pi/4)
v2_s2 = shear(v2_s1, 0.5, 0)
result_v2 = stretch(v2_s2, 1.5, 0.5)
show_task2(v2_s1, 'Order 2, step 1: Rotation', 'violet', 4)
show_task2(v2_s2, 'Order 2, step 2: + Shear', 'pink', 5)
show_task2(result_v2, 'Order 2 result: + Stretch', 'purple', 6)

#Shear -> Rotation -> Stretch
print("\nShear -> Rotation -> Stretch")
v3_s1 = shear(lynx, 0.5, 0)
v3_s2 = rotation(v3_s1, np.pi/4)
result_v3 = stretch(v3_s2, 1.5, 0.5)
show_task2(v3_s1, 'Order 3, step 1: Shear', 'violet', 7)
show_task2(v3_s2, 'Order 3, step 2: + Rotation', 'pink', 8)
show_task2(result_v3, 'Order 3 result: + Stretch', 'purple', 9)

plt.tight_layout()
plt.show()
# матриця не є комутативною, тому фінальний результат залежить від порядку трансформації


#3 task
def rotate_xy (X, alpha):
    X = X.copy()
    transformation = np.array([
        [np.cos(alpha), np.sin(-alpha), 0],
        [np.sin(alpha), np.cos(alpha), 0], [0,0,1]])
    print(f"Rotation xy:\n{transformation}")
    return (transformation @ X.T).T

def rotate_yz (X, alpha):
    X = X.copy()
    transformation = np.array([[1,0,0],
                              [0, np.cos(alpha), np.sin(-alpha)],
                              [0, np.sin(alpha), np.cos(alpha)]])
    print(f"Rotation yz:\n{transformation}")
    return (transformation @ X.T).T

def rotate_xz (X, alpha):
    X = X.copy()
    transformation = np.array([[np.cos(alpha),0, np.sin(-alpha)],
                              [0, 1, 0],
                              [np.sin(alpha), 0, np.cos(alpha)]])
    print(f"Rotation xz:\n{transformation}")
    return (transformation @ X.T).T


def read_off(file):
    with open(file, 'r') as f:
        if 'OFF' != f.readline().strip():
            raise ValueError('Not a valid OFF header')

        n_verts, n_faces, _ = map(int, f.readline().strip().split())

        verts = [list(map(float, f.readline().strip().split())) for _ in range(n_verts)]
        faces = [list(map(int, f.readline().strip().split()[1:])) for _ in range(n_faces)]

        return np.array(verts), faces

def plot_off(vertices, faces, title = '3D Model'):
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, projection='3d')
        mesh = Poly3DCollection([vertices[face] for face in faces], alpha=0.3, edgecolor='k')
        ax.add_collection3d(mesh)
        ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=2, c='r')
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title(title)

        ax.auto_scale_xyz(vertices[:, 0], vertices[:, 1], vertices[:, 2])
        plt.show()
file_name = 'airplane_0005.off'
vertices, faces = read_off(file_name)
vertices = vertices - vertices.mean(axis=0)

plot_off(vertices, faces, title="Original 3D Model")

alpha_3d = np.pi / 4

vertices_xy = rotate_xy(vertices, alpha_3d)
plot_off(vertices_xy, faces, title="Rotated XY")

vertices_yz = rotate_yz(vertices, alpha_3d)
plot_off(vertices_yz, faces, title="Rotated YZ")

vertices_xz = rotate_xz(vertices, alpha_3d)
plot_off(vertices_xz, faces, title="Rotated XZ")