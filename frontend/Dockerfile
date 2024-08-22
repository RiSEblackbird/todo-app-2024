# Node.js 20をベースイメージとして使用
FROM node:20

# アプリケーションディレクトリの作成
WORKDIR /app

# package.jsonとpackage-lock.jsonをコピーして依存関係をインストール
COPY package*.json ./
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

# 開発サーバーを起動
CMD ["npm", "start"]
