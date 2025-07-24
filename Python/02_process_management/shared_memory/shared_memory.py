from multiprocessing import Process
from multiprocessing import shared_memory


def worker(shm_name: str, size: int):
    # 附加到已存在的共享記憶體
    existing_shm = shared_memory.SharedMemory(name=shm_name)
    buf = existing_shm.buf

    # 以整數列表讀出前 size 個數字
    data = list(buf[:size])
    print(f"Child read: {data}")

    # 將每個數字乘以 10（注意結果若超過 255 會 mod 256）
    for i, val in enumerate(data):
        buf[i] = (val * 10) % 256
    print(f"Child modified: {list(buf[:size])}")

    # 僅關閉本地映射，不 unlink
    existing_shm.close()


if __name__ == "__main__":
    size = 10  # 我們要共享的元素個數

    # 建立一塊共享記憶體（大小 = size bytes）
    shm = shared_memory.SharedMemory(create=True, size=size)
    buf = shm.buf  # 一個 memoryview

    # 初始化共享記憶體為一個整數陣列: 0,1,2,...,9
    for i in range(size):
        buf[i] = i
    print(f"Parent initial: {list(buf[:size])}")

    # 啟動子進程，傳入 shm.name 與 size
    p = Process(target=worker, args=(shm.name, size))
    p.start()
    p.join()

    # 子進程修改後，父進程也能看到
    print(f"Parent after child: {list(buf[:size])}")

    # 清理：先 close，然後 unlink（移除 shared memory）
    shm.close()
    shm.unlink()
