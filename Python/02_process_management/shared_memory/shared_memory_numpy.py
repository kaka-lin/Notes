from multiprocessing import Process
from multiprocessing import shared_memory

import numpy as np


def worker(shm_name: str, shape: tuple, dtype: str):
    # 附加到已存在的共享記憶體
    existing_shm = shared_memory.SharedMemory(name=shm_name)

    # 將共享記憶體映射為 NumPy 陣列
    arr = np.ndarray(shape, dtype=dtype, buffer=existing_shm.buf)
    print("Child process read:", arr[:])

    # 對資料做修改
    arr *= 10
    print("Child process modified:", arr[:])

    # 僅關閉本地映射，不 unlink
    existing_shm.close()


if __name__ == "__main__":
    # 建立原始 NumPy 陣列
    ori_arr = np.array([1, 2, 3, 4], dtype=np.int64)

    # 建立共享記憶體區塊，大小至少為 numpy array 的位元組長度
    shm = shared_memory.SharedMemory(create=True, size=ori_arr.nbytes)

    # Now create a NumPy array backed by shared memory
    shm_arr = np.ndarray(ori_arr.shape, dtype=ori_arr.dtype, buffer=shm.buf)
    # Copy the original data into shared memory
    shm_arr[:] = ori_arr[:]
    print("type(ori_arr), type(shm_arr):", type(ori_arr), type(shm_arr))
    print("Parent process initial:", shm_arr[:])

    # 啟動子進程，並將 shm.name、shape、dtype 傳入
    p = Process(target=worker, args=(shm.name, ori_arr.shape, ori_arr.dtype.str))
    p.start()
    p.join()

    # 子進程修改後，父進程也能看到
    print("Parent process after child:", shm_arr[:])

    # 清理，共享記憶體不再需要時要 close 並 unlink
    shm.close()
    shm.unlink()
