<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <!-- List Header -->
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">My Teams</h2>

        <div class="flex mb-4">
                <button type="button"
                    class="bg-yellow-600 text-white py-2 px-4 rounded-md hover:bg-yellow-800 transition h-fit mb-4 mx-auto"
                    @click.prevent="foundNewTeam">
                    Found a new team
                </button>
            </div>

        <div v-if="!viewTeamEdit" class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto relative">
            <!-- Message-Box -->
            <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

            <!-- Scrollable Team List -->
            <div class="overflow-x-auto max-h-95">
                <ul v-for="team in teamList" :key="task.id" class="mb-8">
                    <teams-item :task="task" @hideTeamEdit="showTeamEdit" @updateTeamList="updateList"
                        @closeItem="showMessage"></teams-item>
                </ul>
            </div>
        </div>

        <teams-item-edit v-else :team="selectedTeam" @hideItemEdit="showTeamEdit"></teams-item-edit>
    </div>
</template>


<script setup>
import { ref } from 'vue'
import TeamsItem from './Teams-Item.vue';
import TeamsItemEdit from './Teams-Item-Edit.vue';
import MessageBox from './shared/Message-Box.vue';

const msg = ref('')
const errorPhrase = 'Something went wrong!'
const emit = defineEmits(['hideTeamList', 'updateTeamList'])
const teamName = ref('')
const viewTeamEdit = ref(false);
const selectedTeam = ref('')

defineProps({
    teamList: Array
})

const foundNewTeam = () => {
    console.log('Attempting to found new team...');
}

const updateList = () => {
    emit('updateTeamList', true)
}

const showTeamEdit = (hideTeamEdit) => {
    if (hideTeamEdit[0]) {
        viewTeamEdit.value = false
    } else {
        selectedTeam.value = hideTeamEdit[1]
        viewTeamEdit.value = true
    }
}

const showMessage = (message) => {
    console.log(message);
    msg.value = message
}
</script>