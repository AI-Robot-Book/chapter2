# 第２章　はじめてのROS2
## 概要
ROS2とPythonで作って学ぶAIロボット入門（出村・萩原・升谷・タン著，講談社）第２章のサンプルプログラムと補足情報などを掲載しています．

## ディレクトリ構成
- **[airobot_interfaces](airobot_interfaces)**: 「AI Robot Book」のためのインタフェース定義 (升谷 保博) 
- **[bringme_service](bringme_service)**: airobot_interfacesを使ったサンプルパッケージ 
- **[happy](happy)**: はじめてのROS2パッケージ 
- **[happy_action](happy_action)**: action用のサンプルパッケージ 
- **[happy_action_interfaces](happy_action_interfaces)**: happy_action用のインタフェース定義 
- **[happy_interfaces](happy_interfaces)**: happy用のインタフェース定義 
- **[happy_service](happy_service)**: service用のサンプルパッケージ 
- **[happy_topic](happy_topic)**: topic用のサンプルパッケージ（プログラムリスト2.6, 2.7）
- **[hello](hello)**: ros2 pkg createコマンドで自動生成されたパッケージ
- **[turtlesim_launch](turtlesim_launch)**: タートルシム用のローンチファイル 

## サンプルプログラム一覧
- プログラムリスト2.1 package.xml
- プログラムリスト2.2 setup.py
- プログラムリスト2.3 hello_node.py
- プログラムリスト2.4 happy_node.py
- プログラムリスト2.5 happy_node2.py
- プログラムリスト2.6 happy_node3.py
- プログラムリスト2.7 happy_publisher_node.py
- プログラムリスト2.8 happy_subscriber_node.py
- プログラムリスト2.9 package.xml
- プログラムリスト2.10 setup.py
- プログラムリスト2.11 happy_pub_sub.py
- プログラムリスト2.12 StringCommand.srv
- プログラムリスト2.13 bringme_service_node.py
- プログラムリスト2.14 bringme_client_node.py
- プログラムリスト2.15 CMakeLists.txt
- プログラムリスト2.16 package.xml
- プログラムリスト2.17 setup.py

## インストール
Chapter2の全パッケージを以下のコマンドでインストールします．
- ROSのワークスペースを`~/airobot_ws`とする．
  ```
  cd ~/airobot_ws/src
  ```

- Chapter2のリポジトリを入手
  ```
  git clone https://github.com/AI-Robot-Book/chapter2
  ```
  
- パッケージのビルド   
  ```
  cd ~/airobot_ws  
  colcon build
  ```



## 補足情報
