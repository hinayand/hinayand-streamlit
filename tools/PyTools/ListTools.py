class ListTools:
    def __init__(self, list):
        self.list = list

    def bubbleSort(self):
        # 冒泡排序列表
        for i in range(len(self.list)):
            for j in range(len(self.list) - 1):
                if self.list[j] > self.list[j + 1]:
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]
        return self.list

    def searchList(self, value):
        # 查找列表中元素的索引
        for k in range(len(self.list)):
            if self.list[k] == value:
                return k
        return None

    def itemIsExist(self, value):
        # 判断列表中是否存在某个元素
        for i in range(len(self.list)):
            if self.list[i] == value:
                return True
        return False

    def removeRepeat(self):
        # 删除列表中重复的元素
        newList = []
        for l in range(len(self.list)):
            if self.list[l] not in newList:
                newList.append(self.list[l])
        return newList

    def removeItem(self, value):
        # 删除列表中某个元素
        for m in range(len(self.list)):
            if self.list[m] == value:
                self.list.pop(m)
                return True
        return False

    def removeItems(self, values):
        # 删除列表中某些元素
        for n in range(len(values)):
            self.removeItem(values[n])
        return self.list
