import pytest
import tensorflow as tf
import gpu_debug

def test_get_gpus_count():
    assert gpu_debug.get_gpus_count() == 4
    

if __name__ == "__main__":
    pytest.main([__file__])