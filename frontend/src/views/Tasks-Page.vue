<template>
    <task-list v-if="viewTaskList" @hideTaskList="showTaskList" @updateTaskList="updateTasks"
        :taskList="taskList"></task-list>
    <task-form v-else @hideTaskList="showTaskList"></task-form>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import TaskList from '@/components/tasks/Task-List.vue'
import TaskForm from '@/components/tasks/Task-Form.vue';
import { useRouter } from 'vue-router';
import { useAuthService } from "@/services/AuthService"
import { useTasksService } from '@/services/TasksService';

const router = useRouter();
const { isAuthenticated, userId } = useAuthService()
const { getAllTasks, tasks } = useTasksService()
const viewTaskList = ref(true)
const taskList = ref([])

onMounted(async () => {
    if (!isAuthenticated.value) {
        router.replace('/');
    } else {
        await fetchTasks()
    }
});

const fetchTasks = async () => {
    await getAllTasks('user', 1)
    taskList.value = tasks.value
}

const updateTasks = async () => {
    await getAllTasks('user', userId)
    taskList.value = tasks.value
}

const showTaskList = async (hideTaskList) => {
    if (hideTaskList) {
        await fetchTasks()
        viewTaskList.value = false
    } else {
        await fetchTasks()
        viewTaskList.value = true
    }
}
</script>