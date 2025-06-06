<template>
    <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto relative">
        <h2 class="text-2xl font-bold text-gray-800 mb-4 text-center">Task-List</h2>

        <!-- Utility-Buttons -->
        <div class="flex justify-center mb-4">
            <button type="button" @click.prevent="showTaskForm"
                class="text-l w-fit bg-yellow-600 text-white px-2 py-1 mb-1 rounded-md hover:bg-yellow-800 transition">
                New task
            </button>
        </div>

        <!-- Scrollable Task List -->
        <div class="overflow-x-auto max-h-95">
            <scrollbar-hide>
                <ul v-for="task in taskList" :key="task.id" class="mb-8">
                    <task-item :task="task"></task-item>
                </ul>
            </scrollbar-hide>
        </div>
    </div>
</template>


<script setup>
import TaskItem from './Task-Item.vue';

const emit = defineEmits(['hideTaskList'])

defineProps({
    taskList: Array
})

const showTaskForm = () => {
    emit('hideTaskList', true)
}
</script>