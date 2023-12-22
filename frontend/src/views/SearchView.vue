<template>
  <div class="Profile">
    <h2>Course Search</h2>
    <input id="searchBar" v-model="searchQuery" type="text" placeholder="Search..." />
    <button class="buttonmain" @click="handleSearch">Search</button>
      <table>
        <tbody>
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Sections, Dates and Time</th>
            <th>Teachers</th>
            <th>Students</th>
          </tr>
          <tr v-for="(item, index) in items" :key="index">
            <td>{{ item.name }}</td>
            <td>{{ item.description }}</td>
            <td>{{ item.secdatetime }}</td>
            <td>{{ item.teachers }}</td>
            <td>{{ item.students }}</td>
          </tr>
        </tbody> 
      </table>
      <table>
      <tbody>
        <tr>
          <th>Student PeopleSoftID</th>
          <th>Course Name</th>
        </tr>
        <tr>
          <td><input id="peoplesoft" type="text" v-model="peoplesoft" placeholder="7 Digit ID..." /></td>
          <td><input id="courseName" type="text" v-model="courseName" placeholder="Name of Course"/></td>
        </tr>
     </tbody>
    </table>
  <button class="buttonsec" @click="addStudentToCourse">Add Student to Course</button>
  <button class="buttonsec" @click="deleteStudentFromCourse">Delete Student from Course</button>

    <table>
      <tbody>
        <tr>
          <th>Course Name</th>
          <th>Description</th>
          <th>Section, Date, Time</th>  
        </tr>
        <tr>
          <td><input id="newCourseName" type="text" v-model="newCourseName" placeholder="Required"/></td>
          <td><input id="description" type="text" v-model="description" placeholder="Description of new course"/></td>
          <td><input id="secdatetime" type="text" v-model="secdatetime" placeholder="1.M@10:11,Th@10:11"/></td>
        </tr>
      </tbody>
    </table>
    <button class="buttonsec" @click="addCourse">Add/Update Course</button>
    <button class="buttonsec" @click="deleteCourse">Delete Course</button>
    </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      // Other data properties
    };
  },
  methods: {
    handleSearch() {
      const uri = 'https://8ip466ik32.execute-api.us-east-1.amazonaws.com/API';
      
      const headers = {
        'Content-Type': 'application/json',
        'x-amz-docs-region': 'us-east-1'
      };
  
      const para = {
      "operation": "query_course",
      "name": this.searchQuery
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
        if (data.Items.length == 0) {
          alert("Course Not Found");
          return;
        }
        alert("Course Found");
        this.items = data.Items.map(item => ({
        name: item.name.S,
        description: item.description.S,
        secdatetime: item.secdatetime.SS,
        teachers: item.teachers.NS,
        students: item.students.NS
    // Other properties
      }));
  
      })
      .catch(error => {
        alert("Something went wrong");
      });
    },
    addStudentToCourse() {
      const uri = 'https://8ip466ik32.execute-api.us-east-1.amazonaws.com/API';
  
      const headers = {
        'Content-Type': 'application/json',
        'x-amz-docs-region': 'us-east-1'
      };

      const para = {
      "operation": "add_student_course",
      "peoplesoftID": this.peoplesoft,
      "name": this.courseName
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
      })
      .then(data => {
        alert("Student Added to Course");
      })
      .catch(error => {
        alert("Something went wrong");
      });
    },
    deleteStudentFromCourse() {
      const uri = 'https://8ip466ik32.execute-api.us-east-1.amazonaws.com/API';
  
      const headers = {
        'Content-Type': 'application/json',
        'x-amz-docs-region': 'us-east-1'
      };
  
      const para = {
      "operation": "delete_student_course",
      "peoplesoftID": this.peoplesoft,
      "name": this.courseName
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
      })
      .then(data => {
        alert("Student Deleted from Course");
      })
      .catch(error => {
        alert("Something went wrong");
      });    },
    addCourse() {
      const uri = 'https://8ip466ik32.execute-api.us-east-1.amazonaws.com/API';
      
      const headers = {
        'Content-Type': 'application/json',
        'x-amz-docs-region': 'us-east-1'
      };
      const para = {
        "operation": "add_course",
        "name": this.newCourseName,
        "description": this.description,
        "secdatetime": [this.secdatetime],
        "teachers": ["0"],
        "students": ["0"] 
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
      })
      .then(data => {
        alert("Course Added to Catalog");
      })
      .catch(error => {
        alert("Something went wrong");
      });
    },
    deleteCourse() {
      const uri = 'https://8ip466ik32.execute-api.us-east-1.amazonaws.com/API';
      
      const headers = {
        'Content-Type': 'application/json',
        'x-amz-docs-region': 'us-east-1'
      };

      const para = {
      "operation": "delete_course",
      "name": this.newCourseName
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
      })
      .then(data => {
        alert("Course Deleted from Catalog");
      })
      .catch(error => {
        alert("Something went wrong");
      });
    },
    // Your other methods
  }
};
</script>

<style scoped>

.buttonmain {
  display: block;
  width: 100%;
  padding: 10px;
  font-size: 18px;
  margin-top: 10px;
  border: 3px solid black; /* Add this line */
  margin-bottom: 20px; /* Add this line */
}

#searchBar {
  width: 100%;
  padding: 20px;
  font-size: 24px;
  border: 3px solid black;
}
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
  margin-bottom: 20px;
  border: 2px solid black;
}
th, td {
  padding: 0.5rem;
  border: 1px solid #000;
}
/* setup the spacing and the text alignment of the table headers and table cells */
.fetch :is(th, td) {
  text-align: left;
  padding: 0.25rem 0.75rem;
  min-width: 10rem;
}
/* make even numbered rows an off-white color to make the table more legible */
.fetch tr:nth-child(even) {
  background-color: #f9f9f9;
}

.buttonsec {
  display: inline-block; /* Change from block to inline-block */
  width: auto; /* Adjust as needed */
  padding: 5px; /* Adjust as needed */
  font-size: 18px;
  margin: 10px; /* Add some margin to separate the buttons */
  border: 3px solid black;
}
</style>