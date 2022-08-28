# bringme_service:  
## 概要
２章のサンプルプログラム  
airobot_interfacesを使ったサンプルパッケージ


## インストール
Chapter2のパッケージは全部まとめてインストール・ビルドをします．
- [第2章 インストール](https://github.com/AI-Robot-Book/chapter2)を参照してください．


## 実行  
- 端末を２つに分割する．
- 1番目の端末で次のコマンドを実行する．  
```
ros2 run bringme_service bringme_service_node  
```
- 2番目の端末で次のコマンドを実行する．
```
ros2 run bringme_service bringme_client_node
何をとってきますか：
```
と聞かれるので，取ってきて欲しい英単語を入力する．  
'apple', 'banana', 'candy'を入力すると **"はい，これです．”** とレスポンスが返る，  
それ以外は **"見つけることができませんでした．”** とレスポンスが返る．


## ヘルプ
- 今のところありません．
　
 
## 著者
出村 公成


## 履歴
- 2022-08-29: 初期版


## ライセンス
Copyright (c) 2022, Kosei Demura All rights reserved. This project is licensed under the Apache-2.0 license found in the LICENSE file in the root directory of this project.


## 参考文献
- 今のところありません．

