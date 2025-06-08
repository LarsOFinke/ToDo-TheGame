<template>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md p-6 mx-auto">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Team form</h2>

        <!-- Message-Box -->
        <message-box :msg="msg" :errorPhrase="errorPhrase"></message-box>

        <div class="flex mb-4">
            <label class="flex text-sm font-medium text-gray-700 justify-between mb-2">Team
                <input v-model.trim="teamName" type="text" placeholder="Team name" required
                    class="mt-1 block w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
            </label>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const msg = ref('')
const errorPhrase = 'Something went wrong!'
const teamName = ref('')

</script>