<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <!-- List Header -->
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Join a Team</h2>

        <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto relative">
            <!-- Message-Box -->
            <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

            <!-- Scrollable Team List -->
            <div class="overflow-x-auto max-h-95">
                <ul v-if="teamList[0]" v-for="team in teamList" :key="team.id" class="mb-8">
                    <teams-item :team="team" :mode="'teams-join'" @hideTeamTasks="" @updateTeamList="fetchTeams"></teams-item>
                </ul>
                <h2 v-else>No Teams joinable.</h2>
            </div>
        </div>

        <!-- Utility-Buttons -->
        <div class="flex w-full justify-between mt-4">
            <button type="button" @click.prevent="hideTeamJoin"
                class="w-fit bg-red-700 text-white py-1 px-4 rounded-md hover:bg-red-800 transition">Back</button>
        </div>
    </div>
</template>


<script setup>
import MessageBox from '@/components/shared/Message-Box.vue';
import TeamsItem from '@/components/teams/Teams-Item.vue';
import { ref, onMounted } from 'vue'
import { useAuthService } from '@/services/AuthService';
import { useTeamsService } from '@/services/TeamsService';

const emit = defineEmits(['hideTeamJoin',])
const msg = ref('')
const errorPhrase = 'Something went wrong!'
const { teams, getAllTeamsNotJoined } = useTeamsService()
const { userId } = useAuthService()
const teamList = ref([])

onMounted(async () => {
    await fetchTeams()
});

const fetchTeams = async () => {
    await getAllTeamsNotJoined(userId.value)
    teamList.value = teams.value
}

const hideTeamJoin = () => {
    emit('hideTeamJoin', false)
}
</script>