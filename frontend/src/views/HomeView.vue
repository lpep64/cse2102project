<template>
  <main class="home">
    <h2 style="font-size: 32px; font-family: Arial, sans-serif;">Hello Students!</h2>
    <p><br><br>Welcome to the new student admin. Here you will be able to register for classes.
      </p>
      <p>Feel free to explore the different features and functionalities of the student admin.</p>
  </main>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

function handleSubmit() {
  router.push('/Husky37');
}
</script>

<style scoped>
.home {
  height: 100vh; /* Cover the full viewport height */
  background-image: url('../assets/UConnHome.png');
  background-size: 100% 70%;
  background-position: center top;
  background-repeat: no-repeat;
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
}

.home {
  padding: 1rem;
  text-align: center;
}

.home h2 {
  font-size: 26px;
  font-weight: bold;
  margin-bottom: 30rem;
  color: #090334;
}

.home p {
  font-size: 24px;
  color: #090334;
}

.home gray-box {
  position: absolute;
  bottom: 20;
  left: 0;
  width: 100%;
  height: 220px; 
  background-color: #000E2F; 
}
</style>
