import json
from pathlib import Path
from nonebot.log import logger



NULL_DATA = {"null":[]}

# 创建jobhandle类
class Jobhandle(object):
    def __init__(self) -> None:
        # 确认并创建json文件路径和json文件
        self.data_dir = Path("data/masiro").absolute()
        self.data_path = self.data_dir / "masiro.json"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.__data = NULL_DATA 
        self.__load()
    
    def __load(self):
        if self.data_path.exists() and self.data_path.is_file():
            with self.data_path.open("r", encoding="utf-8") as f:
                self.__data = json.load(f)
            logger.success("读取数据位于 " + str(self.data_path))
        else:
            self.__data = NULL_DATA
            self.__save()
            logger.success("创建json文件位于 " + str(self.data_path))

    def __save(self):
        with self.data_path.open("w", encoding="utf-8") as f:
            json.dump(self.__data, f, ensure_ascii=False, indent=4)
    

    
    # 查

    # 查询账密
    def match(self,username):
        if username in self.__data:
            return self.__data[username][0], self.__data[username][1]
        else:
            return None

    # 全部
    def matchlist(self):        
        if self.__data == NULL_DATA:
            return None
        else:
            return self.__data


    # 删
    # 单个
    def delete(self,username):
        try:
            del(self.__data[username])
            self.__save()
            return True
        except:
            return False
    
    # 清空
    def clearall(self):
        self.__data.clear()
        self.__save()

    # 增or改
    def plus(self,useraccount,userpassword,username,userjinyanzhi):
        self.__data[username] = [useraccount,userpassword,userjinyanzhi]
        self.__save()


jobhandle = Jobhandle()