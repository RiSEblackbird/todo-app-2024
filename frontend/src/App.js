import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchTasks } from './store/tasksSlice';
import { Container, Typography, List, ListItem, ListItemText } from '@mui/material';

function App() {
  const dispatch = useDispatch();
  // Reduxストアからタスクの配列を取得
  const tasks = useSelector(state => state.tasks.items);
  // Reduxストアからタスクの読み込み状態を取得
  const taskStatus = useSelector(state => state.tasks.status);

  // コンポーネントのマウント時にタスクを取得
  useEffect(() => {
    if (taskStatus === 'idle') {
      dispatch(fetchTasks());
    }
  }, [taskStatus, dispatch]);

  return (
    <Container>
      <Typography variant="h4" component="h1" gutterBottom>
        Task Management
      </Typography>
      {/* タスクのリストを表示 */}
      <List>
        {tasks.map(task => (
          <ListItem key={task.id}>
            <ListItemText primary={task.title} secondary={task.description} />
          </ListItem>
        ))}
      </List>
    </Container>
  );
}

export default App;