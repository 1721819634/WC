import wx
import os
from wc import WC


class WcFrame(wx.Frame):
    def __init__(self, parent):
        super(WcFrame, self).__init__(parent, title="Word Count", pos=(1000, 200), size=(500, 190))
        self.path_test = wx.TextCtrl(self, pos=(5, 5), size=(350, 24))
        self.open_button = wx.Button(self, label="打开", pos=(370, 5), size=(50, 24))
        self.open_button.Bind(wx.EVT_BUTTON, self.OnOpenFile)  # 绑定打开文件事件到open_button按钮上
        #  wx.TE_MULTILINE可以实现以滚动条方式多行显示文本,若不加此功能文本文档显示为一行
        self.content_text = wx.TextCtrl(self, pos=(5, 39), size=(475, 100), style=wx.TE_MULTILINE)
        self.cal_button = wx.Button(self, label="计算", pos=(430, 5), size=(50, 24))
        self.cal_button.Bind(wx.EVT_BUTTON, self.word_count)

    def OnOpenFile(self, event):  # 打开文件事件
        wildcard = 'All files(*.*)|*.*'
        dialog = wx.FileDialog(None, 'select', os.getcwd(), '', wildcard, wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dialog.ShowModal() == wx.ID_OK:
            self.path_test.SetValue(dialog.GetPath())
            dialog.Destroy

    def word_count(self, event):
        wc = WC(self.path_test.GetValue(), '-g')
        chars = wc.chars_count()
        words = wc.words_count()
        lines =wc.lines_count()
        result = '字符数：{}， 单词数：{}，代码行行数：{}，注释行行数：{}，空行行数：{}   总行数：{}'.format(chars, words, lines[0], lines[1], lines[2], lines[3])
        self.content_text.SetValue(result)


if __name__ == '__main__':
    app = wx.App()
    frame = WcFrame(None)
    frame.Show()
    app.MainLoop()