<template>
    <teams-list></teams-list>
</template>

<script setup>
import TeamsList from '@/components/teams/Teams-List.vue'
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthService } from '@/services/AuthService'

const router = useRouter();
const { isAuthenticated } = useAuthService()

onMounted(async () => {
    if (!isAuthenticated.value) {
        router.replace('/');
    }
});
</script>