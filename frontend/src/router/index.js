import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SearchView from "../views/SearchView.vue";
import ScheduleView from "../views/ScheduleView.vue";
import ProfileView from "../views/ProfileView.vue";
import LoginView from "../views/LoginView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "Login",
      component: LoginView,
    },
    {
      path: "/",
      redirect: "/login", // Redirect to the login page by default
    },
    {
      path: "/Husky37",
      name: "Husky37",
      component: () => import('../views/HomeView.vue'),
    },

    {
      path: "/search",
      name: "Search",
      component: SearchView,
    },

    {
      path: "/Schedule",
      name: "Schedule",
      component: ScheduleView,
    },

    {
      path: "/Profile",
      name: "Profile",
      component: ProfileView,
    },

  ],
});

router.beforeEach((to, from, next) => {
  document.title = to.name
  next()
})

export default router;