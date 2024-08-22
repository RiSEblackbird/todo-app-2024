import { configureStore } from '@reduxjs/toolkit';
import tasksReducer from './tasksSlice';

// Reduxストアの設定
// tasksReducer: タスク関連の状態を管理するリデューサー
export const store = configureStore({
  reducer: {
    tasks: tasksReducer,
  },
});