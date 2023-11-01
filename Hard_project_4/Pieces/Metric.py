class Metric:
    def distance(a = "1a", b = "1a"):
        return ord(a[0]) - ord(b[0]), ord(a[1]) - ord(b[1])
    
    def move(a = "1a", xy = [0, 0]):
        return chr(ord(a[0]) + xy[0]) + chr(ord(a[1]) + xy[1])
    
    def isOut(a = "1a"):
        if a[0] < '1':
            return True
        if a[0] > '8':
            return True
        if a[1] < 'a':
            return True
        if a[1] > 'h':
            return True
        return False
    
    def iterate(pos, move):
        if pos == move:
            raise RuntimeError("Invalid destiation for iteration")
        
        dis = Metric.distance(move, pos)

        if dis[0] != 0 and dis[1] != 0 and abs(dis[0]) != abs(dis[1]):
            raise RuntimeError("Invalid destiation for iteration")

        k = [0, 0]

        for i in range(2):
            if dis[i] != 0:
                k[i] = int(dis[i]/abs(dis[i]))

        inc = k

        while not Metric.isOut(pos) and Metric.move(pos) != move:
            yield Metric.move(pos, k)
            k[0] += inc[0]
            k[1] += inc[1]