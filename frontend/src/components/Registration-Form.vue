<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Register</h2>
        <form @submit.prevent="register" class="flex flex-col">
            <div class="mb-4">
                <input v-model.trim="username" type="text" placeholder="Username"
                    class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
            </div>

            <div class="mb-6">
                <input v-model.trim="password" :type="showPassword ? 'text' : 'password'" placeholder="Password"
                    class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
            </div>

            <div class="mb-6">
                <input v-model.trim="passwordConfirm" :type="showPassword ? 'text' : 'password'"
                    placeholder="Password confirm"
                    class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
            </div>

            <div class="mb-6">
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
import { ref } from 'vue'

const username = ref('')
const password = ref('')
const passwordConfirm = ref('')
const showPassword = ref(false)

const register = () => {
    console.log(username.value, password.value);

    checkPasswordRequirements()
}

const checkPasswordRequirements = () => {
    if (password.value === passwordConfirm.value) {
        console.log('test');
    }
}
</script>