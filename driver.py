import sys
import os
import time
import functools
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import dl as DL
import labeling as LABEL

if __name__ == "__main__":
    DL.load_files()
    LABEL.main()
    