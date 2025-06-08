<template>
  <nav class="flex bg-gray-800 text-white p-2">
    <div class="container mx-auto">
      <h1 class="text-xl">PageHeader</h1>
    </div>

    <div class="flex float-right">
      <ul class="flex">
        <li
          :class="isAuthenticated ? 'hidden' : 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline cursor-pointer'">
          <a @click.prevent="home">Home</a>
        </li>
        <li
          :class="isAuthenticated ? 'hidden' : 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline cursor-pointer'">
          <a @click.prevent="registration">Registration</a>
        </li>
        <li
          :class="isAuthenticated ? 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline cursor-pointer' : 'hidden'">
          <a @click.prevent="profile">Profile</a>
        </li>
        <li
          :class="isAuthenticated ? 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline cursor-pointer' : 'hidden'">
          <a @click.prevent="tasks">Tasks</a>
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
import { useRouter } from 'vue-router';
import { useAuthService } from "@/services/AuthService"

const router = useRouter();
const { isAuthenticated, clearSession } = useAuthService()

const home = () => {
  router.replace("/")
}

const registration = () => {
  router.replace("/registration")
}

const profile = () => {
  router.replace("/profile")
}

const tasks = () => {
  clearSession()
  router.replace("/tasks")
}

const logout = () => {
  clearSession()
  router.replace("/")
}
</script>
