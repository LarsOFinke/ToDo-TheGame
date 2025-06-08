<template>
    <div>
        <div v-if="!viewTeamEdit" class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-6 mx-auto relative">
            <!-- Scrollable Team List -->
            <div class="overflow-x-auto max-h-95">
                <ul v-for="team in teamList" :key="task.id" class="mb-8">
                    <team-item :task="task" @hideTeamEdit="showTeamEdit" @updateTeamList="updateList"
                        @closeItem="showMessage"></team-item>
                </ul>
            </div>
        </div>

        <!-- <teams-item-edit v-else :team="selectedTeam" @hideItemEdit="showTeamEdit"></teams-item-edit> -->
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
const viewTeamEdit = ref(false);
const selectedTeam = ref('')

defineProps({
    teamList: Array
})

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