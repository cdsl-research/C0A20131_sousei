# C0A20131_souseikadai

# 概要
これは, サーバー機器の自作監視モジュールとその設定ファイルである. 必要に応じてモジュールを新しく作ることも可能．

### 設定ファイル
conf.yaml→設定ファイル

モジュールの選択と条件の記載を行う.

モジュールの追加はここで行う.

### 実行ファイル
run.py→実行ファイル

このプログラムファイル実行すると設定ファイルで選んだモジュールが動く.


### 動かし方
例としてaliveとdnsをうごかす．
conf.yamlを記述
```python
module: #ここのモジュールの設定を記述
  dns: #名前解決
    dns_count: 3 #名前解決を何回行うか
    domain_name: manato-log #ドメイン名
  web: #外形監視
    web_count: 3 #外形監視を何回行うか
    web_url: http://192.168.100.143/manato/ #外形監視用URL
  log: #ログ監視
    log_count: 3 #ログ監視を何回行うか
    log_path: /var/log/td-agent/nginx/access.log.b5ebd3b0e0e07075e159e85ea77a52e9f.log #ログファイルのパス
  alive: #死活監視
    alive_count: 3 #死活監視を何回行うか
    alive_server_ipaddr: #死活監視を行いたいIPアドレス
    - 192.168.100.143 #IPアドレス
  path: #経路監視
    path_count: 3 #経路監視を何回行うか
    path_server_ipaddr: #経路監視を行いたいIPアドレス
    - 192.168.100.143 #IPアドレス
    - 192.168.150.10

conditions: |- #条件記載部
  if module_list[1].main(**list[1]) == "成功":
      module_list[4].main(**list[4])
      module_list[1].main(**list[1])
```




