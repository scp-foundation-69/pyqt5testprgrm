## PyQt5 Test program
## Made in 2025 by SCP
## On Discord: @secure.contain.protect.

import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QCheckBox,
    QRadioButton, QComboBox, QSpinBox, QDoubleSpinBox, QSlider, QProgressBar,
    QListWidget, QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QMessageBox, QFileDialog, QColorDialog, QFontDialog, QInputDialog,
    QVBoxLayout, QHBoxLayout, QFormLayout, QTabWidget, QGroupBox,
    QLCDNumber, QDial, QScrollBar, QCalendarWidget, QSplitter, QStackedWidget,
    QDateEdit, QTimeEdit, QToolButton, QMenuBar, QMenu, QToolBar, QStatusBar,
    QGraphicsView, QGraphicsScene, QAction
)
from PyQt5.QtGui import QIcon, QColor, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect

class WidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI';
                font-size: 10pt;
            }
            QTabWidget::pane {
                border: 1px solid #C0C0C0;
                margin-top: 10px;
            }
            QGroupBox {
                border: 2px solid gray;
                border-radius: 5px;
                margin-top: 1ex;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
            }
            QPushButton {
                background-color: #F0F0F0;
                border: 1px solid #C0C0C0;
                border-radius: 3px;
                padding: 5px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
            QStatusBar {
                background-color: #F8F8F8;
                border-top: 1px solid #E0E0E0;
            }
        """)

        main_layout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)

        basic_tab = QWidget()
        basic_layout = QVBoxLayout()
        
        input_group = QGroupBox("Input Widgets")
        input_layout = QFormLayout()
        self.line_edit = QLineEdit("Example Text")
        self.text_edit = QTextEdit("Multi-line text")
        self.spin_box = QSpinBox()
        self.double_spin = QDoubleSpinBox()
        self.date_edit = QDateEdit()
        self.time_edit = QTimeEdit()
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Option 1", "Option 2", "Option 3"])
        
        input_layout.addRow(QLabel("QLineEdit:"), self.line_edit)
        input_layout.addRow(QLabel("QTextEdit:"), self.text_edit)
        input_layout.addRow(QLabel("QSpinBox:"), self.spin_box)
        input_layout.addRow(QLabel("QDoubleSpinBox:"), self.double_spin)
        input_layout.addRow(QLabel("QDateEdit:"), self.date_edit)
        input_layout.addRow(QLabel("QTimeEdit:"), self.time_edit)
        input_layout.addRow(QLabel("QComboBox:"), self.combo_box)
        input_group.setLayout(input_layout)
        basic_layout.addWidget(input_group)

        button_group = QGroupBox("Buttons")
        button_layout = QVBoxLayout()
        self.test_btn = QPushButton("Test Button")
        self.checkbox = QCheckBox("Check Box")
        self.radio_btn = QRadioButton("Radio Button")
        self.tool_button = QToolButton()
        self.tool_button.setText("Tool Button")
        
        self.test_btn.clicked.connect(self.pushButtonTest)
        button_layout.addWidget(self.test_btn)
        button_layout.addWidget(self.checkbox)
        button_layout.addWidget(self.radio_btn)
        button_layout.addWidget(self.tool_button)
        button_group.setLayout(button_layout)
        basic_layout.addWidget(button_group)

        basic_tab.setLayout(basic_layout)
        tabs.addTab(basic_tab, "Basic")

        dialog_tab = QWidget()
        dialog_layout = QVBoxLayout()
        
        msg_group = QGroupBox("Message Dialogs")
        msg_layout = QVBoxLayout()
        msg_btn_info = QPushButton("Show Information Message")
        msg_btn_warning = QPushButton("Show Warning Message")
        msg_btn_critical = QPushButton("Show Critical Message")
        
        msg_btn_info.clicked.connect(lambda: QMessageBox.information(self, "Info", "Information message"))
        msg_btn_warning.clicked.connect(lambda: QMessageBox.warning(self, "Warning", "Warning message"))
        msg_btn_critical.clicked.connect(lambda: QMessageBox.critical(self, "Critical", "Critical message"))
        
        msg_layout.addWidget(msg_btn_info)
        msg_layout.addWidget(msg_btn_warning)
        msg_layout.addWidget(msg_btn_critical)
        msg_group.setLayout(msg_layout)
        dialog_layout.addWidget(msg_group)

        file_group = QGroupBox("File Operations")
        file_layout = QVBoxLayout()
        self.file_label = QLabel("No file selected")
        file_btn = QPushButton("Open File")
        file_btn.clicked.connect(self.open_file)
        file_layout.addWidget(file_btn)
        file_layout.addWidget(self.file_label)
        file_group.setLayout(file_layout)
        dialog_layout.addWidget(file_group)

        style_group = QGroupBox("Styling")
        style_layout = QVBoxLayout()
        color_btn = QPushButton("Choose Color")
        font_btn = QPushButton("Choose Font")
        input_btn = QPushButton("Get Text Input")
        
        color_btn.clicked.connect(self.choose_color)
        font_btn.clicked.connect(self.choose_font)
        input_btn.clicked.connect(self.get_text_input)
        
        style_layout.addWidget(color_btn)
        style_layout.addWidget(font_btn)
        style_layout.addWidget(input_btn)
        style_group.setLayout(style_layout)
        dialog_layout.addWidget(style_group)

        dialog_tab.setLayout(dialog_layout)
        tabs.addTab(dialog_tab, "Dialogs")

        graphics_tab = QWidget()
        graphics_layout = QVBoxLayout()
        
        draw_group = QGroupBox("Graphics View")
        draw_layout = QVBoxLayout()
        self.graphics_view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)
        
        draw_controls = QHBoxLayout()
        btn_add_text = QPushButton("Add Text")
        btn_add_rect = QPushButton("Add Rectangle")
        btn_clear = QPushButton("Clear")
        
        btn_add_text.clicked.connect(self.add_graphic_text)
        btn_add_rect.clicked.connect(self.add_graphic_rect)
        btn_clear.clicked.connect(lambda: self.scene.clear())
        
        draw_controls.addWidget(btn_add_text)
        draw_controls.addWidget(btn_add_rect)
        draw_controls.addWidget(btn_clear)
        draw_layout.addWidget(self.graphics_view)
        draw_layout.addLayout(draw_controls)
        draw_group.setLayout(draw_layout)
        graphics_layout.addWidget(draw_group)

        graphics_tab.setLayout(graphics_layout)
        tabs.addTab(graphics_tab, "Graphics")

        system_tab = QWidget()
        system_layout = QVBoxLayout()
        
        info_group = QGroupBox("System Info")
        info_layout = QFormLayout()
        self.lcd = QLCDNumber()
        self.slider = QSlider(Qt.Horizontal)
        self.progress_bar = QProgressBar()
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.lcd.display)
        self.slider.valueChanged.connect(self.progress_bar.setValue)
        
        info_layout.addRow(QLabel("LCD Display:"), self.lcd)
        info_layout.addRow(QLabel("Control Slider:"), self.slider)
        info_layout.addRow(QLabel("Progress Bar:"), self.progress_bar)
        info_group.setLayout(info_layout)
        system_layout.addWidget(info_group)

        dial_group = QGroupBox("Dial & Scrollbar")
        dial_layout = QVBoxLayout()
        self.dial = QDial()
        self.scrollbar = QScrollBar(Qt.Horizontal)
        dial_layout.addWidget(self.dial)
        dial_layout.addWidget(self.scrollbar)
        dial_group.setLayout(dial_layout)
        system_layout.addWidget(dial_group)

        system_tab.setLayout(system_layout)
        tabs.addTab(system_tab, "System")

        containers_tab = QWidget()
        containers_layout = QVBoxLayout()
        
        list_group = QGroupBox("List Widget")
        list_layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Item 1", "Item 2", "Item 3"])
        self.list_widget.itemDoubleClicked.connect(self.triggerLabelChange)
        self.listItemDoubleClickedLabel = QLabel("Double-click a list item")
        list_layout.addWidget(self.list_widget)
        list_layout.addWidget(self.listItemDoubleClickedLabel)
        list_group.setLayout(list_layout)
        containers_layout.addWidget(list_group)

        table_group = QGroupBox("Table Widget")
        table_layout = QVBoxLayout()
        self.table_widget = QTableWidget(3, 3)
        for i in range(3):
            for j in range(3):
                self.table_widget.setItem(i, j, QTableWidgetItem(f"Cell {i},{j}"))
        table_layout.addWidget(self.table_widget)
        table_group.setLayout(table_layout)
        containers_layout.addWidget(table_group)

        tree_group = QGroupBox("Tree Widget")
        tree_layout = QVBoxLayout()
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabel("Tree")
        root = QTreeWidgetItem(self.tree_widget, ["Root"])
        QTreeWidgetItem(root, ["Child"])
        tree_layout.addWidget(self.tree_widget)
        tree_group.setLayout(tree_layout)
        containers_layout.addWidget(tree_group)

        containers_tab.setLayout(containers_layout)
        tabs.addTab(containers_tab, "Containers")

        advanced_tab = QWidget()
        advanced_layout = QVBoxLayout()
        
        calendar_group = QGroupBox("Calendar Widget")
        calendar_layout = QVBoxLayout()
        self.calendar = QCalendarWidget()
        calendar_layout.addWidget(self.calendar)
        calendar_group.setLayout(calendar_layout)
        advanced_layout.addWidget(calendar_group)

        splitter_group = QGroupBox("Splitter")
        splitter_layout = QVBoxLayout()
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(QLabel("Left Panel"))
        splitter.addWidget(QLabel("Right Panel"))
        splitter_layout.addWidget(splitter)
        splitter_group.setLayout(splitter_layout)
        advanced_layout.addWidget(splitter_group)

        stacked_group = QGroupBox("Stacked Widget")
        stacked_layout = QVBoxLayout()
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(QLabel("Page 1"))
        self.stacked_widget.addWidget(QLabel("Page 2"))
        stack_btn = QPushButton("Switch Page")
        stack_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1 - self.stacked_widget.currentIndex()))
        stacked_layout.addWidget(self.stacked_widget)
        stacked_layout.addWidget(stack_btn)
        stacked_group.setLayout(stacked_layout)
        advanced_layout.addWidget(stacked_group)

        advanced_tab.setLayout(advanced_layout)
        tabs.addTab(advanced_tab, "Advanced")

        credits_tab = QWidget()
        credits_layout = QVBoxLayout()
        credits_text = QLabel(
            "Credits:\n\nDeveloped by SCP\n"
            "Special thanks to PyQt5 contributors\n"
            "PyQt5 Widget Demonstration Program\n"
            "Free to use code\n\n"
            "Notice:\n\nThis program demonstrates various PyQt5 widgets\n"
            "and their basic functionality."
        )
        credits_text.setAlignment(Qt.AlignCenter)
        credits_layout.addWidget(credits_text)
        credits_tab.setLayout(credits_layout)
        tabs.addTab(credits_tab, "Credits")

        main_layout.addWidget(tabs)
        
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("Ready (QStatusBar)")
        main_layout.addWidget(self.status_bar)

        menubar = QMenuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction("Exit", self.close)
        file_menu.addAction("Metadata Test", self.testProgramMetaData)
        main_layout.setMenuBar(menubar)

        toolbar = QToolBar()
        toolbar_action = QAction(QIcon(), "Toolbar Action", self)
        toolbar_action.triggered.connect(self.toolbar_action)
        toolbar.addAction(toolbar_action)
        main_layout.addWidget(toolbar)

        self.setLayout(main_layout)
        self.setWindowTitle("PyQt5 Widget Demonstration")
        self.setGeometry(100, 100, 1024, 768)
        
        self.animated_label = QLabel("SCP Foundation - PyQt5 Widget showoff", self)
        self.animated_label.setFont(QFont("Arial", 10, QFont.Bold))
        self.animation = QPropertyAnimation(self.animated_label, b"geometry")
        self.animation.setDuration(10000)
        self.animation.setStartValue(QRect(50, 5, 300, 20))
        self.animation.setEndValue(QRect(674, 5, 300, 20))
        self.animation.setLoopCount(-1)
        self.animation.start()

    def pushButtonTest(self):
        QMessageBox.information(self, "Button Test", "QPushButton clicked successfully!")

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_name:
            self.file_label.setText(f"Selected: {file_name}")
            self.status_bar.showMessage(f"Opened file: {file_name}")

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            QMessageBox.information(self, "Color Selected", f"Selected color: {color.name()}")

    def choose_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            QMessageBox.information(self, "Font Selected", f"Selected font: {font.family()}")

    def get_text_input(self):
        text, ok = QInputDialog.getText(self, "Text Input", "Enter your name:")
        if ok:
            QMessageBox.warning(self, "Name Check", "Consider changing your name!")

    def toolbar_action(self):
        QMessageBox.information(self, "Toolbar", "Toolbar action activated!")

    def testProgramMetaData(self):
        num = random.choice([1, 2, 3])
        if num == 1:
            QMessageBox.information(self, "Metadata", "System Status: OK")
        else:
            QMessageBox.warning(self, "Metadata", "System Status: Warning")

    def add_graphic_text(self):
        self.scene.addText("PyQt5 Text Element", QFont("Arial", 12))

    def add_graphic_rect(self):
        color = QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.scene.addRect(
            random.randint(0, 200),
            random.randint(0, 100),
            50, 50,
            color,
            color
        )
    
    def triggerLabelChange(self, item):
        self.listItemDoubleClickedLabel.setText(f"Double-clicked: {item.text()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = WidgetDemo()
    demo.show()
    sys.exit(app.exec_())

## Last updated 8th of February, 2025
## Free to use program
