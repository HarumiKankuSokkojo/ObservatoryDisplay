サークルディスプレイ+測候所  by 晴海管区測候所

Raspberry Pi と BME280 を用い、即売会の会場などで
サークルのディスプレイと温湿度の表示を行います。

Copyright  2016  Hiroyuki Yata
All files except bin/bme280.patch is licensed under MIT Licence.
bin/bme280.patch requires codes of SWITCHSCIENCE.
https://github.com/SWITCHSCIENCE/BME280

bin/bme280.patch 以外のファイルは MIT ライセンスで提供されます。
ただし bin/bme280.patch については、スイッチサイエンスによるコードが必要です。
https://github.com/SWITCHSCIENCE/BME280

revisions
2016/10/28
初期バージョン
2018/12/10
毎秒ログを取る logger.py と html+グラフ作成の drawgraph.py に分離

含まれるファイル
INSTALL
README.md
bin/bme280.patch
bin/climate.plt.base
bin/logger.py
bin/drawgraph.py
html/graph.html.base


