import pyopencl.array as clArray

def fancyindex2D(func, queue, arr, mask, value=0):
    masked = clArray.empty_like(arr)
    func(
        queue, arr.shape, None,
        arr.data,
        mask.data,
        masked.data,
        arr.dtype.type(value)
    )
    return masked