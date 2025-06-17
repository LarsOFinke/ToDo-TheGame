<template>
    <div class="flex mb-4">
        <button type="button"
            class="bg-yellow-600 text-white py-2 px-4 rounded-md hover:bg-yellow-800 transition h-fit mb-4 mx-auto"
            @click.prevent="cancelEditMode">
            Exit edit mode
        </button>
    </div>

    <!-- Message-Box -->
    <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

    <div class="flex flex-col mb-4 justify-between">
        <label class="flex text-sm font-medium text-gray-700 justify-between mb-2">User
            <input v-model.trim="username" type="text" placeholder="Username" required
                class="mt-1 block w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
        </label>

        <button type="button" class="bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 transition h-fit"
            @click.prevent="newUsername">
            Edit
        </button>
    </div>

    <hr>

    <div class="flex flex-col mt-4 justify-between">
        <label class="flex text-sm font-medium text-gray-700 mb-2 justify-between">New password
            <input v-model.trim="newPassword1" :type="showPassword ? 'text' : 'password'" placeholder="New password"
                required
                class="mt-1 block w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
        </label>

        <label class="flex text-sm font-medium text-gray-700 mb-2 justify-between">Confirmation
            <input v-model.trim="newPassword2" :type="showPassword ? 'text' : 'password'"
                placeholder="Confirm new password" required
                class="mt-1 block w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
        </label>

        <div class="mb-4">
            <label class="float-right">
                Show passwords
                <input v-model="showPassword" type="checkbox">
            </label>
        </div>

        <button type="button" class="bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 transition h-fit"
            @click.prevent="newPassword">
            Change password
        </button>
    </div>
</template>

<script setup>
import MessageBox from '@/components/shared/Message-Box.vue'
import { ref } from 'vue';
import { useAuthService } from '@/services/AuthService'

const msg = ref('')
const errorPhrase = 'Something went wrong!'
const { user, userId, changeUsername, changePassword } = useAuthService()
const username = ref(user)
const newPassword1 = ref('')
const newPassword2 = ref('')
const showPassword = ref(false)
const emit = defineEmits(['showEditMode'])

const cancelEditMode = () => {
    emit('showEditMode', false)
}

const newUsername = () => {
    if (changeUsername(userId.value, username.value)) {
        msg.value = "Username successfully changed!"
    }
}

const newPassword = () => {
    if (newPassword1.value === newPassword2.value) {
        if (changePassword(userId.value, newPassword1.value)) {
            msg.value = "Password successfully changed!"
        }
    }
}
</script>