<template>
    <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-bold text-gray-800 mb-4 text-center">Task-List</h2>



        <ul v-for="task in taskList" :key="task.id" class="relative m-4">
            <!-- Utility-Buttons -->
            <div class="mb-2 absolute top-2 right-[calc(31.5%)]">
                <button type="button" @click.prevent="showTaskForm"
                    class="text-l w-fit bg-yellow-600 text-white px-2 rounded-md hover:bg-yellow-800 transition">
                    Add new task
                </button>
            </div>

            <br> <br>
            <task-item :task="task"></task-item>
        </ul>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import TaskItem from './Task-Item.vue';

const emit = defineEmits(['hideTaskList'])

const taskList = ref([
    {
        id: 1,
        title: "Task-Title",
        mode: "Private / Team",
        priority: "Priority",
        deadlineDate: "06.06.2025",
        remainingTime: "2d 4h 24min 12s",   // Needs to get calculated in the Task-Item asynchronously?
        description: `Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime suscipit, et fugiat
                    ipsam, tempora animi
                    laborum laboriosam natus asperiores aspernatur itaque cupiditate voluptatum accusamus iure officiis
                    quisquam obcaecati culpa error?`
    },
])

const showTaskForm = () => {
    emit('hideTaskList', true)
}
</script>