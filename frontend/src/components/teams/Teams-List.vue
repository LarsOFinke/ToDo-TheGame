<template>
    <div v-if="viewTeamList" class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <!-- List Header -->
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">My Teams</h2>

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
                Join a team
            </button>
        </div>

        <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto relative">
            <!-- Message-Box -->
            <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

            <!-- Scrollable Team List -->
            <div class="overflow-x-auto max-h-95">
                <ul v-for="team in teamList" :key="team.id" class="mb-8">
                    <teams-item :team="team" :mode="'teams-list'" @hideTeamTasks="showTeamTasks" @updateTeamList="fetchTeams"></teams-item>
                </ul>
            </div>
        </div>
    </div>

    <teams-form v-else-if="viewTeamForm" @hideTeamForm="showTeamForm"></teams-form>

    <teams-join v-else-if="viewTeamJoin"></teams-join>

    <task-list v-else :mode="'team'" :modeId="selectedTeamId" @hideTeamTasks="showTeamTasks"></task-list>
</template>


<script setup>
import MessageBox from '@/components/shared/Message-Box.vue';
import TeamsForm from '@/components/teams/Teams-Form.vue'
import TeamsItem from '@/components/teams/Teams-Item.vue';
import TeamsJoin from '@/components/teams/Teams-Join.vue';
import TaskList from '@/components/tasks/Task-List.vue';
import { ref, onMounted } from 'vue'
import { useAuthService } from '@/services/AuthService';
import { useTeamsService } from '@/services/TeamsService';

const emit = defineEmits(['hideTeamList', 'updateTeamList', 'hideTeamTasks'])
const msg = ref('')
const errorPhrase = 'Something went wrong!'
const { userId } = useAuthService()
const { teams, getTeamsForUser } = useTeamsService()
const viewTeamList = ref(true)
const viewTeamForm = ref(false)
const viewTeamJoin = ref(false)
const teamList = ref([])
const selectedTeamId = ref(0)

onMounted(async () => {
    await fetchTeams()
});

const fetchTeams = async () => {
    await getTeamsForUser(userId.value)
    teamList.value = teams.value
}

const newTeam = () => {
    showTeamForm(true)
}

const joinTeam = () => {
    showTeamJoin(true)
}

const showTeamForm = async (hideTeamForm) => {
    if (hideTeamForm) {
        viewTeamForm.value = true
        viewTeamList.value = false
    } else {
        await fetchTeams()
        viewTeamForm.value = false
        viewTeamList.value = true
    }
}

const showTeamJoin = async (hideTeamList) => {
    if (hideTeamList) {
        viewTeamJoin.value = true
        viewTeamList.value = false
    } else {
        await fetchTeams()
        viewTeamList.value = true
    }
}

const showTeamTasks = (hideTeamTasks) => {
    if (hideTeamTasks[0]) {
        selectedTeamId.value = hideTeamTasks[1]
        viewTeamList.value = true
    } else {
        selectedTeamId.value = hideTeamTasks[1]
        viewTeamList.value = false
    }
}
</script>