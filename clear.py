def btn_clear_on_clicked(self):
    '''
     按下清屏按钮：
     将列表赋值为空
     将输出识别结果的标签赋值为空
     然后刷新界面，重新绘画即可清屏
    '''

    self.pos_xy = []
    self.pos_x = []
    self.pos_y = []
    self.label_output.setText('')
    self.update()