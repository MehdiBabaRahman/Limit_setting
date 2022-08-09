{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "N=3\n",
    "r=0.4\n",
    "L=59.97"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "msD=np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])\n",
    "alpha=np.array([0.206, 0.207, 0.204, 0.192, 0.189, 0.191, 0.191, 0.218, 0.248, 0.266, 0.27, 0.294])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "sigBr=N/(L*r*alpha)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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a/tu3bqRmprKzJkzue6667j77rtJSGj6yqVSJyIiIrvMnDmTQYMGYWa0aNGCiRMn7jr6NWvWLIYMGbJr26qqKs4880zOOeccjjrqqAPa/xtvvLHrTtQ9X3s+jgSq73AtKyujsrKSyspKysrK2LFjx671v/71r5k7dy6vvPLKrhsVdtqwYQNvvfXWru958sknef/99zn22GPrzHbkkUeSlZXFxRdfzLp163B3vv32W/75z3/uuuN32LBhTJw4kRkzZgCwadMmXnrppd2Koplx8MEH86tf/YpRo0bt9Rq+UFOpExERkV32LG7jxo2jTZs2wP/dQLHT5ZdfTs+ePfnFL36xa9nSpUv54Q9/yD333MOll17K9u3bG5Xn5ptvJj09nT/+8Y888cQTpKenc/PNNwOwaNEiHnzwQWbNmkWHDh12HfF78skngerr7K6++mratm1LmzZt+Nvf/saLL75I79696/ysjIwM3nnnHZYsWULfvn1p27YtJ510Ej169OC+++4DIC8vj2uvvZYf/vCHZGZmcvDBB/Pmm29iZrvta8CAAXz++efccccdjfr568P2dggyXowYMcJr36EiuysuLg7bvzAk+sa7sqqSycsnk5aYxtB2Q0lMSAw6Ur1E23hHO433/5k7d+6u69KaSkOvqTtQDzzwAO+88w4TJkzYrdC88MILZGdnM378eP7+978zatQohg8f3mQ5GiMtLY3U1FQuvPBCbrrppkbv70DH/KijjmLKlCmMHDmSwsLCOrfZ298RM5vu7iPq+h7dKCEi9ba9cjuvLniVRz9/lIWbFgLQMrUlY7uMpSC3gNEdR5OWlBZsSBFpMitWrOCCCy5g2LBhHHHEEUD1Q4L/85//MG3aNK64ovrmj2+++YYzzzwzyKj7VFZWFsjnvvPOO02yX5U6ETlgWyq2MGHeBB6f8zirtq2iX6t+3DH2DhItkcKSQgoXFfLiNy+SnpTOoTmHMj53PId3Ppzs1Oygo4tICHXo0IGKioo613311Vc89thjlJaWcvTRR9O8efMwp4tfKnUisl/rytbx5NwneerLp9i8fTOjOo7i5sNuZnTH0btOuxzV9SgqqiqYumIqRSVFTCyZyLsl75JkSYzoMILxueM5ossRdGjWIeCfRkSa0oQJE4KOELdU6kRkr5aWLuWxOY/xwtcvUF5ZTkFuAecOPJcBbQbU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\n",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(figsize=(10,10))\n",
    "ax.plot(msD, sigBr, label = r'$M_{Z_{D}} = 125 [GeV]$', c='tab:green')\n",
    "plt.grid()\n",
    "plt.rcParams.update({'font.size': 12})\n",
    "ax.set_xlabel(r'$\\alpha$')\n",
    "# ax.set_xlabel('Ms_{D}')\n",
    "# ax.set_xlabel('x-axis')\n",
    "ax.set_xlabel(r'$M_{s_{D}}$ [GeV]')\n",
    "# ax.set_ylabel(r'$\\sigma(pp \\rightarrow Z_{D}) \\times Br(Z_{D} \\rightarrow s_{D} \\overline{s_{D})$  [fb]')\n",
    "ax.set_ylabel(r'$\\sigma(pp \\rightarrow Z_{D}) \\times BR(Z_{D} \\rightarrow s_{D} \\bar{s_{D})}$ [fb]')\n",
    "plt.legend()\n",
    "plt.show()\n",
    "fig.savefig('MZD_125.png')\n",
    "# plt.savefig('foo.pdf')\n",
    "# plt.clf()\n",
    "# plt.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
