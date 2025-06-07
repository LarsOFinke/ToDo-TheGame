import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/views/Home-Page.vue";
import RegistrationPage from "@/views/Registration-Page.vue";
import TasksPage from "@/views/Tasks-Page.vue";
import ImpressumPage from "@/views/Impressum-Page.vue";
import TaskItemEdit from "@/components/Task-Item-Edit.vue";

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
    {
      path: "/impressum",
      name: "impressum",
      component: ImpressumPage,
    },
    {
      path: "/edit",
      name: "edit",
      component: TaskItemEdit,
    }
  ],
});

export default router;
