from Scripts.Sprite import Sprite

class MapGenerator():
    TileSetX = 64
    TileSetY = 64

    

    def __init__(self, scrn):
        self.scrn = scrn
        self.img0 = Sprite("Images\\MissingTexture.png", self.scrn)
        self.img1 = Sprite("Images\\Flor.png", self.scrn)
        self.img2 = Sprite("Images\\GrassTop.png", self.scrn)

    def load(self, filename):
        imgMap = Sprite(filename, self.scrn)
        self.mapSize = imgMap.imgae.get_size()

        self.mat = [[0] * self.mapSize[1] for _ in range(self.mapSize[0])]
        for i in range(0, self.mapSize[0]):
            for j in range(0, self.mapSize[1]):
                color = imgMap.imgae.get_at((i, j))

                if color == (0, 0, 0):
                    self.mat[i][j] = 0
                elif color == (255, 255, 255):
                    self.mat[i][j] = 1
                else:
                    self.mat[i][j] = -1

    def draw(self):
        for i in range(0, self.mapSize[0]):
            for j in range(0, self.mapSize[1]):
                if self.mat[i][j] == 0:
                    self.img1.draw(i*self.TileSetX, j*self.TileSetY)
                elif self.mat[i][j] == 1:
                    self.img2.draw(i*self.TileSetX, j*self.TileSetY)
                else:
                    self.img0.draw(i*self.TileSetX, j*self.TileSetY)