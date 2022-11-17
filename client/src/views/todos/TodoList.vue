<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <span 
          @click="updateTodoStatus(todo)" 
          :class="{ 'is-completed': todo.is_completed }"
        >
        {{ todo.title }}
        </span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: null,
    }
  },
  methods: {
    getTodos: function () {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/todos/`,
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
        .then(res => {
          console.log(res)
          this.todos = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      const token = localStorage.getItem('jwt')
      // 3번 문제
      axios({
        method: 'delete',
        url: `${API_URL}/todos/${todo.id}/`,
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
        .then((res)=>{
          this.getTodos()
          console.log(res)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    updateTodoStatus: function (todo) {
      const token = localStorage.getItem('jwt')
      // 4번 문제
      console.log('debug', todo)
      axios({
        method: 'put',
        url: `${API_URL}/todos/${todo.id}/`,
        data: {
          title: todo.title,
          is_completed: !todo.is_completed,
        },
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
        .then((res)=>{
          this.getTodos()
          console.log(res)
        })
        .catch((err)=>{
          console.log(err)
        })
      console.log(todo)
    },
  },
  mounted () {
    const token = localStorage.getItem('jwt')
    axios({
      method: 'get',
      url: `${API_URL}/todos/`,
      headers: {
          'Authorization': `Bearer ${token}`,
      },
    })
      .then(res => {
        this.todos = res.data
        this.getTodos()
      })
      .catch(err => {
        console.log(err)
      })
  },
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
