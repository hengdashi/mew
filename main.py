import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from utils import set_tensorflow_gpu_growth

if __name__ == '__main__':
    set_tensorflow_gpu_growth()
