import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/views/Home-Page.vue";
import RegistrationPage from "@/views/Registration-Page.vue";
import TasksPage from "@/views/Tasks-Page.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomePage,
    },
    {
      path: "/registration",
      name: "registration",
      component: RegistrationPage,
    },
    {
      path: "/tasks",
      name: "tasks",
      component: TasksPage,
    },
  ],
});

export default router;
