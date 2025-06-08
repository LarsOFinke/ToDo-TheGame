<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Register</h2>

        <!-- Message-Box -->
        <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

        <form @submit.prevent="signUp" class="flex flex-col">
            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Username
                    <input v-model.trim="username" type="text" placeholder="Username"
                        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
                </label>
            </div>

            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Password
                    <input v-model.trim="password" :type="showPassword ? 'text' : 'password'" placeholder="Password"
                        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
                </label>
            </div>

            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Password confirm
                    <input v-model.trim="passwordConfirm" :type="showPassword ? 'text' : 'password'"
                        placeholder="Password confirm"
                        class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
                </label>
            </div>

            <div class="mb-4">
                <label class="float-right">
                    Show password
                    <input v-model="showPassword" type="checkbox">

                </label>
            </div>

            <div class="flex justify-between">
                <button type="reset"
                    class="w-fit bg-indigo-600 text-white py-2 px-10 rounded-md hover:bg-indigo-800 transition">Reset</button>
                <button type="submit"
                    class="w-fit bg-indigo-600 text-white py-2 px-8 rounded-md hover:bg-indigo-800 transition">Register</button>
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router';
import MessageBox from './shared/Message-Box.vue';
import { useAuthService } from '@/services/AuthService'

const router = useRouter();
const { register, loading } = useAuthService()

const msg = ref('')
const errorPhrase = 'Passwords don\'t match!'
const username = ref('')
const password = ref('')
const passwordConfirm = ref('')
const showPassword = ref(false)

watch(loading, (newVal) => {
    if (newVal) {
        msg.value = "Registering..."
    } else {
        msg.value = ""
    }
})

const signUp = async () => {
    console.log(username.value, password.value);

    if (checkPasswordRequirements()) {
        if (await register(username.value, password.value)) {
            router.replace("/")
        }
    }
}

const checkPasswordRequirements = () => {
    if (password.value === passwordConfirm.value) {
        return true
    } else {
        msg.value = "Passwords don't match!"
        return false
    }
}
</script>