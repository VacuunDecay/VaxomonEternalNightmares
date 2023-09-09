from Scripts.Sprite import Sprite

class MapGenerator():
    TileSetX = 64
    TileSetY = 64

    mat = [[0] * 10 for _ in range(10)]

    def __init__(self, scrn):
        self.mat[2][2] = 1
        self.scrn = scrn
        self.img1 = Sprite("Images\\GrassTop.png", self.scrn)

    def draw(self):
        for i in range(0, 10):
            for j in range(0, 10):
                if self.mat[i][j] == 1:
                    self.img1.draw(i*self.TileSetX, j*self.TileSetY)
                if self.mat[i][j] == 0:
                    pass
                    #imagem0 em i*tylesetx j*tylesetY
