<template>
  <div class="flex flex-col min-h-screen bg-gray-300">
    <!-- Navbar -->
    <navbar-item></navbar-item>

    <!-- Main content -->
    <main class="flex-1 container mx-auto p-4 flex items-center justify-center min-h-[calc(100vh-10%)])">
      <router-view />
    </main>

    <!-- Footer -->
    <footer-item></footer-item>
  </div>
</template>


<script setup>
import NavbarItem from '@/components/shared/navbar/Navbar-Item.vue'
import FooterItem from '@/components/shared/Footer-Item.vue'
</script>