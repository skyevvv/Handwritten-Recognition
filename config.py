class Config():
    SOURCE_URL = "http://yann.lecun.com/exdb/mnist/"
    IMAGE_SIZE = 28
    NUM_CHANNELS = 1
    PIXEL_DEPTH = 255
    NUM_LABELS = 10
    VALIDATION_SIZE = 5000  # Size of the validation set.
    SEED = 66478  # Set to None for random seed.
    BATCH_SIZE = 64
    NUM_EPOCHS = 10
    EVAL_BATCH_SIZE = 64
    EVAL_FREQUENCY = 100  # Number of steps between evaluations.
    _FLAGS = None
    _WORK_DIRECTORY = None

    @property
    def FLAGS(self):
        return self._FLAGS
    @FLAGS.setter
    def FLAGS(self, val):
        self._FLAGS = val

    @property
    def WORK_DIRECTORY(self):
        return self._WORK_DIRECTORY
    @WORK_DIRECTORY.setter
    def WORK_DIRECTORY(self, val):
        self._WORK_DIRECTORY = val

config = Config()