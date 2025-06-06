<template>
  <nav class="flex bg-gray-800 text-white p-2">
    <div class="container mx-auto">
      <h1 class="text-xl">PageHeader</h1>
    </div>

    <div class="flex float-right">
      <ul class="flex">
        <li :class="isAuthenticated ? 'hidden' : 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline'"><a href="/">Home</a></li>
        <li :class="isAuthenticated ? 'hidden' : 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline'"><a href="/registration">Registration</a></li>
        <li :class="isAuthenticated ? 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline' : 'hidden'"><a href="/tasks">Tasks</a></li>
        <li :class="isAuthenticated ? 'mr-4 font-medium dark:text-yellow-300 hover:text-yellow-400 hover:underline' : 'hidden'"><a href="/">Logout</a></li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useAuthService } from "@/services/AuthService"

const router = useRouter();
const { isAuthenticated } = useAuthService()


</script>
