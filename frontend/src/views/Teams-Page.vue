<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Teams</h2>

        <teams-list v-if="showTeamsList"></teams-list>
    </div>
</template>

<script setup>
import TeamsList from '@/components/Teams-List.vue'
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthService } from '@/services/AuthService'

const router = useRouter();
const { user, isAuthenticated } = useAuthService()
const showTeamsList = ref(true)

// onMounted(async () => {
//     if (!isAuthenticated.value) {
//         router.replace('/');
//     }
// });

</script>