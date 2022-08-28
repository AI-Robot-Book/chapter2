# 第２章　はじめてのROS2
## 概要
ROS2とPythonで作って学ぶAIロボット入門（出村・萩原・升谷・タン著，講談社）第２章のサンプルプログラムと補足情報などを掲載しています．

## ディレクトリ構成
- **airobot_interfaces**: 「AI Robot Book」のためのインタフェース定義 (升谷 保博) 
- **bringme_service**: airobot_interfacesを使ったサンプルパッケージ 
- **happy**: はじめてのROS2パッケージ 
- **happy_action**: action用のサンプルパッケージ 
- **happy_action_interfaces**: happy_action用のインタフェース定義 
- **happy_interfaces**: happy用のインタフェース定義 
- **happy_mini_turtlebot3_sim**: Happy Miniシミュレータ
- **happy_service**: service用のサンプルパッケージ 
- **happy_topic**: topic用のサンプルパッケージ
- **hello**: ros2 pkg createコマンドで自動生成されたパッケー
- **map**: 地図ファイルを格納するディレクトリ
- **turtlesim_launch**: タートルシム用のローンチファイル 

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
