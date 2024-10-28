from times import time_range
import pytest

def test_time_range_backwards():
    start_time = "2010-10-12 12:00:00"
    end_time = "2010-10-12 10:00:00"
    
    with pytest.raises(ValueError, match="End time must not be earlier than start time."):
        time_range(start_time, end_time)

