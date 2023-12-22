<template>
    <div class="login-page">
        <div class="login-container">
            <form name="login-form" @submit.prevent="handleSubmit">
            <div class="mb-3">
                <label for="username">PeopleSoftID: </label>
                <input id="username" v-model="peoplesoft" type="text" />
            </div>
            <div class="mb-3">
                <label for="password">Password: </label>
                <input id="password" v-model="password" type="password" />
            </div>
            <button class="btn btn-outline-dark" type="submit">
                Login
            </button>
            </form>
        </div>
    </div>
</template>


<script setup>
import { useRouter } from 'vue-router';
import store from '@/store';

const router = useRouter();
let peoplesoft = '';
let password = '';

store.commit('setProfile', { name: 'John Doe', permissions: '1', email: '', password: '', netId: '', peopleSoftId: '502', classes: []});

function convertDynamoDBData(data) {
  return Object.entries(data).reduce((obj, [key, value]) => {
    const dataType = Object.keys(value)[0];
    obj[key] = value[dataType];
    return obj;
  }, {});
}

function handleSubmit() {
    const uri = 'https://8ip466ik32.execute-api.us-east-1.amazonaws.com/API';
  
    const headers = {
      'Content-Type': 'application/json',
      'x-amz-docs-region': 'us-east-1'
    };
  
    const para = {
    "operation": "query_profile",
    "peoplesoftID": peoplesoft
}
    let self = this;
    fetch(uri, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(para)
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      const items = data.Items.map(convertDynamoDBData);
      if ((items[0].password) === password){
        alert("Login Successful")
        store.commit('setProfile', items[0]);
        router.push('/Husky37');
      }
      else{
        alert("Incorrect Password");
      }
    })
    .catch(error => {
      alert("Incorrect Username");
      console.error('There was an error!', error);
    });
  }
</script>


<style scoped>
.login-page {
  height: 100vh; 
  background-image: url('../assets/foggystorrs.jpeg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.login-container {
  background-color: rgba(255, 255, 255, 0.8); 
  padding: 50px;
  border-radius: 50px; 
  max-width: 400px; 

  margin: auto; 
  
}

.login-container label {
    font-size: 30px;
    color: #000E2F;
    
}


.login-container input {
    font-size: 30px;
    border-radius: 10px;
    color: #000E2F;
    width: 100%;
}

.login-container button {
    display: block;
    margin-left: auto;
    margin-right: auto;
    font-size: 30px;
    margin-top: 20px;
    border-radius: 5px;
    padding: 10px;
    background-color:#000E2F;
    color:white;
}

</style>