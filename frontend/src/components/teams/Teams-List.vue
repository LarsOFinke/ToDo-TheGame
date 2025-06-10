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
                Join team
            </button>
        </div>

        <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto relative">
            <!-- Message-Box -->
            <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

            <!-- Scrollable Team List -->
            <div class="overflow-x-auto max-h-95">
                <ul v-for="team in teamList" :key="team.id" class="mb-8">
                    <teams-item :team="team" @hideTeamList="showTeamList"></teams-item>
                </ul>
            </div>
        </div>
    </div>

    <teams-item-edit v-else-if="!viewTeamList && !viewTeamForm" :team="selectedTeam"
        @hideTeamList="showTeamList"></teams-item-edit>
    <teams-form v-else @hideTeamForm="showTeamForm"></teams-form>

</template>


<script setup>
import MessageBox from '@/components/shared/Message-Box.vue';
import TeamsForm from '@/components/teams/Teams-Form.vue'
import TeamsItem from '@/components/teams/Teams-Item.vue';
import TeamsItemEdit from '@/components/teams/Teams-Item-Edit.vue';
import { ref } from 'vue'

const emit = defineEmits(['hideTeamList', 'updateTeamList'])
const msg = ref('')
const errorPhrase = 'Something went wrong!'
const selectedTeam = ref(Object)
const viewTeamList = ref(true)
const viewTeamForm = ref(false)

defineProps({
    teamList: Array
})

const newTeam = () => {
    showTeamForm(true)
}

const joinTeam = () => {

}

const showTeamForm = (hideTeamForm) => {
    if (hideTeamForm) {
        viewTeamForm.value = true
        viewTeamList.value = false
    } else {
        emit('updateTeamList', true)
        viewTeamForm.value = false
        viewTeamList.value = true
    }
}

const showTeamList = (hideTeamList) => {
    if (hideTeamList[0]) {
        viewTeamList.value = false
    } else {
        selectedTeam.value = hideTeamList[1]
        viewTeamList.value = true
    }
}

const showMessage = (message) => {
    msg.value = message
}
</script>