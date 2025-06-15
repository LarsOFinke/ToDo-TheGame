<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <!-- List Header -->
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Join a Team</h2>

        <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto relative">
            <!-- Message-Box -->
            <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

            <!-- Scrollable Team List -->
            <div class="overflow-x-auto max-h-95">
                <ul v-for="team in teamList" :key="team.id" class="mb-8">
                    <teams-item :team="team" :mode="'teams-join'" @hideTeamTasks=""></teams-item>
                </ul>
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
import { useTeamsService } from '@/services/TeamsService';

const emit = defineEmits(['hideTeamJoin', 'hideTeamTasks'])
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

const showTeamTasks = (hideTeamTasks) => {
    // NEEDS TO GET REFACTORED TO SEND A SIGNAL TO TEAMS-LIST TO MAAGE VISIBILITY //
    if (hideTeamTasks[0]) {
        selectedTeamId.value = hideTeamTasks[1]
        // viewTeamList.value = true
    } else {
        selectedTeamId.value = hideTeamTasks[1]
        // viewTeamList.value = false
    }
}

const hideTeamJoin = () => {

}
</script>