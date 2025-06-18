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
      name: "Home",
      component: HomePage,
    },
    {
      path: "/registration",
      name: "Registration",
      component: RegistrationPage,
    },
    {
      path: "/tasks",
      name: "Tasks",
      component: TasksPage,
    },
    {
      path: "/teams",
      name: "Teams",
      component: TeamsPage,
    },
    {
      path: "/profile",
      name: "Profile",
      component: ProfilePage,
    },
    {
      path: "/impressum",
      name: "Impressum",
      component: ImpressumPage,
    },
  ],
});

export default router;
