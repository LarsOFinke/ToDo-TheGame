<template>
    <div>
        <div v-if="!viewItemEdit" class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto relative">
            <h2 class="text-2xl font-bold text-gray-800 mb-4 text-center">Task-List</h2>

            <!-- Message-Box -->
            <div v-if="msg !== ''"
                :class="msg === 'Something went wrong!' ? 'w-fit max-w-sm bg-gray-100 text-red-600 font-semibold rounded-lg shadow-md p-1 mx-auto' : 'w-fit max-w-sm bg-gray-100 text-gray-800 font-semibold rounded-lg shadow-md p-1 mx-auto'">
                <p>{{ msg }}</p>
            </div>

            <!-- Utility-Buttons -->
            <div class="flex justify-center mb-4">
                <button type="button" @click.prevent="showTaskForm"
                    class="text-l w-fit bg-yellow-600 text-white px-2 py-1 mb-1 rounded-md hover:bg-yellow-800 transition">
                    New task
                </button>
            </div>

            <!-- Scrollable Task List -->
            <div class="overflow-x-auto max-h-95">
                <ul v-for="task in taskList" :key="task.id" class="mb-8">
                    <task-item :task="task" @hideItemEdit="showItemEdit" @updateTaskList="updateList"
                        @closeItem="showMessage"></task-item>
                </ul>
            </div>
        </div>

        <task-item-edit v-else :task="selectedTask" @hideItemEdit="showItemEdit"></task-item-edit>
    </div>
</template>


<script setup>
import { ref } from 'vue'
import TaskItem from './Task-Item.vue';
import TaskItemEdit from './Task-Item-Edit.vue';

const msg = ref('')
const emit = defineEmits(['hideTaskList', 'updateTaskList'])
const viewItemEdit = ref(false);
const selectedTask = ref('')

defineProps({
    taskList: Array
})

const showTaskForm = () => {
    emit('hideTaskList', true)
}

const updateList = () => {
    emit('updateTaskList', true)
}

const showItemEdit = (hideItemEdit) => {
    if (hideItemEdit[0]) {
        viewItemEdit.value = false
    } else {
        selectedTask.value = hideItemEdit[1]
        viewItemEdit.value = true
    }
}

const showMessage = (message) => {
    console.log(message);
    msg.value = message
}
</script>