<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Profile</h2>

        <!-- Message-Box -->
        <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

        <div class="flex mb-4 justify-between">
            <label class="flex text-sm font-medium text-gray-700">Username
                <input v-model.trim="username" type="text" placeholder="Username" required
                    class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
            </label>
            <button type="button" class="bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 transition"
                @click.prevent="editUsername">
                Edit
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

// onMounted(async () => {
//     if (!isAuthenticated.value) {
//         router.replace('/');
//     }
// });

const editUsername = () => {
    console.log(username.value);
}
</script>