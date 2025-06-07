<template>
    <task-list v-if="viewTaskList" @hideTaskList="showTaskList" :taskList="taskList"></task-list>
    <task-form v-else @hideTaskList="showTaskList" @addTask="addNewTask"></task-form>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import TaskList from '@/components/Task-List.vue'
import TaskForm from '@/components/Task-Form.vue';
import { useRouter } from 'vue-router';
import { useAuthService } from "@/services/AuthService"
import { useTasksService } from '@/services/TasksService';

const router = useRouter();
const { isAuthenticated } = useAuthService()
const { getAllTasks, tasks } = useTasksService()
const viewTaskList = ref(true)
const taskList = ref([])

onMounted(async () => {
    if (!isAuthenticated.value) {
        router.replace('/');
    } else {
        await fetchTasks()
        console.log(tasks);
        taskList.value = tasks.value

    }
});

const fetchTasks = async () => { await getAllTasks() }

const showTaskList = (hideTaskList) => {
    if (hideTaskList) {
        viewTaskList.value = false
    } else {
        viewTaskList.value = true
    }
}

const addNewTask = (newTask) => {
    taskList.value.push(newTask)
}

</script>