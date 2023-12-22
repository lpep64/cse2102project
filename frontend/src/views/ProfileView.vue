<template>
  <div class="Profile">
    <h2>User Profile</h2>
    <!-- Add your schedule content here -->
    <div class="table-container">
      <table>
        <tbody>
          <tr>
            <th>Name</th>
            <td>{{ profile && profile.username }}</td>
          </tr>
          <tr>
            <th>Permissions</th>
            <td>{{ role }}</td>
          </tr>
          <tr>
            <th>Email Address</th>
            <td>{{ profile && profile.email }}</td>
          </tr>
          <tr>
            <th>NetID</th>
            <td>{{ profile && profile.NetID }}</td>
          </tr>
          <tr>
            <th>PeopleSoftID</th>
            <td>{{ profile && profile.peoplesoftID }}</td>
          </tr>
          <tr>
            <th>Password</th>
            <td>{{ profile && profile.password }}</td>
          </tr>
        </tbody>
      </table>
      <p v-if="role === 'Admin'">Your role is: {{ role }}, As an admin you can add and delete profiles.<br>
        When Updating your own profile please note that changes will not be visible until you next login.<br>
        Deleting Profiles only requires PeopleSoftID</p>
      <table v-if="role === 'Admin'">
        <tbody>
          <tr>
            <th>Name</th>
            <th>Permissions</th>
            <th>Email Address</th>
            <th>NetID</th>
            <th>PeopleSoftID</th>
            <th>Password</th>
          </tr>
          <tr>
            <td><input id="username" v-model="username" type="text" /></td>
            <td><input id="permissions" v-model="permissions" type="text" /></td>
            <td><input id="email" v-model="email" type="text" /></td>
            <td><input id="NetID" v-model="NetID" type="text" /></td>
            <td><input id="peoplesoftID" v-model="peoplesoftID" type="text" /></td>
            <td><input id="password" v-model="password" type="text" /></td>
          </tr>
        </tbody> 
      </table>
      <div class="button-container" v-if="role === 'Admin'">
        <button class="button" @click="addProfile">Add/Update Profile</button>
        <button class="button" @click="deleteProfile">Delete Profile</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'CurrentUser',
  computed: {
    ...mapState(['profile']),
    role() {
      if (!this.profile || !this.profile.permissions) {
        return '';
      }
      switch (this.profile.permissions) {
        case '1':
          return 'Student';
        case '2':
          return 'Teacher';
        case '3':
          return 'Admin';
        default:
          return '';
      }
    },
  },
  methods: {
    addProfile() {
      let username = '';
      let permissions = '';
      let email = '';
      let NetID = '';
      let peoplesoftID = '';
      let password = '';
      
      if (
        this.peoplesoftID === '' ||
        this.username === '' ||
        this.email === '' ||
        this.NetID === '' ||
        this.password === ''
      ) {
        alert('All fields must be filled');
        return;
      }

      if (isNaN(this.peoplesoftID)) {
        alert('PeopleSoft ID must be a number');
        return;
      }

      if (this.permissions !== 'Student' && this.permissions !== 'Teacher' && this.permissions !== 'Admin') {
        alert('Permissions must be either Student, Teacher, or Admin');
        return;
      }

      const admintet = this.permissions === 'Student' ? '1' : this.permissions === 'Teacher' ? '2' : '3';

      const uri = 'https://8ip466ik32.execute-api.us-east-1.amazonaws.com/API';
  
      const headers = {
        'Content-Type': 'application/json',
        'x-amz-docs-region': 'us-east-1'
      };
  
      const para = {
      "operation": "add_profile",
      "peoplesoftID": this.peoplesoftID,
      "username": this.username,
      "email": this.email,
      "NetID": this.NetID,
      "password": this.password,
      "permissions": admintet
      } 
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
      alert("Profile Added/Updated");
    })
    .catch(error => {
      alert("Something went wrong");
    });
    },
    deleteProfile() {
      let peoplesoftID = '';

      if (isNaN(this.peoplesoftID)) {
        alert('PeopleSoft ID must be a number');
        return;
      }
      const uri = 'https://8ip466ik32.execute-api.us-east-1.amazonaws.com/API';
  
      const headers = {
        'Content-Type': 'application/json',
        'x-amz-docs-region': 'us-east-1'
      };
  
      const para = {
      "operation": "delete_profile",
      "peoplesoftID": this.peoplesoftID,
      } 
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
        alert("Profile Deleted");
      })
      .catch(error => {
        alert("Something went wrong");
      });
      }
    }
  };
</script>

<style scoped>
.Profile {
  padding: 1rem;
  text-align: center;
}
.Profile h2 {
  font-size: 40px;
  margin-bottom: 1rem;
  color: #000E2F;
}
.table-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 1rem;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 0.5rem;
  border: 1px solid #000;
}
th {
  background-color: #000E2F;
  color: #FFF;
}
.button-container {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px; /* Add this line */
}
.button {
  font-size: 20px;
  border-radius: 5px;
  padding: 20px;
  background-color:#000E2F;
  color:white;
}


</style>