<template>
    <div>
        <div :class="viewItemEdit ? 'hidden' : 'w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto relative'">
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
                <ul v-for="task in taskList" :key="task.id" class="mb-8">
                    <task-item :task="task" @hideItemEdit="showItemEdit"></task-item>
                </ul>
            </div>
        </div>

        <task-item-edit :class="viewItemEdit ? '' : 'hidden'" @hideItemEdit="showItemEdit"></task-item-edit>
    </div>
</template>


<script setup>
import TaskItem from './Task-Item.vue';
import TaskItemEdit from './Task-Item-Edit.vue';
import { ref } from 'vue'

const emit = defineEmits(['hideTaskList'])
const viewItemEdit = ref(false);

defineProps({
    taskList: Array
})

const showTaskForm = () => {
    emit('hideTaskList', true)
}

const showItemEdit = (hideItemEdit) => {
    if (hideItemEdit) {
        viewItemEdit.value = false
    } else {
        viewItemEdit.value = true
    }
}

</script>