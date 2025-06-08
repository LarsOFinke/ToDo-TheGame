<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Profile</h2>

        <!-- Message-Box -->
        <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

        <div class="flex flex-col mb-4 justify-between">
            <label class="flex text-sm font-medium text-gray-700 justify-between mb-4">Username
                <input v-model.trim="username" type="text" placeholder="Username" required
                    class="mt-1 block w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
            </label>

            <button type="button"
                class="bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 transition h-fit"
                @click.prevent="editUsername">
                Edit
            </button>
        </div>

        <hr>

        <div class="flex flex-col mt-4 justify-between">
            <label class="flex text-sm font-medium text-gray-700 mb-2 justify-between">New password
                <input v-model.trim="newPassword1" :type="showPassword ? 'text' : 'password'" placeholder="New password" required
                    class="mt-1 block w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
            </label>

            <label class="flex text-sm font-medium text-gray-700 mb-2 justify-between">Confirmation
                <input v-model.trim="newPassword2" :type="showPassword ? 'text' : 'password'" placeholder="Confirm new password" required
                    class="mt-1 block w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
            </label>

            <div class="mb-4">
                <label class="float-right">
                    Show password
                    <input v-model="showPassword" type="checkbox">
                </label>
            </div>

            <button type="button"
                class="bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 transition h-fit"
                @click.prevent="changePassword">
                Change password
            </button>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import MessageBox from '@/components/shared/Message-Box.vue'
import { useRouter } from 'vue-router';
import { useAuthService } from '@/services/AuthService'

const router = useRouter();
const { user, isAuthenticated } = useAuthService()
const msg = ref('')
const errorPhrase = 'Incorrect credentials!'
const username = ref(user)
const newPassword1 = ref('')
const newPassword2 = ref('')
const showPassword = ref(false)

// onMounted(async () => {
//     if (!isAuthenticated.value) {
//         router.replace('/');
//     }
// });

const editUsername = () => {
    console.log(username.value);
}

const changePassword = () => {
    if (newPassword1.value === newPassword2.value) {
        console.log('Attempting to change password...');
    }
}
</script>