

class Size:

    winSize = 500

    def setsize(self, num):
        if num < 200:
            Size.winSize = 200

        elif num > 800:
            Size.winSize = 800

        else:
            Size.winSize = num

    def getsize(self):
        return Size.winSize


if __name__ == "__main__":
    pass
