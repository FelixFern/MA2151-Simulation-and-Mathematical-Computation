import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# Inisiasi Awal
width = 50
height = 50 
heat_diffusion_rate = 0.125

# Diubah untuk pertanyaan b
env_temp = 0

# Diubah untuk run yang berbeda-beda
seed = np.random.seed(1)

ext_heat_grid = np.zeros([height + 2, width + 2])
ext_main_grid = np.zeros([height + 2, width + 2])

# Fungsi Environment_temp : Untuk mengisi grid dengan env_temp yang telah di tentukan
def enviroment_temp(grid, temp):
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = temp
    return grid

# Memanggil fungsi environment_temp
ext_heat_grid = enviroment_temp(ext_heat_grid, env_temp)

# Fungsi Absorbing : Untuk membuat absorbing boundary condition pada grid
def absorbing(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
                grid[j][i] = -1
    return grid

# Fungsi Reflecting : Untuk membuat reflecting boundary condition pada grid
def reflecting(grid): 
    for i in range(1, width + 1): 
        grid[0][i] = grid[1][i]
        grid[height + 1][i] = grid[height][i]
    for i in range(0, height + 2): 
        grid[i][0] = grid[i][1]
        grid[i][width + 1] = grid[i][width]
    return grid

# Memanggil fungsi reflecting dan absorbing untuk masing-masing grid
ext_heat_grid = reflecting(ext_heat_grid)
ext_main_grid = absorbing(ext_main_grid)


# Rodents = 40
# Viper = 50
# Border = -1

# Temperature : 0 (low) - 37 (med)

# Random Rodent Position
rodent = [37, np.random.randint(1, height + 1), np.random.randint(1, width + 1), 1] #  rodent temp, x, y, alive / dead (1 / 0)

# Random Viper Position
viper = [np.random.randint(1, height + 1), np.random.randint(1, width + 1)] # x, y

# Fungsi rodent_movement : Untuk pergerakan dari rodent
def rodent_movement():
    steps = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [1,-1], [-1,-1], [-1, 1]]
    rand = np.random.randint(0, len(steps))
    if 1 <= rodent[1] + steps[rand][0] <= width and 1 <= rodent[2] + steps[rand][1] <= height and rodent[3] == 1:
        rodent[1] += steps[rand][0]
        rodent[2] += steps[rand][1]

# Fungsi viper_movement : Untuk pergerakan dari viper
def viper_movement(heat):
    steps = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [1,-1], [-1,-1], [-1, 1]]
    max_heat = 0
    max_heat_pos = [0,0]
    for step in steps:
        if viper[1] + step[1] == rodent[2] and viper[0] + step[0] == rodent[1]:
            viper[0] += step[0]
            viper[1] += step[1]
        if 1 <= viper[1] + step[1] <= width and 1 <= viper[0] + step[0] <= height:
            if heat[viper[1] + step[1]][viper[0] + step[0]] >= max_heat:
                max_heat = heat[viper[1] + step[1]][viper[0] + step[0]]
                max_heat_pos = [viper[0] + step[0], viper[1] + step[1]]    
    if max_heat != 0:
        viper[0] = max_heat_pos[0]
        viper[1] = max_heat_pos[1]
    else: 
        rand = np.random.randint(0, len(steps))
        if 1 <= viper[0] + steps[rand][0] <= width and 1 <= viper[1] + steps[rand][1] <= height:
            viper[0] += steps[rand][0]
            viper[1] += steps[rand][1]

t = 0 # Variable untuk menghitung waktu iterasi yang diperlukan sampai rodent tertangkap
dead = False # Variable berupa boolean untuk menunjukkan keadaan dari rodent

# Animasi
def generate_data():
    global t, dead
    # Posisi Rodent 
    rodent_x = rodent[1]
    rodent_y = rodent[2]
    # Posisi Viper Pos
    viper_x = viper[0]
    viper_y = viper[1]

    # Menyimpan grid untuk heat_grid 
    save_heat_grid = np.copy(reflecting(ext_heat_grid))

    # Looping Simulasi 
    for i in range(1, width + 1):
        for j in range(1, height + 1):
            # Array yang berisikan incrementasi x dan y, contoh : [1,0] incrementasi pada x sebesar 1 dan incrementasi pada y sebesar 0
            steps = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
            # Variable untuk jumlah suhu disekeliling titik yang diperiksa
            sums = 0
            # Looping sepanjang variable steps
            for step in steps:
                # Jika titik yang diperiksa merupakan rodent
                if i + step[0] == rodent_x and j + step[1] == rodent_y and rodent[3] == 1:
                    sums += (rodent[0] - save_heat_grid[j][i]) # Menambahkan dengan suhu tubuh dari rodent
                else: 
                    sums += (save_heat_grid[j + step[1]][i + step[0]] - save_heat_grid[j][i])
            ext_heat_grid[j][i] += heat_diffusion_rate*sums # Rumus Difusi
            ext_main_grid[j][i] = ext_heat_grid[j][i] 
    # Menambahkan Viper and Rodent kedalam grid
    if rodent[3] == 1:
        ext_main_grid[rodent_y][rodent_x] = 40
    ext_main_grid[viper_y][viper_x] = 50

    # Memanggil fungsi untuk pergerakan viper dan rodent
    viper_movement(save_heat_grid)
    rodent_movement()

    # Jika rodent dan viper berada dalam posisi yang sama
    if viper_x == rodent_x and viper_y == rodent_y: 
        rodent[3] = 0
        dead = True

    if rodent[3] == 0 and dead == True:
        dead = False
        print("Tertangkap pada iterasi ke :", t)
    else: 
        t += 1
    return ext_main_grid

# Fungsi untuk animasi simulasi
def update(data):
    mat.set_data(data)
    return mat 
    
def data_gen():
    while True:
        yield generate_data()
        if rodent[3] == 0:
            break

fig, ax = plt.subplots()
mat = ax.matshow(generate_data())
ani = animation.FuncAnimation(fig, update, data_gen, interval=100, save_count=400)

plt.show()