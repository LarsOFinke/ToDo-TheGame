<template>
    <teams-list v-if="showTeamsList" :teamList="teamList"></teams-list>
</template>

<script setup>
import TeamsList from '@/components/Teams-List.vue'
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthService } from '@/services/AuthService'

const router = useRouter();
const { isAuthenticated } = useAuthService()
const showTeamsList = ref(true)

onMounted(async () => {
    if (!isAuthenticated.value) {
        router.replace('/');
    }
});

const teamList = ref([{id: 1}, {id: 2}])

</script>