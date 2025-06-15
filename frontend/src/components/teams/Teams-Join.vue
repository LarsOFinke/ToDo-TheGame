<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <!-- List Header -->
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Join a Teams</h2>

        <!-- Utility-Buttons -->
        <div class="flex w-full justify-between mb-4">
            <button type="button"
                class="bg-yellow-600 text-white py-2 px-4 rounded-md hover:bg-yellow-800 transition h-fit mb-4"
                @click.prevent="newTeam">
                New team
            </button>

            <button type="button"
                class="bg-yellow-600 text-white py-2 px-4 rounded-md hover:bg-yellow-800 transition h-fit mb-4"
                @click.prevent="joinTeam">
                Join team
            </button>
        </div>

        <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto relative">
            <!-- Message-Box -->
            <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

            <!-- Scrollable Team List -->
            <div class="overflow-x-auto max-h-95">
                <ul v-for="team in teamList" :key="team.id" class="mb-8">
                    <teams-item :team="team" @hideTeamTasks="showTeamTasks"></teams-item>
                </ul>
            </div>
        </div>
    </div>
</template>


<script setup>
import MessageBox from '@/components/shared/Message-Box.vue';
import TeamsItem from '@/components/teams/Teams-Item.vue';
import { ref, onMounted } from 'vue'
import { useTeamsService } from '@/services/TeamsService';

const emit = defineEmits(['hideTeamList', 'updateTeamList', 'hideTeamTasks'])
const msg = ref('')
const errorPhrase = 'Something went wrong!'
const { teams, getAllTeams } = useTeamsService()
const teamList = ref([])

onMounted(async () => {
    await fetchTeams()
});

const fetchTeams = async () => {
    await getAllTeams()
    teamList.value = teams.value
}

const joinTeam = () => {

}
</script>