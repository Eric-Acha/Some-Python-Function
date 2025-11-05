# visualize the progress of a loop with a progress bar using the tqdm module

import time
from tqdm import tqdm

for _ in tqdm(range(100)):
    time.sleep(0.30)
