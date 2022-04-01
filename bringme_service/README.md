# bringme_service: airobot_interfacesを使ったサンプルパッケージ  

## 使いかた  
### 端末を２つに分割する．
### 1番目の端末で次のコマンドを実行する．  
```
ros2 run bringme_service bringme_service_node  
```
### 2番目の端末で次のコマンドを実行する．
```
ros2 run bringme_service bringme_client_node
何をとってきますか：
```
と聞かれるので，取ってきて欲しい英単語を入力する．
'apple', 'banana', 'candy'を入力すると"はい，これです．”とレスポンスが返る，
それ以外は"見つけることができませんでした．”とレスポンスが返る．
