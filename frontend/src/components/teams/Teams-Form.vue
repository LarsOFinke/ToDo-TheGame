<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Create a new team!</h2>

        <!-- Message-Box -->
        <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

        <form @submit.prevent="submitNewTeam">
            <!-- Team-Name -->
            <div class="flex flex-col justify-between mb-4">
                <label class="flex text-sm font-medium text-gray-700 justify-between mb-2">Team
                    <input v-model.trim="teamName" type="text" placeholder="Team name" required
                        class="mt-1 w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>

            <!-- Team-Description -->
            <div class="flex flex-col justify-between mb-4">
                <label class="flex text-sm font-medium text-gray-700 justify-between mb-2">Description
                    <textarea v-model.trim="description"
                        placeholder="Describe your teams purpose and a quick general overview." required
                        class="mt-1 w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>

            <!-- Utility-Buttons -->
            <div class="w-full flex justify-between">
                <button type="button" @click.prevent="showTaskList"
                    class="w-fit bg-red-700 text-white py-1 px-4 rounded-md hover:bg-red-800 transition">Back</button>

                <button type="reset"
                    class="w-fit bg-indigo-600 text-white py-1 px-4 rounded-md hover:bg-indigo-800 transition">Reset</button>

                <button type="submit"
                    class="w-fit bg-indigo-600 text-white py-1 px-2 rounded-md hover:bg-indigo-800 transition">Submit</button>
            </div>
        </form>
    </div>
</template>

<script setup>
import MessageBox from '@/components/shared/Message-Box.vue';
import { ref, watch } from 'vue';
import { useAuthService } from '@/services/AuthService';
import { useTeamsService } from '@/services/TeamsService';

const emit = defineEmits(['hideTeamForm'])
const msg = ref('')
const errorPhrase = 'Something went wrong!'
const { userId } = useAuthService()
const { loading, createNewTeam } = useTeamsService()
const teamName = ref('')
const description = ref('')

watch(loading, (newVal) => {
    if (newVal) {
        msg.value = "Creating team..."
    } else {
        msg.value = ""
    }
})

const showTaskList = () => {
    emit('hideTeamForm', false)
}

const submitNewTeam = async () => {
    const newTeam = {
        teamName: teamName.value,
        userId: userId.value,
        teamDescription: description.value,
    }

    if (await createNewTeam(newTeam)) {
        msg.value = 'Successfully created new team!'
    } else {
        msg.value = 'Something went wrong!'
    }

}
</script>