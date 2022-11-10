# happy_topic
## 概要
２章のサンプルプログラム．topic通信．
- happy_topic/happy_publisher_node.py  (プログラムリスト2.7)
- happy_topic/happy_subscriber_node.py (プログラムリスト2.8)

## バグ情報
- Dockerコンテナのhappy_topicパッケージにバグがありました．chapter2/happy_topic/happy_topic/happy_subscriber.pyの以下の行を次のように変更してください．なお，githubのコードは修正済みです．
  - 7行目：　誤　class HappyPublisher(Node):　正　class HappySubscriber(Node):　　
  - 20行目： 誤　node = HappyPublisher()      正　node = HappySubscriber():　
  
## インストール
Chapter2のパッケージは全部まとめてインストール・ビルドをします．
- [第2章 インストール](https://github.com/AI-Robot-Book/chapter2)を参照してください．

## 実行  
端末で以下のコマンドを実行
```
cd ~/airobot_ws
source install/setup.bash
ros2 run happy_topic happy_publisher_node
```

## ヘルプ
- 今のところありません．
　
 
## 著者
出村 公成


## 履歴
- 2022-11-08: happy_subscriber_node.pyのノード名がこの本と違っていたので，それに伴う7行と20行の変更．
- 2022-08-29: 初期版


## ライセンス
Copyright (c) 2022, Kosei Demura All rights reserved. This project is licensed under the Apache License 2.0 license found in the LICENSE file in the root directory of this project.


## 参考文献
- 今のところありません．
