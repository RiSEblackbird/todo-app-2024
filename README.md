# todo-app-2024

- コンテナのビルドと起動
    - `docker-compose up --build`

- コンテナをダウン（通常時）
    - `docker-compose down`
- ボリュームごとコンテナをダウン
    - `docker-compose down -v`

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

- キャッシュのクリアと再ビルド:Docker buildのキャッシュをクリアして、フロントエンドコンテナを完全に再ビルド
    - `docker-compose build --no-cache frontend`
    - `docker-compose up --force-recreate frontend`

- コンテナのログの確認
    - `docker-compose logs db`
- MySQLコンテナが正常に起動しているか確認
    - `docker-compose exec db mysql -uroot -prootpassword -e "SHOW DATABASES;"`
- ポート3000の使用状況を確認
    - `netstat -ano | findstr :3000`
- プロセスを終了
    - `taskkill /PID <プロセスID> /F`

---------------
- bundle installが正しく実行されたか確認
    - `docker-compose run --rm backend bundle check`

- Gemfile更新後のgenインストール
    - docker-compose run --rm backend bundle install --gemfile

- rails console
    - `docker-compose run --rm backend rails console`
        - <details><summary>ex. サンプルタスク作成</summary>
        
            ```
            backend(dev)> Task.create(title: "First task", description: "This is the first task", status: "To Do")
            TRANSACTION (0.5ms)  BEGIN
            Task Create (12.0ms)  INSERT INTO `tasks` (`title`, `description`, `status`, `created_at`, `updated_at`) VALUES ('First task', 'This is the first task', 'To Do', '2024-08-22 15:42:41.719441', '2024-08-22 15:42:41.719441')
            TRANSACTION (17.7ms)  COMMIT
            => 
            #<Task:0x00007f1c0ce222f8
            id: 1,
            title: "First task",
            description: "This is the first task",
            status: "To Do",
            created_at: "2024-08-22 15:42:41.719441000 +0000",
            updated_at: "2024-08-22 15:42:41.719441000 +0000">
            backend(dev)> Task.create(title: "Second task", description: "This is the second task", status: "In Progress")
            TRANSACTION (1.3ms)  BEGIN
            Task Create (4.7ms)  INSERT INTO `tasks` (`title`, `description`, `status`, `created_at`, `updated_at`) VALUES ('Second task', 'This is the second task', 'In Progress', '2024-08-22 15:42:52.405834', '2024-08-22 15:42:52.405834')
            TRANSACTION (12.8ms)  COMMIT
            => 
            #<Task:0x00007f1c0cb9a508
            id: 2,
            title: "Second task",
            description: "This is the second task",
            status: "In Progress",
            created_at: "2024-08-22 15:42:52.405834000 +0000",
            updated_at: "2024-08-22 15:42:52.405834000 +0000">
            ```
        </details>

- rspecのインストール
    - `docker-compose run --rm backend rails generate rspec:install`
    - 最初のテストデータベース作成: `docker-compose run --rm backend rails db:test:prepare`
    - 実行: `docker-compose run --rm test`
----------------

- Reactのトップページ
    - http://localhost:3001