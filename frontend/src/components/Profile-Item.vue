<template>
    <div class="flex mb-4">
        <button type="button"
            class="bg-yellow-600 text-white py-2 px-4 rounded-md hover:bg-yellow-800 transition h-fit mb-4 mx-auto"
            @click.prevent="activateEditMode">
            Edit mode
        </button>
    </div>

    <div class="flex flex-col mb-4 justify-between">
        <label class="flex text-sm font-medium text-gray-700 justify-between">User
            <label
                class="mt-1 block w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">{{
                    user }}</label>
        </label>
    </div>

    <hr>

    <div class="flex flex-col mt-4 justify-between">
        <label class="flex text-sm font-medium text-gray-700 justify-between mb-4">User
            <label
                class="mt-1 block w-50 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">{{
                    user }}</label>
        </label>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthService } from '@/services/AuthService'

const { user } = useAuthService()
const emit = defineEmits(['showEditMode'])

const activateEditMode = () => {
    emit('showEditMode', true)
}
</script>