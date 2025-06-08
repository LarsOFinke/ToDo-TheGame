import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/views/Home-Page.vue";
import RegistrationPage from "@/views/Registration-Page.vue";
import TasksPage from "@/views/Tasks-Page.vue";
import ImpressumPage from "@/views/Impressum-Page.vue";
import ProfilePage from "@/views/Profile-Page.vue";
import TeamsPage from "@/views/Teams-Page.vue";


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
      path: "/profile",
      name: "profile",
      component: ProfilePage,
    },
    {
      path: "/teams",
      name: "teams",
      component: TeamsPage,
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
  ],
});

export default router;
