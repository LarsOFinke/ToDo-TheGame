<template>
    <task-list :class="showTaskList ? '' : 'hidden'" @hideTaskList="toggleViews"></task-list>
    <task-form :class="showTaskList ? 'hidden' : ''" @hideTaskList="toggleViews"></task-form>
</template>

<script setup>
import { ref } from 'vue';
import TaskList from '@/components/Task-List.vue'
import TaskForm from '@/components/Task-Form.vue';

const showTaskList = ref(true)

const toggleViews = (hideTaskList) => {
    if (hideTaskList) {
        showTaskList.value = false
    } else {
        showTaskList.value = true
    }
}
</script>