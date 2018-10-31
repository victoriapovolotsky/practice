class MaxArea:
    def max_area(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        length = len(height)
        for i in range(length):
            for j in range(length):
                if i != j:
                    area = MaxArea.find_area(i, j, height[i], height[j])
                    if area > max_area:
                        max_area = area

        return max_area


    def find_area(i, j, h1, h2):
        height = 0
        if h1 <= h2:
            height = h1
        else:
            height = h2

        width = abs(i-j)

        return height * width


# ma = MaxArea()
# print(ma.max_area([1,8,6,2,5,4,8,3,7]))