import React from 'react';
import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from './store/store';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Reactルート要素の作成
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    {/* Reduxストアをアプリケーション全体で利用可能にする */}
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);

// パフォーマンス計測のための関数（必要に応じて使用）
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();