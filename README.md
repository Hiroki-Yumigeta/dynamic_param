# dynamic_param
dynamic_reconfigureとrqt_reconfigureの使い方

# はじめに
このパッケージは
2つのlaunchファイルに分かれています。
* launch/dynamic_param.launch
* launch/cv_calibration.launch
## dynamic_param.launch
これは
「
[空飛ぶロボットのつくりかた](http://robonchu.hatenablog.com/entry/2017/02/21/230903)」さんのサンプルを元に作成にしています。
詳しい作り方はこちらを参照ください

## cv_calibration.launch
これは応用例として作成しました。機能は以下のとおりです
* rqt_reconfigureを利用としたパラメータの動的制御とyamlに保存
* yamlファイルからの読み出し
* OpenCVによるパラメータ変更の可視化

# 設定

## 新規作成する場合
### パッケージ作成
``` ROS
catkin create_pkg <package_name> rospy roscpp dynamic_reconfigure
```
### CMakeLists.txtの編集
* 以下を追加する
```CMakeLists
generate_dynamic_reconfigure_options(
  <config file>.cfg
)
add_dependencies(<executable> <packagename>_gencfg)
```

## 既存のパッケージに追加する場合
* 以下を追加する
### CMakeLists.txtの編集
```CMakeLists
...

find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure # add
  roscpp
  rospy
)

...

generate_dynamic_reconfigure_options(
  <config file>.cfg
  ...
)

...

catkin_package(
  ...
  CATKIN_DEPENDS dynamic_reconfigure roscpp rospy
  ...
)
```

## package.xmlの編集
* 以下を追加する
``` XML
  ...

  <build_depend>dynamic_reconfigure</build_depend>

  ...

  <build_export_depend>dynamic_reconfigure</build_export_depend>

  ...

  <exec_depend>dynamic_reconfigure</exec_depend>

  ...
```