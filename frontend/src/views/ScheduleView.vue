<template>
  <div class="schedule">
    <h2>Schedule</h2>
    <p v-if="profile">{{ profile && profile.username }}'s Schedule</p>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th></th>
            <th v-for="day in days" :key="day">{{ day }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="time in times" :key="time">
            <td>{{ time }}</td>
            <td v-for="(day, index) in days" :key="day" :class="{ 'sunday-fix': index === 6 }">
              <span>{{ schedule[day][time] }}</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'ScheduleView',
  data() {
    return {
      days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
      times: ['8:00am', '9:00am', '10:00am', '11:00am', '12:00pm', '1:00pm', '2:00pm', '3:00pm', '4:00pm', '5:00pm', '6:00pm'],
      schedule: {
        Monday: {},
        Tuesday: {},
        Wednesday: {},
        Thursday: {},
        Friday: {},
        Saturday: {},
        Sunday: {},
      },
    };
  },
  computed: {
    ...mapState(['profile']),
  },
  mounted() {
  function convertDynamoDBData(data) {
    return Object.entries(data).reduce((obj, [key, value]) => {
      const dataType = Object.keys(value)[0];
      obj[key] = value[dataType];
      return obj;
    }, {});
  }

  for(let course in this.profile.courses){
    const uri = 'https://8ip466ik32.execute-api.us-east-1.amazonaws.com/API';
  
    const headers = {
      'Content-Type': 'application/json',
      'x-amz-docs-region': 'us-east-1'
    };
    

    const propername = this.profile.courses[course].substring(0, this.profile.courses[course].indexOf("."));
    const sec = (this.profile.courses[course].split('.')[1]) - 1;

    const para = {
    "operation": "query_course",
    "name": propername
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
      const items = data.Items.map(convertDynamoDBData);

      const daysetup = (items[0].secdatetime[sec]).substring(2);
      const dayclass = daysetup.split(",");
      for (course in dayclass){
        const firstChar = dayclass[course][0];
        const secondChar = dayclass[course][1];

        let day = '';
        if(firstChar == 'M'){
          day = "Monday"
        } else if(firstChar == 'W'){
          day = "Wednesday"
        } else if(firstChar == 'F'){
          day = "Friday"
        } else if(firstChar == 'T'){
          if(secondChar == 'h'){
            day = "Thursday"
          } else if(secondChar == 'u'){
            day = "Tuesday"
          }
        } else if(secondChar == 'u'){
          day = "Sunday"
        } else {
          day = "Saturday"
        }

        const fulltime = dayclass[course].split('@')[1]
        let starttime = parseInt(fulltime.split(':')[0]);
        let endtime = parseInt(fulltime.split(':')[1]) + 1;
        let end;
        if (starttime == 8 || starttime == 9 || starttime == 10 || starttime == 11){
          end = ":00am";
        } else {
          end = ":00pm";
        }

        while(starttime != endtime){
          if(this.schedule[day][starttime.toString() + end]) {
            alert("Schedule Conflict at " + day + " " + starttime.toString() + end + " for " + propername);
            this.schedule[day][starttime.toString() + end] = 'Conflict';
            break;
          }
          this.schedule[day][starttime.toString() + end] = propername;
          if(starttime == 11){
            end = ":00pm"
          }
          if(starttime == 12){
            starttime = 0;
          }
        starttime++;
        }
      }  
    })
    .catch(error => {
      alert("Something went wrong");
    });
  }
  },
};
</script>

<style scoped>
.schedule {
  padding: 1rem;
  text-align: center;
  overflow-x: auto;
}

.schedule h2 {
  font-size: 40px;
  margin-bottom: 1rem;
  color: #000E2F;
}

/* Styling for table cells */
.schedule .table-container {
  max-width: 100%;
}

.schedule table {
  border-collapse: collapse;
  width: 100%;
  table-layout: fixed;
}

.schedule table td, .schedule table th {
  border: 1px solid #000;
  padding: 8px;
  width: calc(100% / 8);
}

.sunday-fix {
  width: calc(100% / 8);
}
</style>