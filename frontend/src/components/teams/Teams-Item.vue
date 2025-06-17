<template>
    <div class="w-full max-w-sm bg-gray-200 rounded-lg shadow-md p-4 mx-auto relative">
        <!-- Teams-Header -->
        <div class="flex items-center justify-between w-full mb-2">
            <h3 class="text-xl font-bold text-gray-800 mb-2">{{ team.name }}</h3>
        </div>

        <!-- Teams-Info -->
        <teams-item-info v-if="viewTeamInfo" :team="team" :memberCount="memberCount"></teams-item-info>

        <!-- Teams-Details -->
        <teams-item-details v-else></teams-item-details>

        <!-- Utility-Buttons -->
        <div v-if="viewTeamInfo" class="mb-2 absolute top-2 right-2">
            <button type="button" @click.prevent="showTeamDetails"
                class="w-fit bg-indigo-600 text-white py-1 px-4 rounded-md hover:bg-indigo-800 transition">Details</button>
        </div>
        <div v-else class="mb-2 absolute top-2 right-2">
            <button type="button" @click.prevent="showTeamInfo"
                class="w-fit bg-indigo-600 text-white py-1 px-4 rounded-md hover:bg-indigo-800 transition">Info</button>
        </div>
        <div v-if="mode === 'teams-list'" class="w-full flex justify-around">
            <button type="button" @click.prevent="showTeamTasks"
                class="w-fit bg-indigo-600 text-white py-1 px-2 rounded-md hover:bg-indigo-800 transition">Team-Tasks</button>
        </div>
        <div v-else class="w-full flex justify-around">
            <button type="button" @click.prevent="joinTeam"
                class="w-fit bg-emerald-600 text-white py-1 px-2 rounded-md hover:bg-emerald-800 transition">Join-Team</button>
        </div>
    </div>
</template>

<script setup>
import TeamsItemInfo from '@/components/teams/Teams-Item-Info.vue'
import TeamsItemDetails from '@/components/teams/Teams-Item-Details.vue'
import { ref, onMounted } from 'vue'
import { useMembersService } from '@/services/MembersService'
import { useAuthService } from '@/services/AuthService'

const props = defineProps({
    team: Object,
    mode: String
})
const emit = defineEmits(['hideTeamTasks', 'updateTeamList'])
const { userId } = useAuthService()
const { fetchMemberCountForTeam, addNewMember } = useMembersService()
const memberCount = ref(0)
const viewTeamInfo = ref(true)

onMounted(async () => {
    memberCount.value = await fetchMemberCountForTeam(props.team.id)
});

const showTeamDetails = () => {
    viewTeamInfo.value = false
}

const showTeamInfo = () => { viewTeamInfo.value = true }

const showTeamTasks = () => {
    emit('hideTeamTasks', [false, props.team.id])
}

const joinTeam = async () => {
    if (await addNewMember({
        teamName: props.team.name,
        userId: userId.value,
        teamId: props.team.id
    })) {
        emit('updateTeamList')
    }
}
</script>