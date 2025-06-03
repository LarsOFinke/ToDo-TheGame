<template>
  <div class="flex flex-col min-h-screen">
    <!-- Navbar -->
    <nav class="bg-gray-800 text-white p-4">
      <div class="container mx-auto">
        <h1 class="text-xl">My App</h1>
      </div>
    </nav>

    <!-- Main content -->
    <main class="flex-1 container mx-auto p-4">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white p-4">
      <div class="container mx-auto text-center">
        © 2025 My App
      </div>
    </footer>
  </div>
</template>

<script setup>
// no script logic needed for layout
</script>