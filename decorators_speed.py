import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f"Executing {fn.__name__}")
        print(f"Time: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def list_sum():
    return sum([x for x in range(1000000)])


@speed_test
def gen_sum():
    return sum(x for x in range(1000000))

print(list_sum())
print(gen_sum())