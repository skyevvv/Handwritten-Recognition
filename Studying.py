from PyQt5.QtWidgets import QMessageBox
from LearningUI import LearningUI
from LearningDB import LearningDB


class Learning(LearningUI):
    '''
    Learning实现btn_learn_on_clicked和btn_recognize_on_clicked两个方法
    '''

    def __init__(self):
        super(Learning, self).__init__()

    # 学习函数learn_data(table, dim)和一个识别函数identify_data(test_data)
    self.learn_db = LearningDB()

    def btn_learn_on_clicked(self):
        if not self.pos_xy:
            QMessageBox.critical(self, "注意", "请先写入您要学习的数字！")
            return None

    # 获取要学习的数字learn_num
    learn_num = self.combo_table.currentIndex()

    # 弹出确认对话框
    qbox = QMessageBox()
    qbox.setIcon(QMessageBox.Information)
    qbox.setWindowTitle("请确认")
    qbox.setText("学习数字 %d ？" % learn_num)
    qbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    qbox.setDefaultButton(QMessageBox.No)
    qbox.button(QMessageBox.Yes).setText("是")
    qbox.button(QMessageBox.No).setText("否")
    reply = qbox.exec()

    # 判断对话框结果，执行程序
    if reply == QMessageBox.Yes:
        learn_result = False
        learn_dim = self.get_pos_xy()
        if learn_dim:
            learn_result = self.learn_db.learn_data(learn_num, learn_dim)
        else:
            print('get_pos_xy()函数返回空值')
        return None

        if learn_result:
            QMessageBox.about(self, "提示", "学习成功！")
        else:
            QMessageBox.about(self, "提示", "学习失败！")
    else:
        return None

    def btn_recognize_on_clicked(self):

    # 如果没有进行绘画，警告后退出
    if not self.pos_xy:
        QMessageBox.critical(self, "注意", "请先写入您要识别的数字！")
        return None
    else:
        recognize_num = 0
        recognize_dim = self.get_pos_xy()
        if recognize_dim:
            recognize_num = self.learn_db.identify_data(recognize_dim)
        else:
            print('recognize_dim为空')
        return None
        self.label_output.setText('%d' % recognize_num)
