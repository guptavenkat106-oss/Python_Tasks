import time

# Decorator to track execution time
def track_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()   # Start time
        
        result = func(*args, **kwargs)  # Execute function
        
        end = time.perf_counter()     # End time
        
        print(f"Execution time of {func.__name__}: {end - start:.6f} seconds")
        
        return result
    return wrapper


# Example function
@track_time
def sample_task():
    total = 0
    for i in range(1000000):
        total += i
    return total


# Function call
sample_task()
