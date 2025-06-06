<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Login</h2>

        <!-- Message-Box -->
        <div v-if="msg !== ''"
            :class="msg === 'Incorrect credentials!' ? 'w-fit max-w-sm bg-gray-100 text-red-600 font-semibold rounded-lg shadow-md p-1 mx-auto' : 'w-fit max-w-sm bg-gray-100 text-gray-800 font-semibold rounded-lg shadow-md p-1 mx-auto'">
            <p>{{ msg }}</p>
        </div>

        <form @submit.prevent="handleLogin">
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Username
                    <input v-model.trim="username" type="text" placeholder="Username" required
                        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Password
                    <input v-model.trim="password" :type="showPassword ? 'text' : 'password'" type="password"
                        placeholder="Password" required
                        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                </label>
            </div>
            <div class="mb-14">
                <label class="float-right">
                    Show password
                    <input v-model="showPassword" type="checkbox">
                </label>
            </div>
            <button type="submit"
                class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 transition">
                Log In
            </button>
        </form>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router';
import { useAuthService } from '@/services/AuthService'

const router = useRouter();

const username = ref('')
const password = ref('')
const showPassword = ref(false)
const { login, loading, isAuthenticated } = useAuthService()
const msg = ref('')

watch(loading, (newVal) => {
    if (newVal) {
        msg.value = "Logging in..."
    } else {
        msg.value = ""
    }
})

const handleLogin = async () => {
    await login(username.value, password.value)

    if (isAuthenticated.value) {
        router.replace('/tasks');
    } else {
        msg.value = "Incorrect credentials!"
    }
}
</script>
