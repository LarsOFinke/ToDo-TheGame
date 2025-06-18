<template>
  <nav class="flex bg-gray-800 text-white p-2">
    <div class="container mx-auto">
      <h1 class="text-xl">{{ pageHeaders[route.name] }}</h1>
    </div>

    <div class="flex float-right">
      <ul class="flex">
        <!-- VISIBLE WHEN NOT AUTHENTICATED -->
        <li
          :class="isAuthenticated ? 'hidden' : 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline cursor-pointer'">
          <a @click.prevent="home">Home</a>
        </li>
        <li
          :class="isAuthenticated ? 'hidden' : 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline cursor-pointer'">
          <a @click.prevent="registration">Registration</a>
        </li>

        <!-- VISIBLE WHEN AUTHENTICATED -->
        <li
          :class="isAuthenticated ? 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline cursor-pointer' : 'hidden'">
          <a @click.prevent="tasks">Tasks</a>
        </li>
        <li
          :class="isAuthenticated ? 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline cursor-pointer' : 'hidden'">
          <a @click.prevent="teams">Teams</a>
        </li>
        <li
          :class="isAuthenticated ? 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline cursor-pointer' : 'hidden'">
          <a @click.prevent="profile">Profile</a>
        </li>
        <li
          :class="isAuthenticated ? 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline cursor-pointer' : 'hidden'">
          <a @click.prevent="logout">Logout</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router';
import { useAuthService } from "@/services/AuthService"

const router = useRouter();
const route = useRoute()
const { userId, isAuthenticated, clearSession } = useAuthService()
const pageHeaders = {
  "Home": "Login",
  "Registration": "Registration",
  "Tasks": "My Tasks",
  "Teams": "Teams",
  "Profile": "My Profile",
  "Impressum": "Impressum",
}

const home = () => {
  router.replace("/")
}

const registration = () => {
  router.replace("/registration")
}

const profile = () => {
  router.replace("/profile")
}

const teams = () => {
  router.replace("/teams")
}

const tasks = () => {
  router.replace({
    name: 'Tasks',
    query: { mode: 'user', modeId: userId.value }
  });
}

const logout = () => {
  clearSession()
  router.replace("/")
}
</script>
