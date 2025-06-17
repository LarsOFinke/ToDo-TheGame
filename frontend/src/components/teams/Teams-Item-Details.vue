<template>
    <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-2 mx-auto relative mb-2">
        <h3 class="text-lg mb-2 font-semibold">Member-List</h3>

        <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-1 mx-auto relative mb-2">
            <div class="text-sm mb-4 overflow-x-auto pl-6 max-h-24">
                <ul v-for="member in memberList" class="mb-2">
                    <members-item :member="member"></members-item>
                </ul>
            </div>
        </div>

    </div>
</template>

<script setup>
import MembersItem from '@/components/members/Members-Item.vue';

const props = defineProps({
    memberList: Array,
})
</script>