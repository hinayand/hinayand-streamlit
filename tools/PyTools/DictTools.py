class DictTools:
    def __init__(self, dict):
        self.dict = dict

    def getValue(self, key):
        # 获取字典中某个键的值
        return self.dict[key]

    def getKey(self, value):
        # 获取字典中某个值的键
        for key in self.dict:
            if self.dict[key] == value:
                return key
        return None

    def getKeys(self):
        # 获取字典中所有的键
        return self.dict.keys()

    def getValues(self):
        # 获取字典中所有的值
        return self.dict.values()

    def getItems(self):
        # 获取字典中所有的键值对
        return self.dict.items()

    def getLength(self):
        # 获取字典中所有的键值对的长度
        return len(self.dict)

    def keyIsExist(self, key):
        # 判断字典中是否存在某个键
        return key in self.dict

    def valueIsExist(self, value):
        # 判断字典中是否存在某个值
        for key in self.dict:
            if self.dict[key] == value:
                return True
        return False

    def sortDict(self):
        # 对字典排序
        return sorted(self.dict.items(), key=lambda x: x[0])
