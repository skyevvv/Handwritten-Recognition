from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QComboBox, QDesktopWidget)
from PyQt5.QtGui import (QPainter, QPen, QFont)
from PyQt5.QtCore import Qt



class LearningUI(QWidget):
    def __init__(self):
        super(LearningUI, self).__init__()

        self.__init_ui()

        
        self.setMouseTracking(False)
        
        self.pos_xy = []
       
        self.pos_x = []
        self.pos_y = []

        
        self.btn_learn.clicked.connect(self.btn_learn_on_clicked)
        self.btn_recognize.clicked.connect(self.btn_recognize_on_clicked)
        self.btn_clear.clicked.connect(self.btn_clear_on_clicked)


        self.btn_add.clicked.connect(self.btn_add_on_clicked)
        self.btn_minus.clicked.connect(self.btn_minus_on_clicked)
        self.btn_mulitiplication.clicked.connect(self.btn_mulitiplication_on_clicked)
        self.btn_division.clicked.connect(self.btn_division_on_clicked)

    def __init_ui(self):
        

    
        self.btn_learn = QPushButton("学习", self)
        self.btn_learn.setGeometry(50, 400, 70, 40)
        self.btn_recognize = QPushButton("识别", self)
        self.btn_recognize.setGeometry(320, 400, 70, 40)
        self.btn_clear = QPushButton("清屏", self)
        self.btn_clear.setGeometry(420, 400, 70, 40)


        self.btn_add= QPushButton("+", self)
        self.btn_add.setGeometry(0, 100, 70, 40)

        self.btn_minus = QPushButton("-", self)
        self.btn_minus.setGeometry(0, 180, 70, 40)

        self.btn_mulitiplication = QPushButton("x", self)
        self.btn_mulitiplication.setGeometry(0, 260, 70, 40)

        self.btn_division = QPushButton("÷", self)
        self.btn_division.setGeometry(0, 340, 70, 40)



        self.combo_table = QComboBox(self)
        for i in range(10):
            self.combo_table.addItem("%d" % i)
        self.combo_table.setGeometry(150, 400, 70, 40)

        
        self.label_end = QLabel('by 没有东西小组', self)
        self.label_end.move(375, 470)

        
        self.label_output = QLabel('', self)
        self.label_output.setGeometry(0, 50,550 , 50)
        self.label_output.setStyleSheet("QLabel{border:5px solid black;}")
        self.label_output.setFont(QFont("Roman times", 10, QFont.Bold))
        self.label_output.setAlignment(Qt.AlignCenter)


        
        self.setFixedSize(550, 500)
        self.center()
        self.setWindowTitle('0-9手写体识别(机器学习中的"HelloWorld!")')


    def center(self):
        

        qt_center = self.frameGeometry()
        desktop_center = QDesktopWidget().availableGeometry().center()
        qt_center.moveCenter(desktop_center)
        self.move(qt_center.topLeft())

    def paintEvent(self, event):
        

        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

        if len(self.pos_xy) > 1:
            point_start = self.pos_xy[0]
            for pos_tmp in self.pos_xy:
                point_end = pos_tmp

                if point_end == (-1, -1):
                    point_start = point_end
                    continue

                if point_start == (-1, -1):
                    point_start = point_end
                    continue

                painter.drawLine(point_start[0], point_start[1], point_end[0], point_end[1])
                point_start = point_end
        painter.end()

    def mouseReleaseEvent(self, event):
        

        pos_test = (-1, -1)
        self.pos_xy.append(pos_test)

        self.update()

    def mouseMoveEvent(self, event):

        self.pos_x.append(event.pos().x())
        self.pos_y.append(event.pos().y())

       
        pos_tmp = (event.pos().x(), event.pos().y())
        
        self.pos_xy.append(pos_tmp)

        self.update()

    def btn_learn_on_clicked(self):
        

    pass

    def btn_recognize_on_clicked(self):
        

    pass

    def btn_clear_on_clicked(self):
        

        self.pos_xy = []
        self.pos_x = []
        self.pos_y = []
        #self.label_output.setText('')
        self.update()

    def btn_add_on_clicked(self):
        content=self.label_output.text()
        self.label_output.setText("%s+"%content)

    def btn_minus_on_clicked(self):
        content=self.label_output.text()
        self.label_output.setText("%s-"%content)

    def btn_mulitiplication_on_clicked(self):
        content=self.label_output.text()
        self.label_output.setText("%s×"%content)

    def btn_division_on_clicked(self):
        content=self.label_output.text()
        self.label_output.setText("%s÷"%content)




    def get_pos_xy(self):
        min_y、min2_y、max2_y、max_y
       

        if not self.pos_xy:
            return None

        pos_count = len(self.pos_x)
        max_x = max(self.pos_x)
        max_y = max(self.pos_y)
        min_x = min(self.pos_x)
        min_y = min(self.pos_y)
        dim = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        dis_x = (max_x - min_x) // 3
        dis_y = (max_y - min_y) // 3

        min2_x = min_x + dis_x
        min2_y = min_y + dis_y
        max2_x = max_x - dis_x
        max2_y = max_y - dis_y

        for i in range(len(self.pos_x)):
            if self.pos_y[i] >= min_y and self.pos_y[i] < min2_y:
                if self.pos_x[i] >= min_x and self.pos_x[i] < min2_x:
                    dim[0] += 1
                    continue
            if self.pos_x[i] >= min2_x and self.pos_x[i] < max2_x:
                dim[1] += 1
                continue
            if self.pos_x[i] >= max2_x and self.pos_x[i] <= max_x:
                dim[2] += 1
                continue
            elif self.pos_y[i] >= min2_y and self.pos_y[i] < max2_y:
                if self.pos_x[i] >= min_x and self.pos_x[i] < min2_x:
                    dim[3] += 1
                    continue
            if self.pos_x[i] >= min2_x and self.pos_x[i] < max2_x:
                dim[4] += 1
                continue
            if self.pos_x[i] >= max2_x and self.pos_x[i] <= max_x:
                dim[5] += 1
                continue
            elif self.pos_y[i] >= max2_y and self.pos_y[i] <= max_y:
                if self.pos_x[i] >= min_x and self.pos_x[i] < min2_x:
                    dim[6] += 1
                    continue
            if self.pos_x[i] >= min2_x and self.pos_x[i] < max2_x:
                dim[7] += 1
                continue
            if self.pos_x[i] >= max2_x and self.pos_x[i] <= max_x:
                dim[8] += 1
                continue
            else:
                pos_count -= 1
            continue
        
        for num in dim:
            num = num * 100 // pos_count

        return dim
