import random
import matplotlib.pyplot as plt
import numpy as np

# for the same results
random.seed(10)


class HumanRandom:
    START = 10
    BASE = 4

    def random_number(self):
        return random.randint(-3, 4)

    # This is a function that will make some noise.
    def noise(self):
        self.START = int((self.START + self.random_number()) / 2) + self.BASE
        return self.START


t = np.asarray(range(0, 300))  # array(range(0, 100))

s1 = []
human = HumanRandom()
for i in range(0, 300):
    s1.append(human.noise())


s1na = np.asarray(s1)

fig, axs = plt.subplots(1, 1)
axs.plot(t, s1na)
axs.set_xlabel('time')
axs.set_ylabel('s1')
axs.grid(True)

fig.tight_layout()
plt.show()
