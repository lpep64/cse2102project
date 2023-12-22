<template>
  <div id="app-wrapper">
    <AppHeader v-if="!isLoginPage" title="Class Enrollment" />
    <RouterView />
    <AppFooter v-if="!isLoginPage" title="Class Enrollment" />
  </div>
</template>

<script setup>
import { RouterView, useRoute } from "vue-router";
import { computed } from 'vue';
import AppHeader from "./components/AppHeader.vue";
import AppFooter from "./components/AppFooter.vue";


const route = useRoute();

// Determine if the current page is the login page
const isLoginPage = computed(() => route.path === '/login');
</script>