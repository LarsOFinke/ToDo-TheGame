<template>
    <task-list :mode="'user'" :modeId="userId"></task-list>
</template>

<script setup>
import TaskList from '@/components/tasks/Task-List.vue'
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthService } from "@/services/AuthService"

const router = useRouter();
const { isAuthenticated, userId } = useAuthService()

onMounted(async () => {
    if (!isAuthenticated.value) {
        router.replace('/');
    }
});

</script>