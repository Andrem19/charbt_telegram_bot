import numpy as np
import shared_vars as sv
import random
import os

async def get_csv_data(path):
    data = np.genfromtxt(path, delimiter=',')
    return data

async def chose_data():
    files = [f for f in os.listdir(sv.path) if os.path.isfile(os.path.join(sv.path, f))]
    
    random_file = random.choice(files)
    file_path = os.path.join(sv.path, random_file)
    
    data = await get_csv_data(file_path)
    
    start_index = random.randint(0, len(data) - 70)
    segment = data[start_index:start_index + 70]

    part1 = segment[:65, :6]
    part2 = segment[65:, :6]

    return part1, part2