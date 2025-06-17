<template>
    <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-2 mx-auto relative mb-2">
        <div class="text-sm mb-4 overflow-x-auto max-h-57">
            <div class="flex flex-col relative text-xs mb-4">
                <div class="flex flex-col w-35">
                    <label class="mb-2"><u>Leader:</u> {{ team.leader.name }}</label>
                    <label class="mb-1"><u>Description:</u> </label>
                </div>
                <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-1 mx-auto relative mb-2">
                    <div class="text-sm mb-4 overflow-x-auto pl-6 max-h-24">
                        {{ props.team.description }}
                    </div>
                </div>

                <div class="absolute -top-1 right-0">
                    <div class="w-full">
                        <label class="text-sm font-semibold">Members:</label>
                        <p class="text-sm text-right">{{ memberCount }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    team: Object,
    memberCount: Number,
})
</script>