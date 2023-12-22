<template>
  <header class="site-header">
    <span class="header-logo" style="font-size: 3rem; font-family: 'Arial', sans-serif;">Husky37</span>
    <nav class="nav">
      <RouterLink to="/Husky37" class="nav-link">
        <div class="nav-item">
          <img src="../assets/home-icon.png" alt="Home" class="nav-icon" />
          <span>Home</span>
        </div>
      </RouterLink>
      <RouterLink to="/search" class="nav-link">
        <div class="nav-item">
          <img src="../assets/classes-icon.png" alt="Classes" class="nav-icon" />
          <span>Classes</span>
        </div>
      </RouterLink>
      <RouterLink to="/Schedule" class="nav-link">
        <div class="nav-item">
          <img src="../assets/schedule-icon.png" alt="Schedule" class="nav-icon" />
          <span>Schedule</span>
        </div>
      </RouterLink>
      <RouterLink to="/Profile" class="nav-link">
        <div class="nav-item">
          <img src="../assets/profile-icon.png" alt="Profile" class="nav-icon" />
          <span>Profile</span>
        </div>
      </RouterLink>
      <RouterLink to="/login" class="nav-link">
        <div class="nav-item">
          <img src="../assets/logout-icon.png" alt="Logout" class="nav-icon" />
          <span>Logout</span>
        </div>
      </RouterLink>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style scoped>
/* Reset default margins and paddings */
body, html {
  margin: 0;
  padding: 0;
}

/* Wrapper styles to center content */
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Header styles */
.site-header {
  background-color: #000E2F;
  color: #fff;
  padding: 10px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.header-title {
  font-size: 2.5rem;
  color: #fff;
  font-weight: bold;
  margin-bottom: 10px; /* Adjust spacing between title and links */
}

/* Navigation styles */
.nav {
  display: flex;
  justify-content: center;
  color: black; /* Change text color */
}

/* Styling for each link container */
.nav-link {
  text-decoration: none;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px 80px; /* Increase space between link items */
}

.nav-icon {
  width: 30px; /* Set width and height for icons */
  height: 30px;
  margin-bottom: 5px; /* Adjust space between icon and text */
}

.nav-item span {
  color: #fff; /* Change text color */
  font-size: 16px;
}

/* Hover effect for navigation links */
.nav-link:hover .nav-item {
  background-color: #5c5c5c;
  border-radius: 5px;
  color: #000E2F;
}
</style>