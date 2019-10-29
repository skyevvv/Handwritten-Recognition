from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QPixmap, QPainter, QPoint, QPaintEvent, QMouseEvent, QPen,\
    QColor, QSize
from PyQt5.QtCore import Qt

class PaintBoard(QWidget):


    def __init__(self, Parent=None):

        super().__init__(Parent)

        self.__InitData() #先初始化数据，再初始化界面
        self.__InitView()
        
    def __InitView(self):
        self.setFixedSize(self.__size)
        
    def __InitData(self):
        
        self.__size = QSize(480,460)
        
        self.__board = QPixmap(self.__size) #新建QPixmap作为画板，宽350px,高250px
        self.__board.fill(Qt.white) #用白色填充画板
        
        self.__IsEmpty = True #默认为空画板 
        self.EraserMode = False #默认为禁用橡皮擦模式
        
        self.__lastPos = QPoint(0,0)
        self.__currentPos = QPoint(0,0)
        
        self.__painter = QPainter()
        
        self.__thickness = 10       #默认画笔粗细为10px
        self.__penColor = QColor("black")       #设置默认画笔颜色为黑色
        self.__colorList = QColor.colorNames() #获取颜色列表

    def paintEvent(self, paintEvent):

        self.__painter.begin(self)
        self.__painter.drawPixmap(0,0,self.__board)
        self.__painter.end()
       
    def mouseMoveEvent(self, mouseEvent):
        self.__currentPos =  mouseEvent.pos()
        self.__painter.begin(self.__board)
        
        if self.EraserMode == False:
            #非橡皮擦模式
            self.__painter.setPen(QPen(self.__penColor,self.__thickness)) #设置画笔颜色，粗细
        else:
            #橡皮擦模式下画笔为纯白色，粗细为10
            self.__painter.setPen(QPen(Qt.white,10))
            
        self.__painter.drawLine(self.__lastPos, self.__currentPos)
        self.__painter.end()
        self.__lastPos = self.__currentPos
                
        self.update() #更新显示
