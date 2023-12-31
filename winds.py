import io
import sqlite3
from PyQt6 import uic
import qdarktheme
from calendar import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QDialog, QLineEdit, QPushButton
from base import get_url, get_note, get_olys, get_theme, get_event, set_theme, set_note, set_date, add_user,\
    handle_link_activation

template_calendar = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>976</width>
    <height>868</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout_3">
    <item>
     <widget class="QCalendarWidget" name="calendar">
      <property name="minimumSize">
       <size>
        <width>700</width>
        <height>0</height>
       </size>
      </property>
     </widget>
    </item>
    <item>
     <layout class="QVBoxLayout" name="verticalLayout_2">
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
       <widget class="QLabel" name="label_2">
        <property name="minimumSize">
         <size>
          <width>250</width>
          <height>0</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>1000</width>
          <height>10</height>
         </size>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop</set>
        </property>
       </widget>
      </item>
      <item>
       <layout class="QVBoxLayout" name="verticalLayout">
        <property name="sizeConstraint">
         <enum>QLayout::SetMinimumSize</enum>
        </property>
        <item>
         <widget class="QLabel" name="events">
          <property name="enabled">
           <bool>true</bool>
          </property>
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="font">
           <font>
            <pointsize>18</pointsize>
            <weight>50</weight>
            <bold>false</bold>
           </font>
          </property>
          <property name="tabletTracking">
           <bool>false</bool>
          </property>
          <property name="acceptDrops">
           <bool>false</bool>
          </property>
          <property name="text">
           <string>Events</string>
          </property>
          <property name="textFormat">
           <enum>Qt::AutoText</enum>
          </property>
          <property name="scaledContents">
           <bool>false</bool>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
          <property name="wordWrap">
           <bool>false</bool>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_2">
        <item>
         <spacer name="horizontalSpacer_3">
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
         <layout class="QVBoxLayout" name="verticalLayout_3">
          <item>
           <widget class="QLabel" name="label">
            <property name="maximumSize">
             <size>
              <width>16777215</width>
              <height>500</height>
             </size>
            </property>
            <property name="text">
             <string/>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="addevent">
            <property name="minimumSize">
             <size>
              <width>200</width>
              <height>0</height>
             </size>
            </property>
            <property name="maximumSize">
             <size>
              <width>16777215</width>
              <height>16777215</height>
             </size>
            </property>
            <property name="layoutDirection">
             <enum>Qt::LeftToRight</enum>
            </property>
            <property name="text">
             <string>Add event</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <spacer name="horizontalSpacer_2">
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
       </layout>
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
         <widget class="QPushButton" name="back">
          <property name="minimumSize">
           <size>
            <width>100</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string>back</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>976</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
template_main = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>701</width>
    <height>414</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout_2">
    <item>
     <spacer name="horizontalSpacer">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>206</width>
        <height>17</height>
       </size>
      </property>
     </spacer>
    </item>
    <item>
     <layout class="QVBoxLayout" name="verticalLayout_2">
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
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <widget class="QPushButton" name="calendar">
          <property name="minimumSize">
           <size>
            <width>250</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string>Calendar</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="olimpiad">
          <property name="text">
           <string>Olimpiads</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="data">
          <property name="text">
           <string>Data</string>
          </property>
         </widget>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout">
          <item>
           <spacer name="horizontalSpacer_4">
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
           <widget class="QPushButton" name="log_out">
            <property name="minimumSize">
             <size>
              <width>0</width>
              <height>0</height>
             </size>
            </property>
            <property name="text">
             <string>Log out</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="dark_theme">
            <property name="text">
             <string>Dark theme</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
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
     <spacer name="horizontalSpacer_2">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>205</width>
        <height>17</height>
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
     <width>701</width>
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
template_olimpiads = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>624</width>
    <height>459</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout_4">
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout">
      <item>
       <widget class="QLabel" name="lvl">
        <property name="maximumSize">
         <size>
          <width>16777215</width>
          <height>40</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Ubuntu Mono</family>
          <pointsize>16</pointsize>
          <weight>50</weight>
          <bold>false</bold>
         </font>
        </property>
        <property name="text">
         <string>I lvl</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignCenter</set>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="lvl_2">
        <property name="maximumSize">
         <size>
          <width>16777215</width>
          <height>40</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Ubuntu Mono</family>
          <pointsize>16</pointsize>
          <weight>50</weight>
          <bold>false</bold>
         </font>
        </property>
        <property name="text">
         <string>2 lvl</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignCenter</set>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="lvl_3">
        <property name="maximumSize">
         <size>
          <width>16777215</width>
          <height>40</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Ubuntu Mono</family>
          <pointsize>16</pointsize>
          <weight>50</weight>
          <bold>false</bold>
         </font>
        </property>
        <property name="text">
         <string>3 lvl</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignCenter</set>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <item>
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <widget class="QPushButton" name="vishaya">
          <property name="text">
           <string>Высшая проба</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="mosh">
          <property name="text">
           <string>МОШ</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="kurch">
          <property name="text">
           <string>Курчатов</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="lomonosov">
          <property name="text">
           <string>Олимпиада «Ломоносов»</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="gori">
          <property name="text">
           <string>Покори Воробьевы горы!</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="fizteh">
          <property name="text">
           <string>Физтех</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="spgu">
          <property name="text">
           <string>Олимпиада СПБГУ</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="goroda">
          <property name="text">
           <string>Турнир городов</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <layout class="QVBoxLayout" name="verticalLayout_2">
        <item>
         <widget class="QPushButton" name="vsesib">
          <property name="text">
           <string>Всесибирская олимпиада</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="formula">
          <property name="text">
           <string>Формула Единства</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="verchenko">
          <property name="text">
           <string>Олимпиада И.Я. Верченко</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="mezvuz">
          <property name="text">
           <string>Межвузовская олимпиада</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="umsh">
          <property name="text">
           <string>Олимпиада ЮМШ</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="open">
          <property name="text">
           <string>Открытая олимпиада</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="rosatom">
          <property name="text">
           <string>Росатом</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="turlom">
          <property name="text">
           <string>Турнир Ломоносова</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <layout class="QVBoxLayout" name="verticalLayout_3">
        <item>
         <widget class="QPushButton" name="finansist">
          <property name="text">
           <string>Финансист</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="innopolis">
          <property name="text">
           <string>Innopolis Open</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="izumrud">
          <property name="text">
           <string>Изумруд</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="sammat">
          <property name="text">
           <string>САММАТ</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="bibn">
          <property name="text">
           <string>БИБН</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="shvb">
          <property name="text">
           <string>Шаг в будущее</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_3">
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
       <widget class="QPushButton" name="back">
        <property name="text">
         <string>Back</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>624</width>
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
template_page = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout_4">
    <item>
     <widget class="QLabel" name="name">
      <property name="font">
       <font>
        <family>Ubuntu Condensed</family>
        <pointsize>22</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>TextLabel</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
     </widget>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_8">
      <item>
       <widget class="QLabel" name="label_7">
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
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <layout class="QVBoxLayout" name="verticalLayout">
          <item>
           <layout class="QHBoxLayout" name="horizontalLayout_2">
            <item>
             <widget class="QLabel" name="label">
              <property name="text">
               <string>Ссылка:</string>
              </property>
             </widget>
            </item>
           </layout>
          </item>
          <item>
           <layout class="QHBoxLayout" name="horizontalLayout_7">
            <item>
             <widget class="QLabel" name="label_3">
              <property name="text">
               <string>Some info:  skufsdufgsldufsdf</string>
              </property>
             </widget>
            </item>
           </layout>
          </item>
         </layout>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QTextBrowser" name="about">
        <property name="readOnly">
         <bool>true</bool>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_3">
      <item>
       <widget class="QLabel" name="label_2">
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
       <widget class="QPushButton" name="back">
        <property name="text">
         <string>Back</string>
        </property>
       </widget>
      </item>
      <item>
       <spacer name="horizontalSpacer">
        <property name="orientation">
         <enum>Qt::Horizontal</enum>
        </property>
        <property name="sizeHint" stdset="0">
         <size>
          <width>358</width>
          <height>20</height>
         </size>
        </property>
       </spacer>
      </item>
      <item>
       <widget class="QPushButton" name="btn">
        <property name="minimumSize">
         <size>
          <width>200</width>
          <height>0</height>
         </size>
        </property>
        <property name="text">
         <string>Edit</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
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
template_calenda = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1107</width>
    <height>868</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout_2">
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <item>
       <widget class="QCalendarWidget" name="calendarWidget">
        <property name="minimumSize">
         <size>
          <width>700</width>
          <height>0</height>
         </size>
        </property>
       </widget>
      </item>
      <item>
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout">
          <item>
           <widget class="QPushButton" name="pushButton_3">
            <property name="minimumSize">
             <size>
              <width>0</width>
              <height>50</height>
             </size>
            </property>
            <property name="text">
             <string>Olimpiads</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="log_inBtn">
            <property name="minimumSize">
             <size>
              <width>50</width>
              <height>50</height>
             </size>
            </property>
            <property name="maximumSize">
             <size>
              <width>100</width>
              <height>16777215</height>
             </size>
            </property>
            <property name="text">
             <string>Log in</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <widget class="QLabel" name="label">
          <property name="enabled">
           <bool>true</bool>
          </property>
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="font">
           <font>
            <pointsize>18</pointsize>
            <weight>50</weight>
            <bold>false</bold>
           </font>
          </property>
          <property name="tabletTracking">
           <bool>false</bool>
          </property>
          <property name="acceptDrops">
           <bool>false</bool>
          </property>
          <property name="text">
           <string>Note:</string>
          </property>
          <property name="textFormat">
           <enum>Qt::AutoText</enum>
          </property>
          <property name="scaledContents">
           <bool>false</bool>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
          <property name="wordWrap">
           <bool>false</bool>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QTextEdit" name="textEdit"/>
        </item>
        <item>
         <widget class="QPushButton" name="pushButton_2">
          <property name="minimumSize">
           <size>
            <width>0</width>
            <height>40</height>
           </size>
          </property>
          <property name="text">
           <string>Save</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1107</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
template_addevent = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>359</width>
    <height>185</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <widget class="QComboBox" name="olybox">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>40</y>
     <width>181</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="label_oly">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>40</y>
     <width>81</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Олимпиада</string>
   </property>
  </widget>
  <widget class="QTimeEdit" name="time">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>70</y>
     <width>118</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="label_time">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>70</y>
     <width>47</width>
     <height>13</height>
    </rect>
   </property>
   <property name="text">
    <string>Время</string>
   </property>
  </widget>
  <widget class="QPushButton" name="save">
   <property name="geometry">
    <rect>
     <x>260</x>
     <y>140</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>Save</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

ex = ''


class SingInWind(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_sign_in)
        uic.loadUi(f, self)
        self.showMaximized()
        qdarktheme.setup_theme()
        main_win = QMainWindow()
        push_button = QPushButton("PyQtDarkTheme!!")
        main_win.setCentralWidget(push_button)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.sign_in.clicked.connect(self.go_to_main)
        self.sign_up.clicked.connect(self.go_to_sign_up)

    def go_to_main(self):
        if self.check() == self.password.text():
            global ex
            ex2 = MainWind(self.email.text())
            ex2.show()
            self.close()
            ex = ex2
        else:
            self.explain.setText('Wrong email or password')

    def go_to_sign_up(self):
        global ex
        ex2 = SignUpWind()
        ex2.show()
        self.close()
        ex = ex2

    def check(self):
        try:
            with sqlite3.connect("datausers") as con:
                cur = con.cursor()
                return cur.execute(f"SELECT password FROM users WHERE email='{self.email.text()}'").fetchall()[0][0]
        except Exception as s:
            print(s)
            return False


class SignUpWind(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_sign_up)
        uic.loadUi(f, self)
        self.showMaximized()
        qdarktheme.setup_theme()
        main_win = QMainWindow()
        push_button = QPushButton("PyQtDarkTheme!!")
        main_win.setCentralWidget(push_button)
        self.setWindowTitle("Sign up")

        self.Sign_in.clicked.connect(self.go_to_sign_in)
        self.Create.clicked.connect(self.create_btn)

    def create_btn(self):  # создаём акк
        if self.Password.text() == self.Password2.text():
            global ex
            check = add_user(self.Email.text(), self.Password.text())
            if check is True:
                ex2 = MainWind(self.Email.text())
                ex2.show()
                ex.close()
                ex = ex2
            else:
                self.error.setText(check)
        else:
            self.error.setText('Different passwords')

    def go_to_sign_in(self):
        global ex
        ex4 = SingInWind()
        ex4.show()
        ex.close()
        ex = ex4


class MainWind(QMainWindow):
    def __init__(self, email):
        super().__init__()
        f = io.StringIO(template_main)
        uic.loadUi(f, self)
        self.showFullScreen()

        self.email = email

        self.olimpiad.clicked.connect(self.go_to_olimpiads)
        self.log_out.clicked.connect(self.go_to_sign_in)
        self.dark_theme.clicked.connect(self.theme)
        self.calendar.clicked.connect(self.go_to_calendar)

        if get_theme(email) == 'light':
            qdarktheme.setup_theme("light")
            self.dark_theme.setText('Dark theme')
        else:
            qdarktheme.setup_theme()
            main_win = QMainWindow()
            push_button = QPushButton("PyQtDarkTheme!!")
            main_win.setCentralWidget(push_button)
            self.dark_theme.setText('Light theme')

    def theme(self):
        if self.sender().text() == 'Dark theme':
            self.color = "Dark"
            qdarktheme.setup_theme()
            main_win = QMainWindow()
            push_button = QPushButton("PyQtDarkTheme!!")
            main_win.setCentralWidget(push_button)
            self.dark_theme.setText('Light theme')
            set_theme(self.color, self.email)
        elif self.sender().text() == 'Light theme':
            self.color = "light"
            qdarktheme.setup_theme("light")
            self.dark_theme.setText('Dark theme')
            set_theme(self.color, self.email)

    def go_to_olimpiads(self):
        global ex
        ex4 = OlimpiadsWind(self.email)
        ex4.show()
        ex.close()
        ex = ex4

    def go_to_sign_in(self):
        global ex
        ex4 = SingInWind()
        ex4.show()
        ex.close()
        ex = ex4

    def go_to_calendar(self):
        global ex
        ex4 = CalendarWind(self.email)
        ex4.show()
        ex.close()
        ex = ex4


class OlimpiadsWind(QMainWindow):
    def __init__(self, email):
        super().__init__()
        f = io.StringIO(template_olimpiads)
        uic.loadUi(f, self)
        self.showFullScreen()
        self.setWindowTitle("List")

        self.email = email

        self.back.clicked.connect(self.go_to_main)
        self.vishaya.clicked.connect(self.olimp_page)
        self.mosh.clicked.connect(self.olimp_page)
        self.kurch.clicked.connect(self.olimp_page)
        self.lomonosov.clicked.connect(self.olimp_page)
        self.gori.clicked.connect(self.olimp_page)
        self.fizteh.clicked.connect(self.olimp_page)
        self.spgu.clicked.connect(self.olimp_page)
        self.goroda.clicked.connect(self.olimp_page)
        self.vsesib.clicked.connect(self.olimp_page)
        self.formula.clicked.connect(self.olimp_page)
        self.verchenko.clicked.connect(self.olimp_page)
        self.mezvuz.clicked.connect(self.olimp_page)
        self.open.clicked.connect(self.olimp_page)
        self.rosatom.clicked.connect(self.olimp_page)
        self.turlom.clicked.connect(self.olimp_page)
        self.finansist.clicked.connect(self.olimp_page)
        self.innopolis.clicked.connect(self.olimp_page)
        self.izumrud.clicked.connect(self.olimp_page)
        self.sammat.clicked.connect(self.olimp_page)
        self.bibn.clicked.connect(self.olimp_page)
        self.shvb.clicked.connect(self.olimp_page)

    def olimp_page(self):
        global ex
        ex2 = PageWind(self.sender().text(), self.email)
        ex2.show()
        ex.close()
        ex = ex2

    def go_to_main(self):
        global ex
        ex2 = MainWind(self.email)
        ex2.show()
        ex.close()
        ex = ex2

    def go_to_sign_in(self):
        global ex
        ex1 = SingInWind()
        ex1.show()
        ex.close()
        ex = ex1


class PageWind(QMainWindow):
    def __init__(self, btn_text, email):
        super().__init__()
        f = io.StringIO(template_page)
        uic.loadUi(f, self)
        self.showFullScreen()
        self.setWindowTitle("Page")

        self.email = email
        self.olimp = btn_text

        self.label.setText(f'<a href="{get_url(btn_text)}">Ссылка:</a>')
        # self.label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label.setOpenExternalLinks(True)
        self.label.linkActivated.connect(handle_link_activation)
        self.name.setText(btn_text)
        self.back.clicked.connect(self.go_to_olimpiads)
        self.btn.clicked.connect(self.edit)
        self.about.setText(get_note(btn_text, self.email))
        self.label_3.setText('Some info: inf0')

    def edit(self):
        if self.about.isReadOnly():
            self.about.setReadOnly(False)
            self.btn.setText('Confirm')
        else:
            set_note(self.olimp, self.about.toPlainText(), self.email)
            self.about.setReadOnly(True)
            self.btn.setText('Edit')

    def go_to_olimpiads(self):
        global ex
        ex2 = OlimpiadsWind(self.email)
        ex2.show()
        ex.close()
        ex = ex2


class CalendarWind(QMainWindow, Ui_MainWindow):
    def __init__(self, email):
        super().__init__()
        self.setupUi(self)
        self.showFullScreen()
        self.email = email

        self.back.clicked.connect(self.go_to_main)
        self.addevent.clicked.connect(self.addevent_wind)
        self.calendar.clicked.connect(self.qwerty)

        for name, time in get_event(self.email, f"{self.calendar.selectedDate()}"):
            button = QPushButton()
            button.setText(name + ' ' + f"{time}")
            button.setFixedWidth(self.addevent.width() * 2 + (self.events.width() - button.width()))
            button.setStyleSheet(f"margin-left: {(self.events.width() - button.width())}")
            self.events.setFixedHeight(200)
            self.verticalLayout.addWidget(button)

    def qwerty(self):
        for i in reversed(range(1, ex.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)
        for name, time in get_event(self.email, f"{self.calendar.selectedDate()}"):
            button = QPushButton()
            button.setText(name + ' ' + f"{time}")
            button.setFixedWidth(self.addevent.width() * 2 + (self.events.width() - button.width()))
            button.setStyleSheet(f"margin-left: {(self.events.width() - button.width())}")
            self.events.setFixedHeight(200)
            self.verticalLayout.addWidget(button)

    def go_to_main(self):
        global ex
        ex2 = MainWind(self.email)
        ex2.show()
        ex.close()
        ex = ex2

    def addevent_wind(self):
        dlg = AddeventWind(self.email)
        dlg.exec()


class AddeventWind(QDialog):
    def __init__(self, email):
        super().__init__()
        f = io.StringIO(template_addevent)
        uic.loadUi(f, self)
        self.setWindowTitle("Add event")

        self.email = email
        self.olybox.addItems(get_olys())
        self.save.clicked.connect(self.save_btn)

    def save_btn(self):
        for i in reversed(range(1, ex.verticalLayout.count())):
            ex.verticalLayout.itemAt(i).widget().setParent(None)
        set_date(self.email, f"{ex.calendar.selectedDate()}", self.olybox.currentText(),
                 f"{self.time.time().hour()}.{self.time.time().minute()}")
        for name, time in get_event(self.email, f"{ex.calendar.selectedDate()}"):
            button = QPushButton()
            button.setText(name + ' ' + f"{time}")
            button.setFixedWidth(ex.addevent.width() * 2 + (ex.events.width() - button.width()))
            button.setStyleSheet(f"margin-left: {(ex.events.width() - button.width())}")
            ex.events.setFixedHeight(200)
            ex.verticalLayout.addWidget(button)
        self.close()
