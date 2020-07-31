import timeit


class DatetimeDecorator:

    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        start_time = timeit.default_timer()
        self.func(*args, **kwargs)
        end_time = timeit.default_timer()
        print("WorkingTime[{}]: {} sec".format(self.func.__name__, end_time - start_time))

#
# def logging_time(original_fn):
#     def wrapper_fn(*args, **kwargs):
#         start_time = timeit.default_timer()
#         result = original_fn(*args, **kwargs)
#         end_time = timeit.default_timer()
#         print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time - start_time))
#         return result
#
#     return wrapper_fn


if __name__ == "__main__":
    pass