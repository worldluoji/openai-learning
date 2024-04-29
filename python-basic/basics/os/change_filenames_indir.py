
import os
import random
import time

'''
重命名为随机值 + 时间戳
'''
def new_name():
    randomList = random.sample('zyxwvutsrqponmlkjihgfedcba_', 6)
    s = ''.join(randomList)
    return s + str(time.time())


'''
file_path 保存图片的目录
ext 需要批量重命名的扩展名
'''
def rename(file_path, ext):
    # 取得指定文件夹下的文件列表
    old_names = os.listdir(file_path)
    for old_name in old_names:

        # 根据扩展名，判断文件是否需要改名
        if old_name.endswith(ext):

            # 完整的文件路径
            old_path = os.path.join(file_path, old_name)

            # 新的文件名
            new_path = os.path.join(file_path, new_name() + ext)
        
            # 重命名
            os.rename(old_path, new_path)

    # 显示改名后的结果
    print(os.listdir(file_path))

if __name__ == '__main__':
    rename('/Users/honorluo/Downloads/test', '.png')