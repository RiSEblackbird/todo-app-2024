import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

// 非同期アクションクリエーター: バックエンドAPIからタスクを取得する
// App.jsのuseEffectフック内で使用される
export const fetchTasks = createAsyncThunk('tasks/fetchTasks', async () => {
  const response = await axios.get('http://localhost:3005/api/v1/tasks');
  return response.data;
});

// タスク管理用のReduxスライス
const tasksSlice = createSlice({
  name: 'tasks',
  initialState: {
    items: [],     // タスクの配列
    status: 'idle', // APIリクエストの状態（'idle', 'loading', 'succeeded', 'failed'）
    error: null     // エラーメッセージ（存在する場合）
  },
  reducers: {},
  // 非同期アクションに対する追加のケース処理
  extraReducers: (builder) => {
    builder
      .addCase(fetchTasks.pending, (state) => {
        // リクエスト開始時の処理
        state.status = 'loading';
      })
      .addCase(fetchTasks.fulfilled, (state, action) => {
        // リクエスト成功時の処理
        state.status = 'succeeded';
        state.items = action.payload;
      })
      .addCase(fetchTasks.rejected, (state, action) => {
        // リクエスト失敗時の処理
        state.status = 'failed';
        state.error = action.error.message;
      });
  }
});

export default tasksSlice.reducer;