<template>
    <task-list :class="showTaskList ? '' : 'hidden'" @hideTaskList="toggleViews" :taskList="taskList"></task-list>
    <task-form :class="showTaskList ? 'hidden' : ''" @hideTaskList="toggleViews" @addTask="addNewTask"></task-form>
</template>

<script setup>
import { ref } from 'vue';
import TaskList from '@/components/Task-List.vue'
import TaskForm from '@/components/Task-Form.vue';

const showTaskList = ref(true)

const taskList = ref([
    {
        id: 1,
        title: "Task-Title",
        mode: "Private / Team",
        priority: "high",
        deadlineDate: "06.06.2025",
        remainingTime: "2d 4h 24min 12s",   // Needs to get calculated in the Task-Item asynchronously?
        description: `Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime suscipit, et fugiat
                    ipsam, tempora animi
                    laborum.`
    },
    {
        id: 2,
        title: "Task-Title",
        mode: "Private / Team",
        priority: "low",
        deadlineDate: "06.06.2025",
        remainingTime: "2d 4h 24min 12s",   // Needs to get calculated in the Task-Item asynchronously?
        description: `Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime suscipit, et fugiat
                    ipsam, tempora animi
                    laborum laboriosam natus asperiores aspernatur itaque cupiditate voluptatum accusamus iure officiis
                    quisquam obcaecati culpa error?`
    },
    {
        id: 3,
        title: "Task-Title",
        mode: "Private / Team",
        priority: "low",
        deadlineDate: "06.06.2025",
        remainingTime: "2d 4h 24min 12s",   // Needs to get calculated in the Task-Item asynchronously?
        description: `Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime suscipit, et fugiat
                    ipsam, tempora animi
                    laborum laboriosam natus asperiores aspernatur itaque cupiditate voluptatum accusamus iure officiis
                    quisquam obcaecati culpa error?Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime suscipit, et fugiat
                    ipsam, tempora animi
                    laborum laboriosam natus asperiores aspernatur itaque cupiditate voluptatum accusamus iure officiis
                    quisquam obcaecati culpa error?`
    },
])

const toggleViews = (hideTaskList) => {
    if (hideTaskList) {
        showTaskList.value = false
    } else {
        showTaskList.value = true
    }
}

const addNewTask = (newTask) => {
    taskList.value.push(newTask)
}
</script>