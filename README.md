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
