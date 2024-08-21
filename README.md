# todo-app-2024
 
`docker-compose up --build`

`docker-compose down -v`

- backendコンテナ再ビルド（起動中も実行可能）
    - `docker-compose build backend`

- Docker ネットワークを確認
    - `docker network ls`
- バックエンドコンテナ内で DB_HOST 環境変数の確認
    - `docker-compose exec backend env | grep DB_HOST`

- バックエンドコンテナ内で `/etc/hosts` ファイルを確認します
    - `docker-compose exec backend cat /etc/hosts`

- バックエンドコンテナ内から db ホストに ping を試みる
    - `docker-compose exec backend ping db`

- バックエンドコンテナ内から直接 MySQL に接続
    - `docker-compose exec backend mysql -h db -u root -prootpassword`
- コンテナのログの確認
    - `docker-compose logs db`
- MySQLコンテナが正常に起動しているか確認
    - `docker-compose exec db mysql -uroot -prootpassword -e "SHOW DATABASES;"`
- ポート3000の使用状況を確認
    - `netstat -ano | findstr :3000`
- プロセスを終了
    - `taskkill /PID <プロセスID> /F`

- bundle installが正しく実行されたか確認
    - `docker-compose run --rm backend bundle check`

- rspecのインストール
    - `docker-compose run --rm backend rails generate rspec:install`
    - 最初のテストデータベース作成: `docker-compose run --rm backend rails db:test:prepare`
    - 実行: `docker-compose run --rm test`
----------------

- Reactのトップページ
    - http://localhost:3001