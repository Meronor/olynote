import io
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

template_sign_in = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>679</width>
    <height>464</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout_5">
    <item>
     <spacer name="horizontalSpacer_2">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>172</width>
        <height>20</height>
       </size>
      </property>
     </spacer>
    </item>
    <item>
     <layout class="QVBoxLayout" name="verticalLayout">
      <item>
       <spacer name="verticalSpacer">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_3">
        <item>
         <widget class="QLabel" name="label">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="font">
           <font>
            <pointsize>18</pointsize>
            <weight>75</weight>
            <bold>true</bold>
           </font>
          </property>
          <property name="text">
           <string>Login</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QLabel" name="label_2">
        <property name="text">
         <string>Email</string>
        </property>
       </widget>
      </item>
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_4">
        <item>
         <widget class="QLabel" name="label_4">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="email">
          <property name="minimumSize">
           <size>
            <width>230</width>
            <height>0</height>
           </size>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="label_7">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QLabel" name="label_3">
        <property name="text">
         <string>Password</string>
        </property>
       </widget>
      </item>
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_2">
        <item>
         <widget class="QLabel" name="label_5">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="password">
          <property name="minimumSize">
           <size>
            <width>230</width>
            <height>0</height>
           </size>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="label_6">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <widget class="QPushButton" name="sign_in">
          <property name="text">
           <string>Sign in</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_9">
        <item>
         <spacer name="horizontalSpacer">
          <property name="orientation">
           <enum>Qt::Horizontal</enum>
          </property>
          <property name="sizeHint" stdset="0">
           <size>
            <width>40</width>
            <height>20</height>
           </size>
          </property>
         </spacer>
        </item>
        <item>
         <widget class="QPushButton" name="sign_up">
          <property name="text">
           <string>Sign up</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="label_8">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QLabel" name="explain">
        <property name="text">
         <string/>
        </property>
       </widget>
      </item>
      <item>
       <spacer name="verticalSpacer_2">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
     </layout>
    </item>
    <item>
     <spacer name="horizontalSpacer_3">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>171</width>
        <height>20</height>
       </size>
      </property>
     </spacer>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>679</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
template_sign_up = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>663</width>
    <height>488</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout_5">
    <item>
     <spacer name="horizontalSpacer_2">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>198</width>
        <height>20</height>
       </size>
      </property>
     </spacer>
    </item>
    <item>
     <layout class="QVBoxLayout" name="verticalLayout">
      <item>
       <spacer name="verticalSpacer_2">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
      <item>
       <widget class="QLabel" name="label">
        <property name="font">
         <font>
          <family>Ubuntu</family>
          <pointsize>20</pointsize>
          <weight>50</weight>
          <bold>false</bold>
         </font>
        </property>
        <property name="text">
         <string>Create an account</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignCenter</set>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="label_2">
        <property name="text">
         <string>Email</string>
        </property>
       </widget>
      </item>
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_4">
        <item>
         <widget class="QLabel" name="label_4">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="Email">
          <property name="minimumSize">
           <size>
            <width>230</width>
            <height>0</height>
           </size>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="label_10">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QLabel" name="label_3">
        <property name="text">
         <string>Password</string>
        </property>
       </widget>
      </item>
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_2">
        <item>
         <widget class="QLabel" name="label_5">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="Password">
          <property name="minimumSize">
           <size>
            <width>230</width>
            <height>0</height>
           </size>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="label_9">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QLabel" name="label_6">
        <property name="text">
         <string>Repeat password</string>
        </property>
       </widget>
      </item>
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_3">
        <item>
         <widget class="QLabel" name="label_7">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="Password2">
          <property name="minimumSize">
           <size>
            <width>230</width>
            <height>0</height>
           </size>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="label_8">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QPushButton" name="Create">
        <property name="text">
         <string>Create</string>
        </property>
       </widget>
      </item>
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <spacer name="horizontalSpacer">
          <property name="orientation">
           <enum>Qt::Horizontal</enum>
          </property>
          <property name="sizeHint" stdset="0">
           <size>
            <width>40</width>
            <height>20</height>
           </size>
          </property>
         </spacer>
        </item>
        <item>
         <widget class="QPushButton" name="Sign_in">
          <property name="text">
           <string>Sign in</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="label_11">
          <property name="enabled">
           <bool>false</bool>
          </property>
          <property name="minimumSize">
           <size>
            <width>20</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string/>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QLabel" name="error">
        <property name="text">
         <string/>
        </property>
        <property name="alignment">
         <set>Qt::AlignCenter</set>
        </property>
       </widget>
      </item>
      <item>
       <spacer name="verticalSpacer">
        <property name="orientation">
         <enum>Qt::Vertical</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>20</width>
          <height>40</height>
         </size>
        </property>
       </spacer>
      </item>
     </layout>
    </item>
    <item>
     <spacer name="horizontalSpacer_3">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>198</width>
        <height>20</height>
       </size>
      </property>
     </spacer>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>663</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Sing_IN_Wind(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_sign_in)
        uic.loadUi(f, self)
        self.showMaximized()
        self.sign_up.clicked.connect(self.GoToSign_Up)

    def GoToSign_Up(self):
        global ex
        ex2 = Sign_Up_Wind()
        ex2.show()
        self.close()
        ex = ex2


class Sign_Up_Wind(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_sign_up)
        uic.loadUi(f, self)
        self.showMaximized()
        self.Sign_in.clicked.connect(self.GoToSign_In)

    def GoToSign_In(self):
        global ex
        ex4 = Sing_IN_Wind()
        ex4.show()
        ex.close()
        ex = ex4


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sing_IN_Wind()
    ex.show()
    sys.exit(app.exec_())
