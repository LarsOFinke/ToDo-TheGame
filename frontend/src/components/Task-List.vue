<template>
    <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Task-List</h2>
        <ul>
            <task-item></task-item>
        </ul>
    </div>
</template>

<script setup>
import TaskItem from './Task-Item.vue';
</script>