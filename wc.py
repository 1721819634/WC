import re
import os
import wx

class WC:
    def __init__(self, file_dict, order):
        self.file_dict = file_dict
        self.order = order

    # 计算字符个数
    def chars_count(self, in_dict=None):
        f_dict = self.file_dict if in_dict is None else in_dict
        file = open(f_dict, mode='r', encoding='UTF-8')
        chars = len(file.read())
        file.close()
        return chars

    # 计算行数
    def lines_count(self, in_dict=None):
        f_dict = self.file_dict if in_dict is None else in_dict
        file = open(f_dict, mode='r', encoding='UTF-8')
        read = file.readlines()
        space_lines = 0  # 空行行数
        code_lines = 0  # 代码行行数
        comment_lines = 0  # 注释行行数
        comment_flag = False  # 注释行判断标志，用于判断多行注释
        start_comment_line = 0  # 多行注释的起始位置
        total_lines = 0  # 总行数
        for line in read:
            total_lines += 1
            line = line.strip()
            if not comment_flag:
                if line.startswith('"""') or line.startswith("'''"):
                    comment_flag = True
                    start_comment_line = total_lines
                elif line.startswith('#'):
                    comment_lines += 1
                elif len(line) <= 1:
                    space_lines += 1
                else:
                    code_lines += 1
            else:
                if line.endswith('"""') or line.endswith("'''"):
                    comment_flag = False
                    comment_lines += (total_lines - start_comment_line + 1)
        file.close()
        return [code_lines, comment_lines, space_lines, total_lines]

    # 计算词语数目
    def words_count(self, in_dict=None):
        f_dict = self.file_dict if in_dict is None else in_dict
        file = open(f_dict, mode='r', encoding='UTF-8')
        read = file.readlines()
        words = []  # 存储单词,得到单词并且存入列表中

        for line in read:
            # 用空格代替一串非数字和字母
            word = re.sub(r'[^0-9a-zA-Z\u4E00-\u9FFF]+', ' ', line)  # 用空格代替一串非数字和字母
            word = word.strip()
            word = word.split(' ')
            # 若该行为空或没有任何单词，word = ['']
            if word != ['']:
                words.extend(word)
        file.close()
        return len(words)

    def main_function(self, in_dict=None, in_oredr=None):
        from gui import WcFrame as WF
        f_dict = self.file_dict if in_dict is None else in_dict
        order = self.order if in_oredr is None else in_oredr
        is_file = False   # 若目录不为文件，只能与'-s'搭配
        if os.path.isfile(f_dict):
            is_file = True
        if order == '-c' and is_file:
            charco = self.chars_count(f_dict)
            print("字符数：", charco)
        elif order == '-w' and is_file:
            wordco = self.words_count(f_dict)
            print("单词数：", wordco)
        elif order == '-l' and is_file:
            lineco = self.lines_count(f_dict)
            print("总行数：", lineco[3])
        elif order == '-a' and is_file:
            lineco = self.lines_count(f_dict)
            print("代码行行数：", lineco[0])
            print("注释行数：", lineco[1])
            print("空行数：", lineco[2])
        elif order == '-s' and not is_file:
            self.recur_files()
        elif order == '-x':
            app = wx.App()
            frame = WF(None)
            frame.Show()
            app.MainLoop()
        elif order == '-g' and is_file:  # 输出全部信息
            lineco = self.lines_count(f_dict)
            print("字符数：", self.chars_count(f_dict))
            print("单词数：", self.words_count(f_dict))
            print("代码行行数：", lineco[0])
            print("注释行数：", lineco[1])
            print("空行数：", lineco[2])
            print("总行数：", lineco[3])
        else:
            print("输入命令有误，请重新输入！")

    def recur_files(self, in_dict=None):
        f_dict = self.file_dict if in_dict is None else in_dict
        path_list = os.listdir(f_dict)  # 获取当前目录下的文件名
        result = []
        result.extend(path_list)
        for path in path_list:
            new_dict = os.path.join(f_dict, path)  # 将获取的文件名拼接到原目录后面，组成新目录
            if os.path.isfile(new_dict):  # 判断是否为文件
                print('----------------')
                print('文件', path)
                self.main_function(new_dict, '-g')
            else:
                result.extend(self.recur_files(new_dict))
        return result  # 返回所有文件名，用于测试函数


if __name__ == '__main__':
    from gui import WcFrame as WF
    order, file_dict = input('请输入命令符和文件路径:').split()
    wc = WC(file_dict, order)
    wc.main_function()

