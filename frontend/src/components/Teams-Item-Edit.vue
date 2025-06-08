<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Edit team</h2>

        <!-- Message-Box -->
        <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

        <div>
            <h3 class="text-xl font-semibold text-gray-800 mb-2">My Teams</h3>
        </div>
        <div class="flex flex-col mb-4 justify-between">
            <label class="flex text-sm font-medium text-gray-700 justify-between mb-2">Team
                <input v-model.trim="teamName" type="text" placeholder="Team name" required
                    class="mt-1 block w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
            </label>

            <button type="button"
                class="bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 transition h-fit"
                @click.prevent="editTeamName">
                Edit team name
            </button>
        </div>
    </div>
</template>

<script setup>
import MessageBox from './shared/Message-Box.vue';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthService } from '@/services/AuthService'

const router = useRouter();
const { isAuthenticated } = useAuthService()
const msg = ref('')
const errorPhrase = 'Something went wrong!'
const teamName = ref('')

onMounted(async () => {
    if (!isAuthenticated.value) {
        router.replace('/');
    }
});

defineProps({
    selectedTeam: Object
})

const editTeamName = () => {
    console.log('Attempting to change team name...');
}
</script>