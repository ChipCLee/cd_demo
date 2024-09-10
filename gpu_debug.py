import tensorflow as tf

def get_gpus_count():
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        count=0
        try:
            # Currently, memory growth needs to be the same across GPUs
            for gpu in gpus:
                # tf.config.experimental.set_memory_growth(gpu, True)
                logical_gpus = tf.config.experimental.list_logical_devices('GPU')
                print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
                count+=len(logical_gpus)
        except RuntimeError as e:
            # Memory growth must be set before GPUs have been initialized
            print(e)
    print("TF will attempt to allocate only as much GPU memory as needed for the runtime allocations")
    return count

get_gpus_count()