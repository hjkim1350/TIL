<template>
  <div id="app">

  <form @submit.prevent="submitForm">
    <div class="form-group row d-flex justify-content-center mb-5">
      <input type="text" class="form-control w-auto mx-2" placeholder="Name" v-model="student.name">
      <input type="text" class="form-control w-auto mx-2" placeholder="Course" v-model="student.course">
      <input type="text" class="form-control w-auto mx-2" placeholder="Rating" v-model="student.rating">
      <button class="btn btn-success mt-2">Submit</button>
    </div>
  </form>

    <table class="table">
      <thead>
        <th>Name</th>
        <th>Course</th>
        <th>Rating</th>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id" @dblclick="$data.student = student">
          <td>{{ student.name }}</td>
          <td>{{ student.course }}</td>
          <td>{{ student.rating }}</td>
          <td><button class="btn btn-outline-danger btn-sm mx-1" @click="deleteStudent(student)">x</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
      student: {},
      students: []
    }
  },

  async created(){
    await this.getStudents();
  },

  methods: {
    submitForm() {
      if (this.student.id === undefined){
        this.createStudent();
      } else {
        this.editStudent();
      }
    },

    async getStudents(){
      var response = await fetch('http://localhost:8000/api/students/')
      this.students = await response.json();
    },

    async createStudent(){
      await this.getStudents();

      await fetch('http://localhost:8000/api/students/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudents();
    },

    async editStudent(){
      await this.getStudents();

      await fetch(`http://localhost:8000/api/students/${this.student.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudents();
      this.student = {};
    },

    async deleteStudent(student){
      await this.getStudents();

      await fetch(`http://localhost:8000/api/students/${student.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudents();
      this.student = {};
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
