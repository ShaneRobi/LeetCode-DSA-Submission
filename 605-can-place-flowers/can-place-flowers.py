class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers_planted = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] != 0:
                continue

            if i == 0:
                right_empty = (
                    len(flowerbed) == 1 or flowerbed[i + 1] == 0
                )

                if right_empty:
                    flowerbed[i] = 1
                    flowers_planted += 1

            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    flowers_planted += 1

            else:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    flowers_planted += 1

            if flowers_planted == n:
                return True

        return flowers_planted >= n