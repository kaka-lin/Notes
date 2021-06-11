import random

class ImgInfo(object):
    def __init__(self, idx, img):
        self.idx = idx
        self.img = img

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __lt__(self, other):
        return self.idx < other.idx

    def __getitem__(self, key):
        return self.__dict__.get(key)


if __name__ == "__main__":
    img_list = []
    img_list.append(ImgInfo('2', 'img2'))
    img_list.append(ImgInfo('5', 'img5'))
    img_list.append(ImgInfo('3', 'img3'))
    img_list.append(ImgInfo('1', 'img1'))
    img_list.append(ImgInfo('4', 'img4'))
    print("Before sort: ", img_list)
    img_list.sort()
    print("After sort: ", img_list)

    print(img_list[0]['idx'])
