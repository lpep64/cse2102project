import "./assets/main.css";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";  // Import the store

const app = createApp(App);

app.use(router);
app.use(store);  // Tell Vue to use the store

app.mount("#app");
