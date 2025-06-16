<template>
    <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-2 mx-auto relative mb-2">
        <h3 class="text-lg mb-2 font-semibold">Member-List</h3>

        <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-1 mx-auto relative mb-2">
            <div class="text-sm mb-4 overflow-x-auto pl-6 max-h-24">
                <ul class="mb-2">
                    <li class="mb-1">Member #1</li>
                    <li class="mb-1">Member #2</li>
                    <li class="mb-1">Member #3</li>
                    <li class="mb-1">Member #4</li>
                </ul>
            </div>
        </div>

    </div>
</template>

<script setup>

const emit = defineEmits(['hideTeamDetails'])

const showTeamList = () => { emit('hideTeamDetails', true) }
</script>